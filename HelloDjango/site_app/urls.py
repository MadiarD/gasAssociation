from django.urls import path, re_path, include
from site_app.views import *
urlpatterns = [
    re_path(r'^$',HomePageView.as_view(),name = 'home_page'),
    re_path(r'^about$',AboutPageView.as_view(),name = 'about'),
    re_path(r'^contacts$',ContactPageView.as_view(),name = 'contacts'),
    re_path(r'^personal_blog$',BlogPageView.as_view(),name = 'personal_blog'),
]