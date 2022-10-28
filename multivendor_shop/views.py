from django.shortcuts import render


def master(request):
    return render(request, 'master.html',{})


def index(request):
    return render(request, 'index.html', {})