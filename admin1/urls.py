from django.contrib import admin
from django.urls import path,include
from admin1 import views 
urlpatterns = [
	path('index', views.index),
	path('add_user', views.add_user),
	path('area', views.area),
	path('dashboard', views.dashboard),
	path('category',views.category),
	path('sub_category',views.sub_category),
	path('product',views.product),
	path('gallery',views.gallery),
	path('order',views.order),
	path('payment',views.payment),
	path('contactus',views.contactus),
	path('review',views.review),
	path('visitor',views.visitor),
	path('cat_delete/<int:id>', views.cat_delete),
    path('cat_edit/<int:id>', views.cat_edit),
    path('cat_data_update/<int:id>', views.cat_edit_update),
    path('area_delete/<int:id>', views.area_delete),
    path('area_edit/<int:id>', views.area_edit),
    path('area_data_update/<int:id>', views.area_edit_update),
    path('sub_category_delete/<int:id>',views.sub_category_delete),
    path('sub_category_edit/<int:id>',views.sub_category_edit),
 	path('product_delete/<int:id>',views.product_delete),
 	path('product_edit/<int:id>',views.product_edit),
 	path('product_show1/<int:id>',views.product_show1)


	
]
 