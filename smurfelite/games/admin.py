from django.contrib import admin
from .models import Games, Category, Product
# Register your models here.
admin.site.register(Games)
admin.site.register(Category)
admin.site.register(Product)