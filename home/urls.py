from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),
    path("services/", views.services, name='services'),
    path("contact/", views.contact, name='contact'),
    path("blog/", views.blog, name='blog'),
    path("blogpost/<slug:slug>/", views.blogpost, name='blog'),
    path("search/", views.search, name='search')
]