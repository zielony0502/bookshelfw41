import datetime

from random import randint


def data(request):
    return {'data':datetime.datetime.now()}


def girka(request):
    x = randint(1, 100)

    return {'liczba':x}