from django import forms

from .models import Account
from ..employees.models import Employee


class AccountForm(forms.ModelForm):
	user = forms.ModelChoiceField(queryset=Employee.objects.all())
	note = forms.CharField(required=False)

	class Meta:
		model = Account
		exclude = ('author', 'pub_date', 'change_date',)
		labels = {
			'name': 'Название ресурса',
			'user': 'Сотрудник',
			'login_method': 'Способ входа',
			'account_type': 'Тип аккаунта',
			'role': 'Роль в системе',
			'note': 'Примечание'
		}
