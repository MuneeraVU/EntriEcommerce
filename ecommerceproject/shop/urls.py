from django.urls import path, include
from shop import admin, views

urlpatterns = [

    path('', views.allproducts, name='allproducts'),
    path('payment/', views.payment, name='payment'),
    path('shipping/', views.ShippingAddress, name='shipping'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('<slug:slug_c>/', views.allproducts, name='product_by_category'),
    path('<slug:slug_c>/<slug_p>/', views.pro_det, name='product_catdetail'),


]
