from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'text': 'Последнее обновление на сайте'
    }
    template = 'posts/index.html'
    return render(request, template, context)


def group_list(request):
    title = f'Здесь будет информация о группе проукта Yatube'
    context = {
        'title': title,
        'text': 'Лев Толстой – зеркало русской революции.'
    }
    template = 'posts/group_list.html'
    return render(request, template, context)
