from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='Register'),
    path('forgotpassword/', views.forgotpassword, name='ForgotPassword'),
    path('resendverification', views.resendverification, name='Resendverification'),
]
