from django.shortcuts import render
from .forms import ThingForm

def home(request):
    form = ThingForm()

    if request.method == 'POST':
        form = ThingForm(request.POST)

        if form.is_valid():
            pass
    return render(request, 'home.html', {'form': form})
