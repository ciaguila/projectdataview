from django.views import generic
from django.urls import reverse_lazy
from .models import Post

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'    
    
    def get_queryset(self):
        """Return the all posts."""
        return Post.objects.all()

class CreateView(generic.edit.CreateView):
    template_name = 'blog/create.html'
    model = Post
    fields = ['author','title','text','created_date','published_date']
    success_url = reverse_lazy('blog:index') 
    

class UpdateView(generic.edit.UpdateView):
    template_name = 'blog/update.html'
    model = Post
    fields = ['author','title','text','created_date','published_date']
    success_url = reverse_lazy('blog:index')
    
class DeleteView(generic.edit.DeleteView):
    template_name = 'blog/delete.html' 
    model = Post
    success_url = reverse_lazy('blog:index')

class FilterSportView(generic.ListView):
    template_name = 'blog/sportfilter.html'
    context_object_name = 'filter_list'    
    
    def get_queryset(self):
        return Post.objects.filter(title__contains="Sport")

class FilterNewsView(generic.ListView):
    template_name = 'blog/newsfilter.html'
    context_object_name = 'filter_list'    
    
    def get_queryset(self):
        return Post.objects.filter(title__contains="News")

class OrderView(generic.ListView):
    template_name = 'blog/order.html'
    context_object_name = 'order_list'    
    
    def get_queryset(self):
        return Post.objects.order_by('-created_date')

class OrderSportView(generic.ListView):
    template_name = 'blog/order.html'
    context_object_name = 'order_list'    
    
    def get_queryset(self):
        return Post.objects.order_by('-created_date').filter(title__contains='Sport')
