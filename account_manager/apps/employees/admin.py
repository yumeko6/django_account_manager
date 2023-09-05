from django.contrib import admin

from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
	fields = [
		'lastname', 'firstname',
		'middlename', 'position',
		'email', 'phone',
		'extension', 'author',
		'is_fired'
	]
	list_display = [
		'id', 'lastname',
		'firstname', 'middlename',
		'position',	'email',
		'phone', 'extension',
		'author', 'pub_date',
		'change_date', 'is_fired'
	]
	search_fields = [
		'lastname', 'firstname',
		'email', 'phone',
		'extension'
	]


admin.site.register(Employee, EmployeeAdmin)
