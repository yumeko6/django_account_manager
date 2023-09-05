from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .forms import EmployeeForm
from .models import Employee
from ..utils.utils import pagination, get_context


@login_required
def show_employee(request, employee_id):
	context = get_context('employees', 'info')
	context.update(
		{
			'employee': get_object_or_404(Employee, pk=employee_id),
			'data': Employee.objects.all()
		}
	)
	return render(request, 'employees/employee.html', context)


@login_required
def show_employees(request):
	employees = Employee.objects.all()
	page_obj = pagination(request, employees)
	context = get_context('employees', 'employees')
	context.update(
		{
			'page_obj': page_obj,
			'data': employees
		}
	)
	return render(request, 'employees/show_employees.html', context)


@login_required
def create_employee(request):
	form = EmployeeForm(request.POST or None)
	if form.is_valid():
		employee = form.save(commit=False)
		employee.author = request.user
		employee.save()
		return redirect('employees:show_employees')
	context = get_context('employees', 'new')
	context.update(
		{
			'data': Employee.objects.all(),
			'form': form
		}
	)
	return render(request, 'employees/create_employees.html', context)


@login_required
def edit_employee(request, employee_id):
	is_edit = True
	employee = get_object_or_404(Employee, pk=employee_id)
	form = EmployeeForm(request.POST or None, instance=employee)
	if form.is_valid():
		form.save()
		return redirect('employees:show_employees')
	context = get_context('employees', 'edit')
	context.update(
		{
			'employee': employee,
			'data': Employee.objects.all(),
			'form': form,
			'is_edit': is_edit
		}
	)
	return render(request, 'employees/create_employees.html', context)


class EmployeeSearchView(ListView):
	model = Employee
	paginate_by = 10
	template_name = 'employee_list.html'
	context_object_name = 'founded_employees'

	def get_queryset(self):
		query = self.request.GET.get('query').split()
		if len(query) == 1:
			object_list = Employee.objects.filter(
				Q(lastname__icontains=query[0].capitalize()) |
				Q(firstname__icontains=query[0].capitalize())
			)
			return object_list
		elif len(query) == 2:
			object_list = Employee.objects.filter(
				Q(lastname__icontains=query[0].capitalize()) &
				Q(firstname__icontains=query[1].capitalize())
			)
			return object_list

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		get_con = get_context('employees', 'search')
		context['title'] = get_con['title']
		context['search_description'] = get_con['search_description']
		context['data'] = Employee.objects.all()
		context['model'] = get_con['model']
		context['searched'] = True
		return context
