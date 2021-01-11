from django.contrib import admin
from .models.products import Product
from .models.categories import Category
from .models.customer import Customer
from .models.order import Order
from .models.shipper import Shipping_Route

class AdminOrder(admin.ModelAdmin):
    list_display = ['Product', 'Customer', 'Quantity', 'Price', 'Order_Date', 'Arrival_Date']  

class AdminProduct(admin.ModelAdmin):
    list_display = ['Name', 'Manufacturer', 'Price', 'Image', 'Category'] 

class AdminCategory(admin.ModelAdmin):
    list_display = ['Name', ] 

class AdminCustomer(admin.ModelAdmin):
    list_display = ['FirstName', 'LastName', 'E_mail', 'Password']

class AdminShipping_Route(admin.ModelAdmin):
    list_display = ['From', 'To', 'Days']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)
admin.site.register(Shipping_Route, AdminShipping_Route)
