from django.urls import path
from . import views
from .views import EmployeeSearchView

app_name = 'employees'

urlpatterns = [
	path(
		'employees/',
		views.show_employees,
		name='show_employees'),
	path(
		'employees/create/',
		views.create_employee,
		name='create_employees'
	),
	path(
		'employees/show/<int:employee_id>/',
		views.show_employee,
		name='show_employee'
	),
	path(
		'employees/show/<int:employee_id>/edit/',
		views.edit_employee,
		name='edit_employees'
	),
	path(
		'employees/search/',
		EmployeeSearchView.as_view(),
		name='search_results',
	)
]
