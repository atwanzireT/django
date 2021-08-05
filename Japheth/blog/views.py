from blog.models import Category, Headline
from django.shortcuts import render
from services.models import Service
# Create your views here.


def index(request):
    categorys = Category.objects.all()
    services = Service.objects.all()
    dict_context = {
        'categorys': categorys,
        'services': services,
    }
    return render(request, 'index.html', dict_context)


def blog(request):
    return render(request, 'blog.html')
