from django.shortcuts import render
from .calendar_API import test_calendar

# Create your views here.


def home(request):
    return render(request, 'home.html')


def demo(request):
    results = test_calendar()
    context = {"results": results}
    return render(request, 'demo.html', context)
