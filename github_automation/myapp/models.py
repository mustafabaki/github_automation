import email
from django.db import models

# Create your models here.



class GithubUser(models.Model):
    url = models.CharField(max_length=100, blank=True, null=True)
    html_url = models.CharField(max_length=100,blank=True, null=True)
    avatar_url = models.CharField(max_length=100,blank=True, null=True)
    type = models.CharField(max_length=100,blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    email = models.CharField(max_length=100,blank=True, null=True)
    hireable = models.CharField(max_length=100,blank=True, null=True)
    bio = models.CharField(max_length=100,blank=True, null=True)
    repos = models.CharField(max_length=100,blank=True, null=True)
    followers = models.CharField(max_length=100,blank=True, null=True)



    