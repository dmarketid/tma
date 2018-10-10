from django.shortcuts import render

def index(request):
    context = {
        'tab_title': 'PT Tarsis murni anugrah',
        'heder_logo': '',
    }
    return render(request, 'index.html', context)