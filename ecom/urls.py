"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from product.views import show_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('products/',show_product,name='index'),
    path('about_us/',views.about_us,name='about-us'),
    path('contact_us/',views.contact_us,name='contact-us'),
    path('product/',include('product.urls')),
    path('account/',include('account.urls')),
    path('cart/',include('cart.urls')),  
    # path('form/',views.form,name='form'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
