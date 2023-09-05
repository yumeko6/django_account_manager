from django.db.models import QuerySet
from django.core.paginator import Paginator


def pagination(request, data: QuerySet):
    """
    Функция принимает на вход запрос и кверисет, возрвщает объект пагинации
    :param request: http-запрос
    :param data: django queryset
    :return: объект пагинации
    """
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def get_context(model: str, title: str):
    """
    Функция принимает на вход строковое название модели и необходимый тайтл,
    возвращает подготовленный context для передачи в html
    :param model: строковое название модели
    :param title: тайтл для html
    :return: context
    """

    descriptions = {
        'employees': {'header': 'сотрудников', 'text': 'сотрудника'},
        'resources': {'header': 'ресурсов', 'text': 'ресурса'},
        'accounts': {'header': 'аккаунтов', 'text': 'аккаунта'}
    }
    titles = {
        'employees': {
            'info': 'Информация о сотруднике',
            'employees': 'Сотрудники',
            'new': 'Новый сотрудник',
            'edit': 'Редактирование сотрудника',
            'search': 'Поиск сотрудников'
        },
        'resources': {
            'info': 'Информация о ресурсе',
            'resources': 'Ресурсы',
            'new': 'Новый ресурс',
            'edit': 'Редактирование ресурса',
            'search': 'Поиск ресурсов'
        },
        'accounts': {
            'info': 'Информация об аккаунте',
            'accounts': 'Аккаунты',
            'new': 'Новый аккаунт',
            'edit': 'Редактирование аккаунта',
            'search': 'Поиск аккаунтов'
        },
    }

    context = {
        'model': model,
        'title': titles[model][title],
        'search_description': descriptions[model]['header'],
        'search_description_text': descriptions[model]['text']
    }
    return context
