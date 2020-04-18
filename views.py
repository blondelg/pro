from django.shortcuts import render
from pro_app.models import *

# Create your views here.
def home(request):
    """ Display home page """

    # load about
    about = []
    for elt in About.objects.filter(abo_display=True).order_by('abo_order'):
        temp = []
        temp.append(elt.abo_icon)
        temp.append(elt.abo_title)
        temp.append(elt.abo_description)
        about.append(temp)

    # load experience
    experience = []
    for elt in Experience.objects.filter(exp_display=True).order_by('exp_order'):
        temp = []
        temp.append(elt.exp_start.isoformat())
        temp.append(elt.exp_stop.isoformat())
        temp.append(elt.exp_poste)
        temp.append(elt.exp_compagny_name)
        temp.append(elt.exp_geo)
        experience.append(temp)
        print(experience)


    return render(request, 'home.html', {'about': about,'experience': experience})

def coming_soon(request):
    """ Display coming_soon page """
    return render(request, 'coming_soon.html')
