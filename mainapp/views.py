from django.shortcuts import render
from .top25 import top25
# Create your views here.


def stockPicker(request):

    return render(request, 'stockpicker.html', {'top25': top25})


def stockTracker(request):

    selectedStocks = request.GET.getlist('pickstocks')

    return render(request, 'stocktracker.html', {'top25': top25, 'selectedStocks': selectedStocks})
