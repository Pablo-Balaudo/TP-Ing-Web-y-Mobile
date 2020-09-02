"""MyLittlePixel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from Usuarios import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Juego.urls')),
    path('foro/', include('Foro.urls')),
    path('galeria/', include('Galeria.urls')),
    path('miscelaneo/', include('Miscelaneo.urls')),
    path('register/', user_views.register, name='Register'),
    path('login/', auth_views.LoginView.as_view(template_name='Usuarios/Login.html'), name='Login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Usuarios/Logout.html'), name='Logout'),
    path('profile/', user_views.profile, name='Profile'),
    path('activate/<uidb64>/<token>/',user_views.activate, name='activate'),
    
    # Restablecer contraseña
    path('password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='Usuarios/password_reset.html'
        ),
        name='password_reset'),
    
    #Correo de restablecimiento de contraseña enviada
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='Usuarios/password_reset_done.html'
        ),
        name='password_reset_done'),
    
    #Confirmar restablecimiento de contraseña
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='Usuarios/password_reset_confirm.html'
        ),
        name='password_reset_confirm'),
    
    #Restablecimiento de contraseña hecha
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='Usuarios/password_reset_complete.html'
        ),
        name='password_reset_complete'),

    path('resendverification/', user_views.resendverification, name='ResendVerification'),
]
