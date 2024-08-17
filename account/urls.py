from django.urls import path
from . import views
from django.views.generic import TemplateView



urlpatterns = [
    # path('login/',views.LoginView.as_view(),name='login'),
    # path('register/',TemplateView.as_view(template_name = 'account/choice.html'),name='register'),
    path('register/choice/<str:request_for>/',views.choice,name='register'),
    path('login/choice/<str:request_for>/',views.choice,name='login'),
    path('register/<str:user_type>/', views.register_user, name='register_user'),
    path('login/<str:user_type>/', views.LoginView.as_view(), name='login_user'),
    path('reset_password/',views.ResetPassword.as_view(),name='reset_password'),
    # path('register/supplier',views.register_supplier,name='register-supplier'),
    # path('register/customer',views.register_customer,name='register-customer'),
    # path('register/',views.register_user,name='register'),
    path('logout/',views.logout_user,name='logout'),
    path('verify_otp/',views.verify_otp,name='verify_otp'),
    path('change_password/',views.change_password,name='change_password'),
]