import csv
import io
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

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
    fields = ['xdata', 'ydata']
    success_url = reverse_lazy('dataview:index')


class UpdateView(generic.edit.UpdateView):
    template_name = 'dataview/update.html'
    model = Data
    fields = ['xdata', 'ydata']
    success_url = reverse_lazy('dataview:index')


class DeleteView(generic.edit.DeleteView):
    template_name = 'dataview/delete.html'
    model = Data
    success_url = reverse_lazy('dataview:index')

class GraphView(TemplateView):
    template_name = 'dataview/graphdata.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Data.objects.all()
        return context


def data_upload(request):
    template_name = "dataview/data_upload.html"

    if request.method == "GET":
        return render(request, template_name)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        message.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Data.objects.update_or_create(
            xdata= int(column[0]),
            ydata= int(column[1]),
        )
    context = {}

    if request.method == "POST":
        return redirect('dataview:index')
    

    return render(request, template_name, context)


def delete_data(request):
    if request.method == 'GET':
        Data.objects.all().delete()
    return redirect('dataview:index')