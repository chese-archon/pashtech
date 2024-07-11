from django.shortcuts import render

# Create your views here.
# Обработка https запросов и функции представления для страниц Главная & other

#def home(request):
#    return HttpResponse('<h1>Главная</h1>')

def audio(request):
    return HttpResponse('<h1>Аудио</h1>')

def video(request):
    return HttpResponse('<h1>Видео</h1>')

def afisha(request):
    return HttpResponse('<h1>Афиша</h1>')

def news(request):
    return HttpResponse('<h1>Новости</h1>')

#def bio(request):
#    return HttpResponse('<h1>Биография</h1>')

def contacts(request):
    return HttpResponse('<h1>Контакты</h1>')


posts = [
    {
        'author': 'Администратор',
        'title': 'Это первый пост',
        'content': 'Содержание первого поста.',
        'date_posted': '12 мая, 2022'
    },
    {
        'author': 'Пользователь',
        'title': 'Это второй пост',
        'content': 'Подробное содержание второго поста.',
        'date_posted': '13 мая, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)


def bio(request):
    return render(request, 'about.html', {'title': 'О клубе Python Bytes'})