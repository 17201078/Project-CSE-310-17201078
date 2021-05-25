from django.contrib import admin
from django.urls import path
from .views.home import Index
from .views import home
from .views.login import Login, logout
from .views.signup import Signup
from .views.cart import Cart
from .views.checkout import Checkout
from .views.orders import OrderView
from .middlewares.auth import auth_middleware
from .views.about import About
from .views.contact import Contactview
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home.Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', Checkout.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('about', About.as_view(), name='about'),
    path('contact', Contactview.as_view(), name='contact'),
]

urlpatterns = urlpatterns+ static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
urlpatterns = urlpatterns+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()