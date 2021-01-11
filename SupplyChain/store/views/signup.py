from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        email = postData.get('email')
        password = postData.get('password')

        data = {
                'first_name':first_name,
                'last_name':last_name,
                'email':email,
                'password':password,
            }

        errors = self.validate(request,data)

        if errors['error1'] != "" or errors['error2'] != "" or errors['error3'] != "" or errors['error4'] != "":
            print(data)
            return render(request, 'signup.html', {'errors':errors, 'data':data})
        
        customer = Customer(FirstName = first_name,
                            LastName = last_name,
                            E_mail = email,
                            Password= password,
                            )

        if customer.account_exists():
            msg = "Account with identical Email already exists"
            return render(request, 'signup.html', {'data':data,'msg':msg})
            
        customer.Password = make_password(customer.Password)
        customer.register()
        print("customer registered")

        return redirect('homepage')
    
    def validate(self, request, data):
        errors = {
            'error1':'',
            'error2':'',
            'error3':'',
            'error4':'',
        }
        #validation
        if not data['first_name']:
            errors['error1'] = "first name required"
        if len(data['first_name']) < 5 and len(data['first_name']) > 0:
            errors['error1'] = "first name must be 5 char long"
        if not data['last_name']:
            errors['error2'] = "last name required"
        if len(data['last_name']) < 5 and len(data['last_name']) > 0:
            errors['error2'] = "last name must be 5 char long"
        if not data['email']:
            errors['error3'] = "email required"
        if not data['password']:
            errors['error4'] = "password required"
        if len(data['password']) < 5 and len(data['password']) > 0:
            errors['error4'] = "password must be 5 char long"

        return errors
        
    