from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class customer_data(models.Model):
	c_id=models.AutoField
	user_id=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	f_name=models.TextField(max_length=20, default='')
	l_name=models.TextField(max_length=20, default='')
	Email=models.EmailField(max_length=20, default='')
	gender=models.BooleanField(max_length=6, default='')
	image=models.ImageField()
	con_no=models.IntegerField(default=0)
	address=models.CharField(max_length=100, default='')
	created_at=models.DateTimeField(default=timezone.now)
	updated_at=models.DateTimeField(default=timezone.now)


class area_data(models.Model):
	area_id=models.AutoField
	area_name=models.CharField(max_length=10, default='')
	pincode=models.IntegerField(default='')
	created_at=models.DateTimeField(default=timezone.now)
	updated_at=models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.area_name

class category_data(models.Model):
	cat_id=models.AutoField
	cat_name=models.CharField(max_length=30, default='')
	created_at=models.DateTimeField(default=timezone.now)
	updated_at=models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.cat_name


class sub_category_data(models.Model):
	s_id=models.AutoField
	cat_id=models.ForeignKey(category_data, on_delete=models.CASCADE)
	s_name=models.CharField(max_length=30, default='')
	created_at=models.DateTimeField(default=timezone.now)
	updated_at=models.DateTimeField(default=timezone.now)


class product_data(models.Model):
	p_id=models.AutoField
	s_id=models.ForeignKey(sub_category_data, on_delete=models.CASCADE)
	p_name=models.TextField(max_length=20, default='')
	p_price=models.FloatField(default=0)   #confusion 
	p_desc=models.CharField(max_length=100, default='')
	p_image=models.ImageField()
	created_at=models.DateTimeField(default=timezone.now)
	updated_at=models.DateTimeField(default=timezone.now)


class gallery_data(models.Model):
	image_id=models.AutoField
	p_id=models.ForeignKey(product_data, on_delete=models.CASCADE)
	p_image=models.ImageField()
	created_at=models.DateTimeField(default=timezone.now)
	updated_at=models.DateTimeField(default=timezone.now)


class order_data(models.Model):
	o_id=models.AutoField
	c_id=models.ForeignKey(customer_data, on_delete=models.CASCADE)
	o_date=models.DateField()
	o_amount=models.FloatField(default='')
	o_address=models.CharField(max_length=100, default='')
	created_at=models.DateTimeField(default=timezone.now)
	updated_at=models.DateTimeField(default=timezone.now)

class order_item_data(models.Model):
	orderitem_id=models.AutoField
	o_id=models.ForeignKey(order_data, on_delete=models.CASCADE)
	p_id=models.ForeignKey(product_data, on_delete=models.CASCADE)
	qty=models.IntegerField(default='')
	amount=models.FloatField(default='')
	created_at=models.DateTimeField(default=timezone.now)
	updated_at=models.DateTimeField(default=timezone.now)



class payment_data(models.Model):
	pay_id=models.AutoField
	o_id=models.OneToOneField(order_data, on_delete=models.CASCADE, primary_key=True)
	pay_date=models.DateField()
	pay_status=models.TextField(max_length=15, default='')
	pay_mode=models.TextField(max_length=10, default='')
	created_at=models.DateTimeField(default=timezone.now)
	updated_at=models.DateTimeField(default=timezone.now)


class contact_us_data(models.Model):
	id=models.AutoField
	name=models.TextField(max_length=20, default='')
	email=models.EmailField(max_length=20, default='')
	con_no=models.IntegerField(default=0)
	msg = models.TextField()
	created_at=models.DateTimeField(default=timezone.now)
	updated_at=models.DateTimeField(default=timezone.now)


class review_data(models.Model):
	r_id=models.AutoField
	p_id=models.ForeignKey(product_data, on_delete=models.CASCADE)
	c_id=models.ForeignKey(customer_data, on_delete=models.CASCADE)
	rating=models.IntegerField(default='') 
	review=models.CharField(max_length=1000, default='')
	created_at=models.DateTimeField(default=timezone.now)
	updated_at=models.DateTimeField(default=timezone.now)