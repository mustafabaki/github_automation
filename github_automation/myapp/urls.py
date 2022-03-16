from django.urls import path
from . import views
urlpatterns = [
path('', views.main_page, name = 'main_page'),
path('get_keywords', views.get_keyword, name = 'get_keywords'),
]