from django.db import models

from apps.employees.models import Employee
from apps.resources.models import Resource
from apps.users.models import CustomUser


class Account(models.Model):
	LOGINPASS = 'LP'
	ESIGN = 'ES'
	USER = 'US'
	ADMIN = 'AD'
	PERSONAL = 'PN'
	GENERAL = 'GN'

	LOGIN_METHODS = [
		(LOGINPASS, 'Логин/пароль'),
		(ESIGN, 'ЭЦП'),
	]

	ROLES = [
		(USER, 'Пользователь'),
		(ADMIN, 'Администратор')
	]

	ACCOUNT_TYPE = [
		(PERSONAL, 'Персональный'),
		(GENERAL, 'Общий')
	]

	name = models.ForeignKey(
		Resource,
		on_delete=models.PROTECT
	)
	user = models.ForeignKey(
		Employee,
		on_delete=models.PROTECT
	)
	login_method = models.CharField(
		max_length=2,
		choices=LOGIN_METHODS,
		default=LOGINPASS,
		verbose_name='Способ входа'
	)
	account_type = models.CharField(
		max_length=2,
		choices=ACCOUNT_TYPE,
		default=PERSONAL,
		verbose_name='Тип аккаунта'
	)
	role = models.CharField(
		max_length=2,
		choices=ROLES,
		default=USER,
		verbose_name='Роль в системе'
	)
	author = models.ForeignKey(
		CustomUser,
		on_delete=models.DO_NOTHING,
		related_name='accounts',
		verbose_name='Автор'
	)
	pub_date = models.DateTimeField(
		auto_now_add=True,
		verbose_name='Дата создания'
	)
	change_date = models.DateTimeField(
		auto_now=True,
		verbose_name='Дата изменения'
	)
	note = models.TextField(
		blank=True,
		verbose_name='Примечание'
	)

	class Meta:
		ordering = ['pub_date']
		verbose_name = 'Аккаунт'
		verbose_name_plural = 'Аккаунты'
		constraints = [
			models.UniqueConstraint(fields=['name', 'user'], name='account')
		]

	def __str__(self):
		return self.name.title
