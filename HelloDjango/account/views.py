from django.shortcuts import render,redirect
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import RegisterForm
from .models import UserProfile, PaymentAccount, Region
from django.contrib.auth.models import User
from site_app.views import get_lng


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("login")
    template_name = 'sign-up.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lng"] = get_lng(self.request)
        return context
    


class ProfilePageView(TemplateView):
    template_name = 'account.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["regions"] = Region.objects.all()
        context["lng"] = get_lng(self.request)
        return context
    


def save_inf(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.profile.phone_number = request.POST.get('phone_number')
        user.profile.save()
        return redirect('profile')
    
def save_address_inf(request):
    if request.method == 'POST':
        user = request.user
        user.profile.region = Region.objects.get(name=request.POST.get('region'))
        user.profile.city = request.POST.get('city')
        user.profile.postal_code = request.POST.get('postal_code')
        user.profile.street = request.POST.get('street')
        user.profile.house = request.POST.get('house')
        user.profile.apartment = request.POST.get('apartment')
        user.profile.save()
        user.save()
        return redirect('profile')
    
