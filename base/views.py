

from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return HttpResponse('<html> <body> gred</body> </html>')
