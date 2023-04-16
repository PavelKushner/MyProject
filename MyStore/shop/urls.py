from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import ProductListView, TeamListView, HomeListView, GalleryListView, checkout, my_account, ContactUsListView
from .views import RegisterView, SignInView, wishlist, shop_detail, CartListView, ProfilePageView

urlpatterns = [
    path('', ProductListView.as_view(), name='shop_product_list'),
    path('home/', HomeListView.as_view(), name='home_page'),
    path('team/', TeamListView.as_view(), name='about_us'),
    path('gallery/', GalleryListView.as_view(), name='gallery'),
    path('contactus/', ContactUsListView.as_view(), name='contact_us'),
    path('checkout/', checkout, name='checkout'),
    path('my_account/', my_account, name='my_account'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('login/', SignInView.as_view(), name='log_in'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('wishlist/', wishlist, name='wishlist'),
    path('shop_detail/', shop_detail, name='shop_detail'),
    path('cart/', CartListView.as_view(), name='cart'),
    path('user_profile/', ProfilePageView.as_view(), name='user_profile')
]
