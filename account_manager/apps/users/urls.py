from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView
from django.urls import path


app_name = 'users'

urlpatterns = [
	path(
		'logout/',
		LogoutView.as_view(template_name='users/newlogin.html'),
		name='logout'
	),
	path(
		'login/',
		LoginView.as_view(template_name='users/newlogin.html'),
		name='login'
	),
	path(
		'password_change/',
		PasswordChangeView.as_view(
			template_name='users/password_change_form.html'
		),
		name='password_change'
	),
	path(
		'password_change/done/',
		PasswordChangeView.as_view(
			template_name='users/password_change_done.html'
		),
		name='password_change_done'
	),
]
