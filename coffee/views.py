from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Coffee
from django.urls import reverse_lazy
# Create your views here.
class CoffeeListView(ListView):
    template_name='coffee/coffee_list.html'
    model=Coffee
    context_object_name="allcoffee"

class CoffeeDetailView(DetailView):
    template_name='coffee/coffee_detail.html'
    model=Coffee

class CoffeeCreateView(CreateView):
    template_name='coffee/coffee_create.html'
    model=Coffee
    fields=['title','purchaser','reviewer','price','img_url']

class CoffeeUpdateView(UpdateView):
    template_name='coffee/coffee_update.html'
    model=Coffee
    fields=['title','purchaser','reviewer','price','img_url']

class CoffeeDeleteView(DeleteView):
    template_name='coffee/coffee_delete.html'
    model=Coffee
    success_url=reverse_lazy('coffee_list')