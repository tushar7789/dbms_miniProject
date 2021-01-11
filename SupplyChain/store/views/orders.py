from django.views import View
from django.shortcuts import render, redirect
from store.models.order import Order
from store.models.customer import Customer
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
from datetime import datetime, date

class Orders(View):

    @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_customer_by_id(customer)

        for order in orders:
            print(date.today()," ",order.Arrival_Date)
            if date.today() == order.Arrival_Date:
                order.Status = True
                  
        return render(request, 'orders.html', {'orders':orders})
