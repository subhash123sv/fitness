from django.shortcuts import render, redirect
from user.models import category_data,area_data,sub_category_data,product_data
from django.core.files.storage import FileSystemStorage
#from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

def index(request):
	return render(request, 'admin1/layout/master.html')

def add_user(request):

	return render(request, 'admin1/add_user.html')

def area(request):
	if request.method == 'POST':
		area_store=request.POST['area_name']
		area_pincode=request.POST['pincode']
		print(area)
		area_update = area_data(area_name=area_store,pincode=area_pincode)
		area_update.save()
		return redirect('/admin1/area')
	else:
		area_show = area_data.objects.all()
		#start paginator logic
		paginator=Paginator(area_show,3)  		
		page=request.GET.get('page')
		try:
			area_show=paginator.page(page)
		except PageNotAnInteger:
			area_show=paginator.page(1)
		except EmptyPage:
			area_show=paginator.page(paginator.num_pages)
			#end paginator logic
		return render(request, 'admin1/area.html',{'area_show':area_show})


def area_delete(request,id):
	area_delete=area_data.objects.filter(id=id)
	area_delete.delete()
	return redirect('/admin1/area')

def area_edit(request,id):
	area_edit=area_data.objects.filter(id=id)
	return render(request, 'admin1/area.html', {'area_edit':area_edit})


def area_edit_update(request,id):
	if request.method == 'POST':
		area_store=request.POST['area_name']
		area_pincode=request.POST['pincode']
		area_update = area_data(id=id,area_name=area_store,pincode=area_pincode)
		area_update.save()
		return redirect('/admin1/area')


def dashboard(request):
	return render(request, 'admin1/dashboard.html')

def category(request):
	if request.method == 'POST':
		category_store=request.POST['cat_name']
		print(category)
		category_update = category_data(cat_name=category_store)
		category_update.save()
		return redirect('/admin1/category')
	else:
		category_show = category_data.objects.all()
		#start paginator logic
		paginator=Paginator(category_show,3)  		
		page=request.GET.get('page')
		try:
			category_show=paginator.page(page)
		except PageNotAnInteger:
			category_show=paginator.page(1)
		except EmptyPage:
			category_show=paginator.page(paginator.num_pages)
			#end paginator logic
		return render(request,'admin1/category.html', {'category_show':category_show})

def cat_delete(request,id):
	cat_deletee=category_data.objects.filter(id=id)
	cat_deletee.delete()
	return redirect('/admin1/category')

def cat_edit(request,id):
	cat_edit=category_data.objects.filter(id=id)
	return render(request, 'admin1/category.html', {'cat_edit':cat_edit})

def cat_edit_update(request,id):
	if request.method == 'POST':
		category_store=request.POST['cat_name']
		print(category)
		category_update = category_data(id=id,cat_name=category_store)
		category_update.save()
		return redirect('/admin1/category')


def sub_category(request):
	if request.method == 'POST':
		category=request.POST['cat_name']
		sub_category=request.POST['s_name']
		sub_category_store = sub_category_data(cat_id=category_data(category),s_name=sub_category)
		sub_category_store.save()
		return redirect('/admin1/sub_category')
	else:
		category_show = category_data.objects.all()
		sub_category_show=sub_category_data.objects.all()
		#start paginator logic
		paginator=Paginator(sub_category_show,3)  		
		page=request.GET.get('page')
		try:
			sub_category_show=paginator.page(page)
		except PageNotAnInteger:
			sub_category_show=paginator.page(1)
		except EmptyPage:
			sub_category_show=paginator.page(paginator.num_pages)
			#end paginator logic
		return render(request,'admin1/sub_category.html', {'category_show':category_show,'sub_category_show':sub_category_show})

def sub_category_delete(request, id):
	sub_category_delete=sub_category_data.objects.filter(id=id)
	sub_category_delete.delete()
	return redirect('/admin1/sub_category')

def sub_category_edit(request, id):
	if request.method == 'POST':
		category=request.POST['cat_name']
		sub_category=request.POST['s_name']
		sub_category_store = sub_category_data(id=id, cat_id=category_data(category),s_name=sub_category)
		sub_category_store.save()
		return redirect('/admin1/sub_category')
	else:
		category_show=category_data.objects.all()
		sub_category_edit=sub_category_data.objects.filter(id=id)
		return render(request,'admin1/sub_category.html',{'sub_category_edit':sub_category_edit,'category_show':category_show})

def product(request):
	if request.method=='POST':
		sub_category=request.POST['s_name']
		product_name=request.POST['p_name']
		product_price=request.POST['p_price']
		product_desc=request.POST['p_desc']
		product_image=request.FILES['p_image']
		fs1=FileSystemStorage()
		filename1=fs1.save(product_image.name, product_image)
		url1=fs1.url(filename1)
		product_store=product_data(s_id=sub_category_data(sub_category),p_name=product_name,p_price=product_price,p_desc=product_desc,p_image=url1)
		product_store.save()
		return redirect('/admin1/product')
	else:
		sub_category_show=sub_category_data.objects.all()
		product_show=product_data.objects.all()
		#start paginator logic
		paginator=Paginator(product_show,3)  		
		page=request.GET.get('page')
		try:
			product_show=paginator.page(page)
		except PageNotAnInteger:
			product_show=paginator.page(1)
		except EmptyPage:
			product_show=paginator.page(paginator.num_pages)
			#end paginator logic
		return render(request,'admin1/product.html',{'sub_category_show':sub_category_show,'product_show':product_show})

def product_delete(request,id):
	product_delete=product_data.objects.filter(id=id)
	product_delete.delete()
	return redirect('/admin1/product')

def product_edit(request,id):
	if request.method == 'POST':
		sub_category=request.POST['s_name']
		product_name=request.POST['p_name']
		product_price=request.POST['p_price']
		product_desc=request.POST['p_desc']
		product_image=request.FILES['p_image']
		fs1=FileSystemStorage()
		filename1=fs1.save(product_image.name, product_image)
		url1=fs1.url(filename1)
		product_store=product_data(id=id,s_id=sub_category_data(sub_category),p_name=product_name,p_price=product_price,p_desc=product_desc,p_image=product_image)
		product_store.save()
		return redirect('/admin1/product')


	else:
		sub_category_show=sub_category_data.objects.all()
		product_edit=product_data.objects.filter(id=id)
		return render(request, 'admin1/product.html',{'product_edit':product_edit,'sub_category_show':sub_category_show})


def product_show1(request,id):
	product_show1=product_data.objects.filter(id=id)
	return render(request,'admin1/product.html',{'product_show1':product_show1})















def gallery(request):
	return render(request,'admin1/gallery.html')
def order(request):
	return render(request,'admin1/order.html')
def payment(request):
	return render(request,'admin1/payment.html')
def contactus(request):
	return render(request,'admin1/contactus.html')
def review(request):
	return render(request,'admin1/review.html')

#def login(request):
	#return render(request,'login.html')
def login1(request):
	return render(request,'login1.html')
def visitor(request):
	return render(request,'admin1/visitor.html')

