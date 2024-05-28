
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from news.models import News, NewsSubscribeList, Document

def get_lng(request):
    cocckie = request.COOKIES.get('lng')
    if cocckie:
        return cocckie
    else:
        return 'ru'


def last_news(request):
    news = News.objects.all().order_by('-date')[:5]
    return news

class NewsPageView(TemplateView):
    template_name = 'news.html'
    def get_context_data(self):
        context = super(NewsPageView, self).get_context_data()
        context['news'] = News.objects.all()
        context['last_news'] = last_news(self.request)
        context['lng'] = get_lng(self.request)
        return context


class NewsPageDetalisView(TemplateView):
    template_name = 'news-detalis.html'
    def get_context_data(self,news_d,**kwargs):

        context = super(NewsPageDetalisView, self).get_context_data()
        context['news'] = News.objects.get(id = news_d)
        context['last_news'] = last_news(self.request)
        context['lng'] = get_lng(self.request)
        return context
    
def subscribe(request):
    request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        email = request.POST['email']
        NewsSubscribeList.objects.create(email=email)
    return redirect(request.META.get('HTTP_REFERER'))


class NotificationPageView(TemplateView):
    template_name = 'notificationsdocx.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lng"] = get_lng(self.request)
        context["last_news"] = last_news(self.request)
        context["notification"] = Document.objects.filter(type = 'notification')
        return context

class ContractPageView(TemplateView):
    template_name = 'contractdocx.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lng"] = get_lng(self.request)
        context["last_news"] = last_news(self.request)
        context["contract"] = Document.objects.filter(type = 'contract')
        return context

class ReportPageView(TemplateView):
    template_name = 'reportdocx.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lng"] = get_lng(self.request)
        context["last_news"] = last_news(self.request)
        context["report"] = Document.objects.filter(type = 'report')
        return context

class InstructionPageView(TemplateView):
    template_name = 'instructiondocx.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lng"] = get_lng(self.request)
        context["instruction"] = Document.objects.filter(type = 'instruction')
        context["last_news"] = last_news(self.request)
        return context
