from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from zrzuta.models import Zrzuta


def index(request):
    return HttpResponse('<h1>Witaj w aplikacji zrzuta :)</h1>')


def about(request):
    text = '<h1>To ja Alek!</h1>'
    now = datetime.now()
    text = text + f'<br>strona wygenerowana: {now}'
    return HttpResponse(text)


def zrzuta(request, id=None):
    if id is None:
        return HttpResponse('Tutaj będzie lista zrzut')

    all_z = Zrzuta.objects.all()
    z = all_z.get(id=id)

    data = {}
    data['id'] = id
    data['user'] = z.user
    data['sum'] = z.sum

    return render(request, 'zrzuta/szablon.html', context=data)
