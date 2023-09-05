from django.db import models

from apps.users.models import CustomUser


class Employee(models.Model):
	lastname = models.CharField(
		max_length=20,
		verbose_name='Фамилия'
	)
	firstname = models.CharField(
		max_length=20,
		verbose_name='Имя'
	)
	middlename = models.CharField(
		max_length=20,
		verbose_name='Отчество'
	)
	position = models.CharField(
		max_length=200,
		verbose_name='Должность'
	)
	email = models.EmailField(
		verbose_name='Эл. почта'
	)
	phone = models.IntegerField(
		blank=True,
		null=True,
		verbose_name='Корпоративный телефон'
	)
	extension = models.IntegerField(
		blank=True,
		null=True,
		verbose_name='Короткий номер'
	)
	author = models.ForeignKey(
		CustomUser,
		on_delete=models.DO_NOTHING,
		related_name='employees',
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
	is_fired = models.BooleanField(
		default=False,
		blank=True,
		verbose_name='Уволен'
	)

	class Meta:
		ordering = ['lastname']
		verbose_name = 'Сотрудник'
		verbose_name_plural = 'Сотрудники'

	def __str__(self):
		return f'{self.lastname} {self.firstname}'
