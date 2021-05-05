from django.shortcuts import render

# Create your views here.


def login(request):
    context = {
        'title': 'GeekShop - Авторизация',
    }
    return render(request, 'authapp/login.html', context)

