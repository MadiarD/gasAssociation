
from django.urls import path, re_path
from news.views import NewsPageView,NewsPageDetalisView,subscribe,NotificationPageView,ContractPageView,ReportPageView,InstructionPageView

urlpatterns = [
    path('',NewsPageView.as_view(),name = 'news'),
    path('<int:news_d>/',NewsPageDetalisView.as_view(),name = 'news_d'),
    path('subscribe/',subscribe,name = 'subscribe'),
    path('notification_docx',NotificationPageView.as_view(),name = 'notification_docx'),
    path('contract_docx',ContractPageView.as_view(),name = 'contract_docx'),
    path('report_docx',ReportPageView.as_view(),name = 'report_docx'),
    path('instruction_docx',InstructionPageView.as_view(),name = 'instruction_docx'),
]
