from django.shortcuts import render

# Create your views here.

def owner_list(request):
    data_context = {
        'nombre':'Katy Paredes',
        'edad': 24,
        'dni': 88842232,
        'pais':'Peru'
    }

    return render(request, 'owner/owner_list.html', data_context)
