from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.urls import reverse_lazy
from .models import Data

class IndexView(generic.ListView):
    template_name = 'dataview/index.html'
    context_object_name = 'dataview_list'    
    
    def get_queryset(self):
        """Return the all data."""
        return Data.objects.all()

class CreateView(generic.edit.CreateView):
    template_name = 'dataview/create.html'
    model = Data
    fields = ['ndata']
    success_url = reverse_lazy('dataview:index') 
    

class UpdateView(generic.edit.UpdateView):
    template_name = 'dataview/update.html'
    model = Data
    fields = ['ndata']
    success_url = reverse_lazy('dataview:index')
    
class DeleteView(generic.edit.DeleteView):
    template_name = 'dataview/delete.html' 
    model = Data
    success_url = reverse_lazy('dataview:index')

