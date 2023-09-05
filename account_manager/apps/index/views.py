from django.shortcuts import render


def index(request):
    context = {
        'title': 'TeeVeeAcc',
    }
    return render(request, 'index/index.html', context)
