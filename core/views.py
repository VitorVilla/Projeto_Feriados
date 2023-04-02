from django.shortcuts import render
from datetime import datetime

contexto = {
    "natal": False,
    "tiradentes": False
}


def natal(request):
    if datetime.now().day == 25 and datetime.now().month == 12:
        contexto["Hoje é natal"] = True
    return render(request, 'natal.html', contexto)


def tiradentes(request):
    if datetime.now().day == 20 and datetime.now().month == 4:
        contexto["Hoje é tiradentes"] = True
    return render(request, 'tiradentes.html', contexto)
