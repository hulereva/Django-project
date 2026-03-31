from django.shortcuts import render

def index(request):  #request - запрос
    data = {
        'title': 'Главная страница',
        'value': ['Some', 'Hello', '123'] #массив который будет передавать данные
    }
    return render(request, 'main/index.html', data) #при написании текста сохраняются настройки текста языка HTML

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')