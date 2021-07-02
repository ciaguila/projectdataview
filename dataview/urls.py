from django.urls import path
from . import views

app_name = 'dataview'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new', views.CreateView.as_view(), name='create'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'), 
    path('upload-csv/', views.data_upload, name="data_upload"),
    path('graphdata', views.GraphView.as_view(), name="graphdata"), 
]