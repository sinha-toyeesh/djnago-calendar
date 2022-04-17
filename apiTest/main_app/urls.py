from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # more routes will go here
    path('rest/v1/calendar/init/', views.GoogleCalendarInitView, name='demo'),
]
