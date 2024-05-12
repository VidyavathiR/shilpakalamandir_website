from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def gallery(request):
    return render(request, 'gallery.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def brass(request):
    return render(request, 'brass.html')

def alankara(request):
    return render(request, 'alankara.html')

def vigraha(request):
    return render(request, 'vigraha.html')

def silver(request):
    return render(request, 'portfolioitems\silver.html')