from django.urls import path,include
from user import views

urlpatterns = [
	path('', views.index),
	path('about_us', views.about_us),
	path('contact_us', views.contact_us),
	path('cart', views.cart),
	path('product', views.product),
	path('single_product', views.single_product),
	path('payment', views.payment),
	path('confirmation', views.confirmation),
	path('search', views.search)
]
 