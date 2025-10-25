from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView, DetailView

from .forms import AddArticleForm
from .models import Article


class HomePage(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    extra_context = {
        'title': 'Main Page',
    }

    def get_queryset(self):
        return Article.published.all()


class ShowPost(DetailView):
    model = Article
    template_name = 'blog/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_object(self, queryset=None):
        return get_object_or_404(Article.published, slug=self.kwargs[self.slug_url_kwarg])


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