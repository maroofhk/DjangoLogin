from django.shortcuts import render, HttpResponseRedirect

from .forms import IOTUserForm, IOTUserProfileForm
from IOT_Users.models import IOTUser


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required

from django.contrib.auth.models import Permission


@login_required
def home(request):
	print('-------------------responce-------------')
	print('first name: ', request.POST.get('first_name'))
	print('last name: ', request.POST.get('last_name'))
	print('email: ', request.POST.get('email'))
	print('-------------------responce-------------')
	form = IOTUserForm(request.POST or None)
	if form.is_valid():
		new_user, created = User.objects.get_or_create(**form.cleaned_data)
		if created:
			new_user.is_active = False
			new_user.save()
			#user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
			#login(request, new_user) 
			return HttpResponseRedirect('profile/')

	context = {'form': form}
	template = 'IOT_Users/home.html'
	return render(request, template, context)

# def can_add_user_in_iot(User):
# 	return User.is_authenticated() and User.has_perm(IOT_Users.add_iotuser)

#@user_passes_test(can_add_user_in_iot)
@login_required
@permission_required('IOT_Users.add_iotuser')
def profile(request):
	form = IOTUserProfileForm(request.POST or None)
	if form.is_valid():
		new_user, created = IOTUser.objects.get_or_create(**form.cleaned_data)
		if created:
			new_user.save()
			return HttpResponseRedirect('/home/')

	context = {'form': form}
	template = 'IOT_Users/profile.html'
	return render(request, template, context)

