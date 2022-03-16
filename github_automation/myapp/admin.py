from django.contrib import admin

# Register your models here.

from myapp.models import GithubUser
myModels = [GithubUser]  # iterable list
admin.site.register(myModels)