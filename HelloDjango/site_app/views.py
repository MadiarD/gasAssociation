from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from news.views import last_news
from members.views import members

def get_lng(request):
    cocckie = request.COOKIES.get('lng')
    if cocckie:
        return cocckie
    else:
        return 'ru'

class HomePageView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["last_news"] = last_news(self.request)
        context["members"] = members()
        context['lng'] = get_lng(self.request)
        return context
    


class AboutPageView(TemplateView):
    template_name = 'about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lng"] = get_lng(self.request)
        return context


class ContactPageView(TemplateView):
    template_name = 'contact.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["last_news"] = last_news(self.request)
        context["lng"] = get_lng(self.request)  
        return context

class BlogPageView(TemplateView):
    template_name = 'personal_blog.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lng"] = get_lng(self.request)
        return context
