from django.contrib import admin
from .models import Event, Timing
# Register your models here.

class TimingInline(admin.TabularInline):
    model = Timing
    extra = 1

class EventAdmin(admin.ModelAdmin):
    inlines = [TimingInline]

admin.site.register(Event, EventAdmin)
