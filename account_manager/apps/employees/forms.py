from django import forms

from .models import Employee


class EmployeeForm(forms.ModelForm):

	class Meta:
		model = Employee
		exclude = ('is_fired', 'author', 'pub_date', 'change_date',)
		labels = {
			'lastname': 'Фамилия',
			'firstname': 'Имя',
			'middlename': 'Отчество',
			'position': 'Должность',
			'email': 'Адрес корпоративной почты',
			'phone': 'Номер корпоративного телефона',
			'extension': 'Короткий номер абонента'
		}
