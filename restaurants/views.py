from django.shortcuts import render
from django.http import HttpResponse

def func(request):
    context = {
        "msg": "Hello World!",
    }
    return render(request, 'some_html_file.html', context)