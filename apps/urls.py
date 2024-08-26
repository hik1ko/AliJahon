from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.views import CategoryListView, CustomLoginView, ProductListView, OrderListView, WishListView, \
    ProfileFormView, OverallProfileView, ProductDetailView, LikeProductView, ForMpttListView, MarketListView, \
    StatsView, PaymentView

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
    path('cat', ForMpttListView.as_view(), name='category_mptt'),
]

urlpatterns += [
    # path('stream/form', StreamFormView.as_view(), name='stream-form'),
    # path('stream/list', StreamListView.as_view(), name='stream-list'),
    # path('stream/details/<int:pk>', StreamDetailsView.as_view(), name='stream-details'),
]

urlpatterns += [
    path('admin_page/market', MarketListView.as_view(), name='market'),
    path('admin_page/stats', StatsView.as_view(), name='stats'),
    path('admin_page/payment', PaymentView.as_view(), name='payment'),
]
