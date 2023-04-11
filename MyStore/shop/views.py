from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import ListView, RedirectView, CreateView

from .forms import UserRegisterForm, LoginForm, CartProductForm
from .models import Product, Team, AboutUs, Blog, Promotion, Insta, Gallery, Order, OrderItems


# Create your views here.
class ProductListView(ListView):
    template_name = 'shop/shop.html'
    model1 = Product
    model2 = Insta
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
        'product_list': self.model1.objects.all(),
        'insta_list': self.model2.objects.all()
        }
        return render(request, self.template_name, self.context)


def contactus(request):
    return render(request, 'shop/contact_us/contact-us.html')


def checkout(request):
    return render(request, 'shop/checkout/checkout.html')


def wishlist(request):
    return render(request, 'shop/wishlist/wishlist.html')


def shop_detail(request):
    return render(request, 'shop/shop_detail/shop-detail.html')


def my_account(request):
    return render(request, 'shop/my-account/my-account.html')


class TeamListView(ListView):
    template_name = 'shop/about.html'
    model1 = Team
    model2 = AboutUs
    model3 = Insta
    paginate_by = 6
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
            'teams': self.model1.objects.all(),
            'aboutuss': self.model2.objects.all(),
            'insta_list': self.model3.objects.all()
        }
        return render(request, self.template_name, self.context)


class HomeListView(ListView):
    template_name = 'shop/home_page/home_page.html'
    model1 = Blog
    model2 = Promotion
    model3 = Insta
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
            'blog_list': self.model1.objects.all(),
            'promotion_list': self.model2.objects.all(),
            'insta_list': self.model3.objects.all()
        }
        return render(request, self.template_name, self.context)


class GalleryListView(ListView):
    template_name = 'shop/gallery/gallery.html'
    model1 = Gallery
    model2 = Insta
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
            'gallery_list': self.model1.objects.all(),
            'insta_list': self.model2.objects.all()
        }
        return render(request,self.template_name, self.context)


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'shop/registration/registration.html'
    success_url = reverse_lazy('my_account')


class SignInView(LoginView):
    template_name = 'shop/registration/login.html'
    form_class = LoginForm


class CartListView(LoginRequiredMixin, ListView):
    model = OrderItems
    template_name = 'shop/cart/cart.html'
    context_object_name = 'order_items_list'

    def get_queryset(self):
        return self.model.objects.filter(order__is_paid=False)

# @require_POST
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     form = CartProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product,
#                  quantity=cd['quantity'],
#                  update_quantity=cd['update'])
#
#     return redirect('cart_detail')
#
#
# def cart_remove(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     cart.remove(product)
#     return redirect('cart_detail')
#
#
# def cart_detail(request):
#     cart = Cart(request)
#     for item in cart:
#         item['update_quantity_form'] = CartProductForm(initial={
#             'quantity': item['quantity'],
#             'update': True
#         })
#     return render(request, 'shop/cart.html')
