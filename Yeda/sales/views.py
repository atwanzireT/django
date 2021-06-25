from django.shortcuts import render
from .models import Sale
from django.views.generic import ListView, DetailView
from .forms import SalesSearchFrom

# Create your views here.
def home_view(request):
    hello = 'Hello Fedora People'
    form = SalesSearchFrom(request.POST or None)

    if request.method == 'POST':
        date_from = request.POST.get('date_form')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        print(date_from)

    context = {
        'welcome': hello,
        'form': form,
    }
    return render(request, 'sales/home.html', context)

class SalesListView(ListView):
    model = Sale
    template_name = 'sales/main.html'

class SalesDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'
