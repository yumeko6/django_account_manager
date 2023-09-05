from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from apps.accounts.forms import AccountForm
from apps.accounts.models import Account
from apps.employees.models import Employee
from apps.utils.utils import pagination, get_context


@login_required
def create_account(request, employee_id):
	employee = get_object_or_404(Employee, pk=employee_id)
	form = AccountForm(
		request.POST or None,
		initial={'user': employee}
	)
	if form.is_valid():
		account = form.save(commit=False)
		account.author = request.user
		account.save()
		return redirect('employees:show_employees')
	context = get_context('accounts', 'new')
	context.update(
		{
			'data': Account.objects.all(),
			'employee': employee,
			'form': form,
		}
	)
	return render(request, 'accounts/create_accounts.html', context)


@login_required
def show_accounts(request, employee_id):
	accounts = Account.objects.filter(user=employee_id).all()
	page_obj = pagination(request, accounts)
	context = get_context('accounts', 'accounts')
	context.update(
		{
			'page_obj': page_obj,
			'data': accounts
		}
	)
	return render(request, 'accounts/show_accounts.html', context)


@login_required
def show_account(request, account_id):
	context = get_context('accounts', 'info')
	context.update(
		{
			'account': get_object_or_404(Account, pk=account_id),
			'data': Account.objects.all()
		}
	)
	return render(request, 'accounts/account.html', context)


@login_required
def show_all_accounts(request):
	accounts = Account.objects.all()
	page_obj = pagination(request, accounts)
	context = get_context('accounts', 'accounts')
	context.update(
		{
			'page_obj': page_obj,
			'data': accounts
		}
	)
	return render(request, 'accounts/show_accounts.html', context)


@login_required
def edit_account(request, account_id):
	is_edit = True
	account = get_object_or_404(Account, pk=account_id)
	form = AccountForm(request.POST or None, instance=account)
	if form.is_valid():
		form.save()
		return redirect('accounts:show_all_accounts')
	context = get_context('accounts', 'edit')
	context.update(
		{
			'account': account,
			'data': Account.objects.all(),
			'form': form,
			'is_edit': is_edit
		}
	)
	return render(request, 'accounts/create_accounts.html', context)
