from django.contrib import admin

# Register your models here.
from app.models import Product


@admin.register(Product)
class PRoductAdmin(admin.ModelAdmin):
    pass