# PurpleMindApp/urls.py
from django.conf.urls import url
from purplemindApp import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]