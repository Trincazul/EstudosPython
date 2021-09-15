from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {}</h1> sua idade é {}'.format(nome, idade))

def soma(request, num1, num2):
    som = int(num1) + int(num2)
    return HttpResponse(f'Voce digitou o {num1} e tambem o {num2} e a soma deles é {som}')