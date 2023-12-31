from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .forms import RegistrationForm, UserEditForm
from .token import account_activation_token
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core.mail import send_mail

# Create your views here.

@login_required
def profile(request):
	return render(request, 'accounts/profile.html', {'section':'profile'})

@login_required
def profile_detail(request):
	username = request.user.username
	profile = User.objects.get(username=username)
	context = {
		'profile': profile
	}
	template = 'accounts/profile_detail.html' 
	return render(request, template, context)

def accounts_register(request):
	if request.method == 'POST':
		registerForm = RegistrationForm(request.POST)
		if registerForm.is_valid():
			user = registerForm.save(commit=False)
			user.set_password(registerForm.cleaned_data['password'])
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			subject = 'Activate your Account'

			message = render_to_string('registration/account_activation_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user),
			})
			to_email = registerForm.cleaned_data['email']
			send_mail(subject, message, 'gobblegobble035@gmail.com', [to_email])
			print('email sent')  
			return HttpResponse('Registered succesfully and activation link sent to your email. Please note that your username and password will not work until you have verified your email.' )


	else:
		registerForm = RegistrationForm()
	return render(request, 'registration/register.html', {'form':registerForm})

def activate(request, uidb64, token):
	try:
		uid = force_str(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		return redirect('login')
	else:
		return render(request, 'registration/activation_invalid.html')

@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		if user_form.is_valid():
			user_form.save()
			print('nice its saved')
	else:
		user_form = UserEditForm(instance=request.user)
		print('nope not saved')
	return render(request, 'accounts/update.html', {'user_form':user_form})

@login_required
def delete_user(request):

	if request.method == 'POST':
		user = User.objects.get(username=request.user)
		user.is_active = False
		user.save()
		return redirect('accounts:login')

	return render(request, 'accounts/delete.html')