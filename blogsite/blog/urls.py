from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.HomePage.as_view(),
         name='home'
         ),
    path('post/<slug:post_slug>/',
         views.ShowPost.as_view(),
         name='post'
         ),
    path('category/<slug:cat_slug>/',
         views.BlogCategory.as_view(),
         name='category'),
]
