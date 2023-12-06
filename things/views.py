from django.shortcuts import render
from things.forms import ThingForm

def home(request):
    form = ThingForm(request.POST)
    return render(request, 'home.html', {'form': form})
