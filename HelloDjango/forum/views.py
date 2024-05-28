from django.shortcuts import render,redirect
from .models import Message
from django.views.generic import TemplateView
from site_app.views import get_lng
from news.views import last_news
from notification.views import Notification
from django.contrib.auth.models import Group

def get_message(request):
    messages = Message.objects.exclude(answers = None).filter(public = True).order_by('-created_at')
    return messages
def get_user_message(request):
    if (request.user.profile.role =='lawyer'):
        messages = Message.objects.exclude(user = request.user).filter(answers = None).order_by('-created_at')
    else :
        messages = Message.objects.filter(user = request.user).order_by('-created_at')
    return messages

class ForumPageView(TemplateView):
    template_name = 'forum.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["messages"] = get_message(self.request)
        context["lng"] = get_lng(self.request)
        context["last_news"] = last_news(self.request)

        print(context)
        return context
    
class MessagePageView(TemplateView):
    template_name = 'message.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["messages"] = get_user_message(self.request)
        context["lng"] = get_lng(self.request)
        context["last_news"] = last_news(self.request)
        return context

def save_lawyer_message(request):
    if request.method == 'POST':
        Notification.objects.create(message = 'Сообщение отправлено',user = request.user)
        message = Message.objects.get(id = request.POST.get('id'))
        public = True if(request.POST.get('public') == 'on') else False
        message.answers.create(message = request.POST.get('message'),user = request.user) 
        message.public = public
        message.save()
        return redirect('messages')
    
def create_message(request):
    if request.method == 'POST':
        Notification.objects.create(message = 'Сообщение отправлено',user = request.user)
        group = Group.objects.get(name='lawyer')
        users = group.user_set.all()
        for user in users:
            notification = Notification(user=user, message=request.POST.get('message'))
            notification.save()
        Message.objects.create(message = request.POST.get('message'),user = request.user)
        return redirect(request.META.get('HTTP_REFERER'))