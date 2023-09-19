from django.shortcuts import render
from django.http import HttpResponse

def tasks_index(request) -> HttpResponse:
    return HttpResponse('Привет!')
