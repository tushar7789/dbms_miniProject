from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from store.models.products import Product
from store.models.order import Order
from store.models.customer import Customer
from store.models.shipper import Shipping_Route
from datetime import datetime, timedelta


class CheckOut(View):
    def get(self, request):
        return render(request, 'cart.html') 
    
    def post(self, request):
        address = request.POST.get('address')
        print("address=",address)
        phone = request.POST.get('phone')
        from_city = request.POST.get('from_city')
        cart = request.session.get('cart')
        print('cart',cart)
        customer = request.session.get('customer')
        print('cust in sheck out',customer)
        products = Product.get_products_by_id(list(cart.keys()))     
        print("producTTTTT", products)  

        if not customer:
            msg = 'Login to Order'
            return_url = request.META['PATH_INFO']
            return render(request, 'login.html', {'msg':msg, 'return_url':return_url})
        else:
            arrival_date = self.get_arrival_date(address, from_city) 
            for product in products:
                order = Order(Customer = Customer(id = customer),
                          Product = product,
                          Quantity = cart.get(str(product.id)),
                          Price = product.Price,
                          Phone = phone,
                          Address = address,
                          Arrival_Date= arrival_date,)
                order.place_order()

            request.session['cart'] = {}
            return redirect('cart')

    def get_arrival_date(self, address, from_city):
        day = Shipping_Route.get_days(from_city, address)

        d = (datetime.now() + timedelta(days=day) )
        return d