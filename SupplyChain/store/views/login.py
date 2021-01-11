from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

class Login(View):

    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        return_url = request.POST.get('return_url')
        print('return_url',return_url)
        error_msg = ""
        if customer:
            flag = check_password(password, customer[0].Password)            #customer.Password)
            if flag:
                request.session['customer'] = customer[0].id
                if return_url:
                    return redirect('cart')
                else:
                    return redirect('homepage')
            else:
                error_msg = "Email/Password is Invalid !"
        else:
            error_msg = "Email/Password is Invalid !"
        return render(request, 'login.html', {'error':error_msg})
    
def logout(request):
    request.session.clear()
    return redirect('login')

