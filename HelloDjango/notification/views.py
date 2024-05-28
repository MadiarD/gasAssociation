
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def notifications_page(request):
    return render(request, 'notifications_page.html')

@login_required
def get_notifications(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False).order_by('-created_at')
    data = [{
        'message': notification.message,
        'created_at': notification.created_at
    } for notification in notifications]

    # Отметить уведомления как прочитанные
    notifications.update(is_read=True)
    return JsonResponse(data, safe=False)

