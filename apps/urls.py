from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.views import CategoryListView, CustomLoginView, ProductListView, OrderListView, LikedProductsView, \
    ProfileFormView, OverallProfileView, ProductDetailView

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(template_name='apps/home_page.html'), name='logout'),
    path('product', ProductListView.as_view(), name='products'),
    path('orders', OrderListView.as_view(), name='orders'),
    path('liked', LikedProductsView.as_view(), name='liked'),
    path('overall', OverallProfileView.as_view(), name='overall'),
    path('profile', ProfileFormView.as_view(), name='profile'),
    path('detail/<str:slug>', ProductDetailView.as_view(), name='detail'),
]
