from django.shortcuts import render

# Create your views here.
def tests1(request):
    return render(request, 'tests1.html')