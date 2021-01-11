from django.views import View
from django.shortcuts import render, redirect
from store.models.products import Product
from store.models.shipper import Shipping_Route

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart'))
        products = Product.get_products_by_id(ids)
        From = Shipping_Route.objects.values('From').distinct()
        To = Shipping_Route.objects.values('To').distinct()
        return render(request, 'cart.html', {'products':products, 'From':From, 'To':To}) 