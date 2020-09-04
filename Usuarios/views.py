from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#Para el registro
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .utils import generate_token
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            
            if User.objects.filter(email=email).exists():
                messages.add_message(request, messages.ERROR,'Correo electrónico en uso, elige otro.')
                return render(request,'Usuarios/Register.html',{'form': form},status=400)
            else:                
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                
                #link = reverse('activate', kwargs={'uidb64':uidb64,'token':token})
                current_site= str(get_current_site(request))
                mail_subject = 'Activa tu cuenta en MyLittlePixel'
                message = render_to_string('Usuarios/Activation.html',
                                   {
                                       'user': user,
                                       'domain': current_site,
                                       'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                       'token': generate_token.make_token(user)
                                   }
                                   )
                
                email_message = EmailMessage(
                    mail_subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email]
                )
                email_message.send(fail_silently=False)
                
                messages.success(request, f'Tu cuenta ha sido creada!')
                return redirect('/login')
    else:
        form = UserRegisterForm()

    # eliminamos el exceso de texto ayuda que se genera automaticamente
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    
    return render(request, 'Usuarios/Register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        print(uid)
        user = User.objects.get(pk=uid)
        print(user.username)
        
        user.is_active=True
        user.save()
        return render(request, 'Usuarios/Email_activation.html')
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        
    return render(request, 'Usuarios/Email_activation_failed.html')

def resendverification(request):
    return render(request, 'Usuarios/Resendverification.html')


@login_required
def profile(request):
    return render(request, 'Usuarios/Profile.html')
