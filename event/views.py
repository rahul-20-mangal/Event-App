from django.shortcuts import render, redirect
from event.models import Event, Timing
from django.views import generic
from event.forms import EventForm, TimingForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from .filters import TimingFilter

# Create your views here.

def index(request):
    return render(request, 'event/index.html')

class EventListView(generic.ListView):
    model = Event

class EventDetailView(generic.DetailView):
    model = Event

class TimingListView(generic.ListView):
    model = Timing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TimingFilter(self.request.GET, queryset=self.get_queryset())
        return context


@login_required
def create_event(request):
    event_form = EventForm(request.POST or None)
    
    TimingFormSet = formset_factory(TimingForm, extra=2)
    timing_formset = TimingFormSet(request.POST or None)

    if event_form.is_valid() and timing_formset.is_valid():
        event = event_form.save()
        event.user = request.user

        for timing_form in timing_formset:
            timing = timing_form.save(commit=False)
            timing.event = event
            timing.save()
        return redirect('event:all-events')
    
    return render(request, 'event/create_event.html', {'event_form':event_form,'formset':timing_formset})


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