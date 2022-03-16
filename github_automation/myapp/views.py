from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def main_page(request):
    # return the index.html file under the html folder
    template = loader.get_template('html/index.html')
    return HttpResponse(template.render())
    
    