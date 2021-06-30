from django.forms.forms import Form
from django.shortcuts import render
from products.models import Product, Category
from django.http import HttpResponseRedirect
from .forms import Submit

# Create your views here.
def products(request):
	product = Product.objects.all()
	submit = Submit(request.POST or None)
	context = {
	    'products':product,
		'submit':submit
	}
 
	# form validation
	if request.method == 'POST':
		submitForm = Submit(request.POST)
		
	return render(request, 'main.html', context)