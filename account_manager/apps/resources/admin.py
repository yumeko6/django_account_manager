from django.contrib import admin

from .models import Resource


class ResourceAdmin(admin.ModelAdmin):
	fields = [
		'title', 'url',
		'note', 'author'
	]
	list_display = [
		'id', 'title',
		'author', 'url',
		'pub_date', 'change_date',
		'note'
	]
	search_fields = [
		'title', 'author',
		'pud_date'
	]


admin.site.register(Resource, ResourceAdmin)
