from django.urls import path
from .views import home, signup, login, cart, check_out, orders

urlpatterns = [
    path('', home.Index.as_view(), name="homepage"),
    path('signup', signup.Signup.as_view(), name="signup"),
    path('login', login.Login.as_view(), name="login"),
    path('logout', login.logout, name="logout"),
    path('cart', cart.Cart.as_view(), name="cart"),
    path('check_out',check_out.CheckOut.as_view(),name="checkout"),
    path('order',orders.Orders.as_view(),name="order"),
    #path('cart/login', login.cart_login, name="cart_login")
]