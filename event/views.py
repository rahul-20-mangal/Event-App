from django.shortcuts import render
from event.models import Event, Timing
from django.views import generic
# Create your views here.

def index(request):
    return render(request, 'event/index.html')

class EventListView(generic.ListView):
    model = Event

