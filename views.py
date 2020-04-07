from django.shortcuts import render

# Create your views here.
def home(request):
    """ Display home page """

    return render(request, 'home.html')
