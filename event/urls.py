from django.urls import path
from . import views

app_name = 'event'

urlpatterns = [
    path('', views.index, name='index'),
    path('allevents/', views.EventListView.as_view(), name='all-events'),
]