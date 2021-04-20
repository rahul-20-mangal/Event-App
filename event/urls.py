from django.urls import path
from . import views

app_name = 'event'

urlpatterns = [
    path('', views.index, name='index'),
    path('allevents/', views.EventListView.as_view(), name='all-events'),
    path('event_detail/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('create_event/', views.create_event, name='create-event'),
    path('filters/', views.TimingListView.as_view(), name='timing-filters'),
]