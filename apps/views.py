import re

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, FormView, DetailView

from apps.forms import ProfileForm
from apps.models import Category, Product, User


class CategoryListView(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/home_page.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['categories'] = Category.objects.all()
        return data


class CustomLoginView(TemplateView):
    template_name = 'apps/auth/login.html'

    def post(self, request, *args, **kwargs):
        phone_number = re.sub(r'\D', '', request.POST.get('phone_number'))
        user = User.objects.filter(phone_number=phone_number).first()
        if not user:
            user = User.objects.create_user(phone_number=phone_number, password=request.POST['password'])
            login(request, user)
            return redirect('home')
        else:
            user = authenticate(request, username=user.phone_number, password=request.POST['password'])
            if user:
                login(request, user)
                return redirect('home')

            else:
                context = {
                    "messages_error": ["Invalid password"]
                }
                return render(request, template_name='apps/auth/login.html', context=context)


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/products_list.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        slug = self.request.GET.get("category")
        query = super().get_queryset()
        if slug != 'all':
            query = query.filter(category__slug=slug)
        return query

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['categories'] = Category.objects.all()
        return data


class ProductDetailView(DetailView):
    model = Product
    template_name = 'apps/product-details.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'


class ProfileFormView(FormView):
    form_class = ProfileForm
    template_name = 'apps/auth/profile_details.html'

    def form_valid(self, form):
        data = form.save(commit=False)
        print(data)

    def form_invalid(self, form):
        data = form.errors
        print(data)


class OverallProfileView(TemplateView):
    template_name = 'apps/auth/overall_profile.html'


class LikedProductsView(ListView):
    template_name = 'apps/liked_products_list.html'


class OrderListView(ListView):
    template_name = 'apps/orders.html'



