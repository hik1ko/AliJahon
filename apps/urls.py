from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.views import CategoryListView, CustomLoginView, ProductListView, OrderListView, WishListView, \
    ProfileFormView, OverallProfileView, ProductDetailView, LikeProductView

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(template_name='apps/home_page.html'), name='logout'),
    path('product', ProductListView.as_view(), name='products'),
    path('orders', OrderListView.as_view(), name='orders'),
    path('wishlist', WishListView.as_view(), name='wishlist'),
    path('product/liked/<str:slug>', LikeProductView.as_view(), name='liked'),
    path('product/order_list', OrderListView.as_view(), name='order_list'),
    path('overall', OverallProfileView.as_view(), name='overall'),
    path('profile', ProfileFormView.as_view(), name='profile'),
    path('detail/<str:slug>', ProductDetailView.as_view(), name='detail'),
]
