from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'app_name': 'Inventory App',
        'name': 'Mario Michael Jeremy Sitanggang',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)