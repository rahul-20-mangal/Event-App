from django.shortcuts import render, redirect
from django.views import generic
from spot.models import Place
from spot.forms import PlaceForm
from django.contrib.gis.db.models import PointField

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

class PlaceListView(generic.ListView):
    model = Place

class PlaceDetailView(generic.DetailView):
    model = Place

def all_cities(request):
    place = Place.objects.distinct('city')
    return render(request, 'spot/all_cities.html', context={"all_places": place})

def cityplaces(request, inputcity):
    city = Place.objects.filter(city=inputcity)
    return render(request, 'spot/city_places.html', context={'cities':city})

def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.save()
            return redirect('spot:list-place')
    else:
        form = PlaceForm()
    
    return render(request, 'spot/add_place.html', {'form':form})




