from django.shortcuts import render
from django.views import View
from django.views.generic import ListView


class HomePage(ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        return None

class ShowPost(View):
    pass


class BlogCategory(View):
    pass