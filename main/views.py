from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406440023',
        'name': 'Saffana Firsta Aqila',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
