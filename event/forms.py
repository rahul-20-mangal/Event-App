from django import forms
from event.models import Event, Timing

class EventForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = ('title','place','tags')

class TimingForm(forms.ModelForm):
    
    class Meta:
        model = Timing
        fields = ('event_date','event_time')