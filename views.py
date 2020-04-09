from django.shortcuts import render

# Create your views here.
def home(request):
    """ Display home page """
    return render(request, 'home.html')

def coming_soon(request):
    """ Display coming_soon page """
    return render(request, 'coming_soon.html')
