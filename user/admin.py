from django.contrib import admin
from .models import category_data,area_data,sub_category_data,product_data


# Register your models here.
admin.site.register(category_data)
admin.site.register(area_data)
admin.site.register(sub_category_data)
admin.site.register(product_data)
