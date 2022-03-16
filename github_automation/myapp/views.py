from tkinter import EW
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import json

# import models from the models.py file
from .models import GithubUser

def main_page(request):
    # return the index.html file under the html folder
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def get_keyword(request):
    # get the keyword from the index.html file
    keyword = request.GET['keywords']

   # query = requests.get("https://api.github.com/search/users?q=" + keyword)

   # find users that match with the given keywords above from the github api
    query = requests.get("https://api.github.com/search/users?q=" + keyword)
    
    content = query.json()

    # print the each element in the json file
    for i in content['items']:
        url = i['url']

        # get the details of the user
        user_details = requests.get(url)

        # get the json file of the user
        user_details_json = user_details.json()

        # save the user details to the database
        user = GithubUser(url = url, html_url = user_details_json['html_url'], avatar_url = user_details_json['avatar_url'], type = user_details_json['type'], name = user_details_json['name'], email = user_details_json['email'], hireable = user_details_json['hireable'], bio = user_details_json['bio'], repos = user_details_json['public_repos'], followers = user_details_json['followers'])
        user.save()

    # return the html file under the html folder
    HttpResponse("<h1>The user details are saved in the database</h1>")
        

    
    return HttpResponse(content)
    
    