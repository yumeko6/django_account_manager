from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .forms import ResourceForm
from .models import Resource
from ..utils.utils import pagination, get_context


@login_required
def show_resource(request, resource_id):
	context = get_context('resources', 'info')
	context.update(
		{
			'resource': get_object_or_404(Resource, pk=resource_id),
			'data': Resource.objects.all()
		}
	)
	return render(request, 'resources/resource.html', context)


@login_required
def show_resources(request):
	resources = Resource.objects.all()
	page_obj = pagination(request, resources)
	context = get_context('resources', 'resources')
	context.update(
		{
			'page_obj': page_obj,
			'data': resources
		}
	)
	return render(request, 'resources/show_resources.html', context)


@login_required
def create_resource(request):
	form = ResourceForm(request.POST or None)
	if form.is_valid():
		resource = form.save(commit=False)
		resource.author = request.user
		resource.save()
		return redirect('resources:show_resources')
	context = get_context('resources', 'new')
	context.update(
		{
			'data': Resource.objects.all(),
			'form': form,
		}
	)
	return render(request, 'resources/create_resource.html', context)


@login_required
def edit_resource(request, resource_id):
	is_edit = True
	resource = get_object_or_404(Resource, pk=resource_id)
	form = ResourceForm(request.POST or None, instance=resource)
	if form.is_valid():
		form.save()
		return redirect('resources:show_resources')
	context = get_context('resources', 'edit')
	context.update(
		{
			'resource': resource,
			'data': Resource.objects.all(),
			'form': form,
			'is_edit': is_edit,
		}
	)
	return render(request, 'resources/create_resource.html', context)


class ResourceSearchView(ListView):
	model = Resource
	paginate_by = 10
	template_name = 'resource_list.html'
	context_object_name = 'founded_resources'

	def get_queryset(self):
		query = self.request.GET.get('query')
		object_list = Resource.objects.filter(
			Q(title__icontains=query.capitalize()) |
			Q(title__icontains=query) |
			Q(url__icontains=query)
		)
		return object_list

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		get_con = get_context('resources', 'search')
		context['title'] = get_con['title']
		context['search_description'] = get_con['search_description']
		context['data'] = Resource.objects.all()
		context['model'] = get_con['model']
		context['searched'] = True
		return context

