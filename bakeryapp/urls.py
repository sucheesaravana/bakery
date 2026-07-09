from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),

    path('cakes/', views.cake, name='cake'),
    path('pastries/', views.pastries, name='pastries'),
    path('sweets/', views.sweets, name='sweets'),
    path('checkout/', views.checkout, name='checkout'),

    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("payment/", views.payment, name="payment"),
    path('addtocard/', views.addtocard, name='addtocard'),
    path("wishlist/", views.wishlist, name="wishlist"),
]
