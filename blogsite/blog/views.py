from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView

from .forms import AddArticleForm
from .models import Article


class HomePage(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'tasks'
    extra_context = {
        'title': 'Main Page',
    }

    def get_queryset(self):
        return Article.published.all()


class ShowPost(View):
    pass


class BlogCategory(View):
    pass


class AddPage(CreateView):
    template_name = 'blog/add_page.html'
    form_class = AddArticleForm
    extra_context = {
        'title': 'New post',
    }

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        w.slug = slugify(w.title)
        return super().form_valid(form)


class AboutView(TemplateView):
    template_name = 'blog/about.html'
    extra_context = {
        'title': 'About us',
    }


class ContactView(TemplateView):
    template_name = 'blog/contact.html'
    extra_context = {
        'title': 'Contacts',
    }