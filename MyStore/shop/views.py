from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, RedirectView, CreateView, DetailView
from slugify import slugify

from .forms import UserRegisterForm, LoginForm, CartProductForm, ContactUsForm, UserUpdateForm
from .models import Product, Team, AboutUs, Blog, Promotion, Insta, Gallery, Order, OrderItems, Message, Profile


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


class ContactUsListView(ListView):
    model = Message
    template_name = 'shop/contact_us/contact-us.html'
    http_method_names = ('get', 'post')
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ContactUsListView, self).get_context_data()
        context['contact_us'] = ContactUsForm()
        return context

    def post(self, request: HttpRequest):
        data = request.POST.dict()
        data.update(slug=slugify(request.POST.get('user')))
        form = ContactUsForm(data)
        if form.is_valid():
            form.save()
        return self.get(request=request)


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
        return render(request, self.template_name, self.context)


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
        return self.model.objects.filter(
            Q(order__is_paid=False) & Q(order__user=self.request.user)
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CartListView, self).get_context_data()
        context['total_amount'] = 0
        context['cart_amount'] = len(context[self.context_object_name])
        for product in context[self.context_object_name]:
            context['total_amount'] += product.product.price
        return context


class ProfilePageView(ListView):
    model = Profile
    template_name = 'shop/my-account/profile.html'
    context_object_name = 'my_profile'


