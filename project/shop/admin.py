

# Register your models here.
from django.contrib import admin
from .models import Category, Product,TypeCategory,Compound


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(TypeCategory)
admin.site.register(Compound)