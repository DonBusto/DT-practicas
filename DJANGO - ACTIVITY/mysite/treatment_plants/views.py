from django.shortcuts import render, redirect
#from .models import GreenTechTreatmentPlant
from .models import Activity
from django.http import HttpResponse
from .forms import ActivityForm
from .forms import NewActivityForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse
from django.shortcuts import redirect
import json
class CreateActivityView(CreateView):
    model = Activity
    fields = ['cnae', 'peso']

    def get_success_url(self):
        return reverse('treatment_plants:greentech_list')


def UploadCSV(request):
    content = request.POST.copy()
    content.pop('csrfmiddlewaretoken');
    data = json.loads(content.get('valores'))
    print(data)

    for element in data:
        if element['Peso']!='' and element['CNAE']!='':
            p = Activity(element['CNAE'],
                         element['Peso'])
            print(p)
            try:
                p.save()
            except:
                print("No introducido")
    print(request)

  #  return HttpResponse()
    return redirect('treatment_plants:greentech_list')

class ActivityView(ListView):
    model = Activity
