from django.shortcuts import render, redirect
from store.models.products import Product
from store.models.categories import Category
from django.views import View

class Index(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
        context = {'products':products, 'categories':categories}

        print('You are : ', request.session.get('customer'))
        return render(request, 'index.html', context, )

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        categoryID = request.POST.get('category') 
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else: 
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print("cart",request.session['cart'])
               
        return redirect('homepage')
        
        


    
