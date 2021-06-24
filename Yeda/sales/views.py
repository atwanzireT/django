from django.shortcuts import render
from .models import Sale
from django.views.generic import ListView, DetailView

# Create your views here.
def home_view(request):
    hello = 'Hello Fedora People'
    return render(request, 'sales/home.html', {'welcome':hello})

class SalesListView(ListView):
    model = Sale
    template_name = 'sales/main.html'

class SalesDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'