from django.db import models

from apps.users.models import CustomUser


class Resource(models.Model):
	title = models.CharField(
		max_length=100,
		unique=True,
		verbose_name='Название'
	)
	author = models.ForeignKey(
		CustomUser,
		on_delete=models.DO_NOTHING,
		related_name='resources',
		verbose_name='Автор'
	)
	url = models.URLField(
		verbose_name='Ссылка'
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
		null=True,
		verbose_name='Примечание'
	)

	class Meta:
		ordering = ['pub_date']
		verbose_name = 'Ресурс'
		verbose_name_plural = 'Ресурсы'

	def __str__(self):
		return self.title
