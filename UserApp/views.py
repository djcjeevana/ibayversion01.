from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

#from orders.views import user_orders

from .forms import RegistrationForm
from .models import UserBase
from .tokens import account_activation_token

@login_required
def dashboard(request):
    #orders = user_orders(request)
    return render(request,
                  'account/user/dashboard.html')

def account_register(request):
    
    if request.user.is_authenticated: # to check user is register or not
        return redirect('account:dashboard')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST) # To Rejester the user using post method me are taking data from the browser
        if registerForm.is_valid():#chek all the email password etc. are enderd correcctly . for that we use validation method.
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False # still user need make inactive. becaseu we need to check about him. becasue email activation is requered
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('account/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message) # in here you can add more informatino to your email. this your email body and content
            return HttpResponse('registered succesfully and activation sent')
    else:
        registerForm = RegistrationForm() # if he is new youser we redirect him to Registraion form
    return render(request, 'account/registration/register.html', {'form': registerForm})


def account_activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registration/activation_invalid.html')
