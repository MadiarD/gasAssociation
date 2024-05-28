from django.shortcuts import render ,redirect
import uuid
import json
from yookassa import Configuration, Payment
from django.views.generic import TemplateView
from site_app.views import get_lng
from news.views import last_news
from .models import Receipt
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from notification.models import Notification
from django.contrib.auth.models import User

Configuration.account_id = 385637
Configuration.secret_key = 'test_3_FbH_H-V7l3A8I9lR_zxfLa-rgETX8nJlkn1aZcuuk'


class CalculationPageView(TemplateView):
    template_name = 'calculation.html'

    def post(self,request, *args, **kwargs):
        Receipt.objects.all()[0].create_receipt_pdf()

        second = float(request.POST.get('second'))
        first = float(request.user.payment_account.meter_indicator)
        amount = request.user.payment_account.provider.detail.price_per_m3
        if(first > second):
            return redirect('calculation')
        amount = amount * (second - first)/5.0
        payment = Payment.create({
            "amount": {
                "value": f"{amount}",
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://gas-association.website/payment/calculation"
            },
            "capture": True,
            "description": f"Лицевой счет {request.user.payment_account.number} за {second-first} куб.м. газа"
        }, uuid.uuid4())
        receipt = Receipt.objects.create(id_p = payment.id, user = request.user, date = payment.created_at, amount = payment.amount.value*5, description = payment.description, status = payment.status, gas_volume = second-first, rate = request.user.payment_account.provider.detail.price_per_m3)
        receipt.save()
        return redirect(payment.confirmation.confirmation_url)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["receipt"] = Receipt.objects.filter(user = self.request.user)
        context["lng"] = get_lng(self.request)
        context["last_news"] = last_news(self.request)
        return context
    
   
@require_POST
@csrf_exempt
def yookassa_notification(request):
    try:
        data = json.loads(request.body)
        payment_id = data.get('object', {}).get('id')
        status = data.get('object', {}).get('status')
        event = data.get('event')
        
        if(event == 'payment.succeeded'):
            
            payment = Receipt.objects.get(id_p = payment_id)
            payment.status = status
            Notification.objects.create(user = User.objects.get(username = payment.user), message = f'{payment_id} толемі сәтті аяқталды')
            payment.user.payment_account.meter_indicator = float(payment.user.payment_account.meter_indicator) + payment.gas_volume
            payment.user.payment_account.save()
            payment.create_receipt_pdf()
                
            payment.save()

        return HttpResponse(status=200)
    except Exception as e:
        print(f"Error: {e}")
        return HttpResponse(status=400)
