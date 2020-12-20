from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'user/index.html')

def about_us(request):
	return render(request, 'user/about_us.html')

def contact_us(request):
	return render(request, 'user/contact_us.html')
def cart(request):
	return render(request, 'user/cart.html')
def product(request):
	return render(request, 'user/product.html')
def single_product(request):
	return render(request, 'user/single_product.html')
def payment(request):
	return render(request, 'user/payment.html')
def confirmation(request):
	return render(request, 'user/confirmation.html')
def search(request):
	return render(request, 'user/search.html')

