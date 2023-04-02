from django.shortcuts import render
from datetime import datetime

from django.http import HttpResponse

contexto = {
    "natal":False,
    "tiradentes":False
}
def natal(request):
    if datetime.now().month == 12 and datetime.now().day == 25:
        contexto["Hoje é natal"] = True
    return render(request, 'natal.html', contexto)

def tiradentes(request):
    if datetime.now().month == 4 and datetime.now().day == 20:
        contexto["Hoje é tiradentes"] = True
    return render(request, 'tiradentes.html', contexto)