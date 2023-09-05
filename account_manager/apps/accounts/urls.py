from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
	path(
		'accounts/<int:employee_id>/create/',
		views.create_account,
		name='create_accounts'
	),
	path(
		'accounts/all',
		views.show_all_accounts,
		name='show_all_accounts'
	),
	path(
		'accounts/<int:employee_id>/',
		views.show_accounts,
		name='show_accounts'
	),
	path(
		'accounts/show/<int:account_id>/',
		views.show_account,
		name='show_account'
	),
	path(
		'accounts/show/<int:account_id>/edit',
		views.edit_account,
		name='edit_account'
	)
]
