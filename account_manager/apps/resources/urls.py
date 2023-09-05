from django.urls import path
from . import views
from .views import ResourceSearchView

app_name = 'resources'

urlpatterns = [
	path(
		'resources/',
		views.show_resources,
		name='show_resources'
	),
	path(
		'resources/create/',
		views.create_resource,
		name='create_resource'
	),
	path(
		'resources/show/<int:resource_id>/',
		views.show_resource,
		name='show_resource'
	),
	path(
		'resources/show/<int:resource_id>/edit/',
		views.edit_resource,
		name='edit_resource'
	),
	path(
		'resources/search/',
		ResourceSearchView.as_view(),
		name='search_results',
	)
]
