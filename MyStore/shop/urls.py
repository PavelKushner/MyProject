from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import ProductListView, TeamListView, HomeListView, GalleryListView, contactus, checkout, my_account
from .views import RegisterView, SignInView
urlpatterns = [
    path('', ProductListView.as_view(), name='shop_product_list'),
    path('home/', HomeListView.as_view(), name='home_page'),
    path('team/', TeamListView.as_view(), name='about_us'),
    path('gallery/', GalleryListView.as_view(), name='gallery'),
    path('contactus', contactus, name='contact_us'),
    path('checkout', checkout, name='checkout'),
    path('my_account', my_account, name='my_account'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('login/', SignInView.as_view(), name='log_in'),
    path('logout/', LogoutView.as_view(), name='logout')
]
