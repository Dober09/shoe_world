from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Product

# Create your views here.

class HomeTempleView(TemplateView):
    template_name = 'pages/index.html'

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'pages/men_shoe.html'

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'pages/order_shoe.html'


