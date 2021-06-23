from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new', views.CreateView.as_view(), name='create'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path('sportfilter', views.FilterSportView.as_view(), name='sportfilter'),
    path('newsfilter', views.FilterNewsView.as_view(), name='newsfilter'),
    path('order', views.OrderView.as_view(), name='order'),
    path('ordersport', views.OrderSportView.as_view(), name='ordersport'),
]