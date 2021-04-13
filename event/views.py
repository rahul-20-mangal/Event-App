from django.shortcuts import render, redirect
from event.models import Event, Timing
from django.views import generic
from event.forms import EventForm, TimingForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'event/index.html')

class EventListView(generic.ListView):
    model = Event

class EventDetailView(generic.DetailView):
    model = Event

@login_required
def create_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        timing_form = TimingForm(request.POST)

        if event_form.is_valid() and timing_form.is_valid():
            x = event_form.save(commit=False)
            y = timing_form.save(commit=False)
            
            y.save()
            return redirect('event:all-events')
    else:
        event_form = EventForm()
        timing_form = TimingForm()
    
    return render(request, 'event/create_event.html', {'event_form':event_form,'timing_form':timing_form})

# def create_event(request):
#     if request.method == 'POST':
#         form = EventForm(request.POST)

#         if form.is_valid():
#             event = form.save(commit=False)
#             event.event_date = form.event_date
#             event.event_time = form.event_time
#             event.save()

#             return redirect('event:all-events')
#     else:
#         form = EventForm()
    
#     return render(request, 'event/create_event.html', {'form':form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('event:index')
    else:
        form = UserCreationForm()
    return render(request, 'event/signup.html', {'form': form})