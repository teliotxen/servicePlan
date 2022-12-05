from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(request, 'landing/landing.html')


def test(request):
    return render(request, 'landing/test.html')


def doubles(request, *args, **kwargs):
    print(kwargs)
    return render(request, 'landing/test.html')