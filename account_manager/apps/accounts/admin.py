from django.contrib import admin

from .models import Account


class AccountAdmin(admin.ModelAdmin):
	fields = [
		'name', 'user',	'login_method',
		'account_type',	'role', 'note', 'author'
	]
	list_display = [
		'id', 'name', 'user',
		'login_method',	'account_type',	'role',
		'pub_date',	'change_date', 'note'
	]
	search_fields = [
		'name__title', 'user__firstname', 'user__lastname'
	]


admin.site.register(Account, AccountAdmin)
