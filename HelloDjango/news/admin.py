from django.contrib import admin
from .models import News, NewsDetails, NewsSubscribeList, Document

admin.site.register(News)
admin.site.register(NewsDetails)
admin.site.register(NewsSubscribeList)
admin.site.register(Document)