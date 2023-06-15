from django.db.models import F, Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Owner
from .forms import OwnerForm
from django.core import serializers as ssr
from django.http import HttpResponse

# Create your views here.

def owner_list(request):
    #data_context = {
    #    'nombre': 'Cristian Cruz',
    #    'edad': 24,
    #    'dni': 88842232,
    #    'pais': 'Perú',
    #    'vigente': False
    #}

    """data_context = [
        {
            'nombre': 'Cristian Cruz',
            'edad': 24,
            'dni': 88842232,
            'pais': 'Perú',
            'vigente': False,
            'pokemons': [
                {
                    'nombre_pokemon': 'charizar',
                    'ataques': ['Ataque 1 - Charizard',
                                'Ataque 2 - Charizard',
                                'Ataque 3 - Charizard']
                }
            ]
        },
        {
            'nombre': 'Katty Paredes',
            'edad': 34,
            'dni': 88842002,
            'pais': 'Perú',
            'vigente': False,
            'pokemons': [
                {

                }
            ]
        },
        {
            'nombre': 'Miguel Valera',
            'edad': 26,
            'dni': 88842256,
            'pais': 'Perú',
            'vigente': False,
            'pokemons': [
                {

                }
            ]
        },
        {
            'nombre': 'Liliana Vargas',
            'edad': 26,
            'dni': 44442256,
            'pais': 'Perú',
            'vigente': False,
            'pokemons': [
                {

                }
            ]
        }
    ]

    """
    """Crear un objeto en una tabla de la BD"""
    #p = Owner(nombre="Luis Mejia", edad=29, dni="88888865", pais="España", vigente=True)
    #p.save()

    #p.nombre = "Margarita Tello"
    #p.save()

    #p = Owner(nombre="Ricardo", edad=24, dni="52021041", pais="Peru", vigente=True)
    #p.save()

    #data_context = Owner.objects.all()

    """Filtracion de datos"""
    #data_context = Owner.objects.filter(nombre="Ricardo", edad=22)
    """Filtracion de datos con __contains"""
    #data_context = Owner.objects.filter(nombre__contains="Evelin")
    """Filtracion de datos con __cendswith"""
    #data_context = Owner.objects.filter(nombre__endswith="n")
    """Obtener un solo objeto de la tabla en la BD"""
    #data_context = Owner.objects.get(dni="75214100")
    """Ordenar por cualquier atributo o campo de la tabla"""
    #data_context = Owner.objects.order_by("nombre")
    #data_context = Owner.objects.order_by("edad")
    #data_context = Owner.objects.order_by("-edad")
    """Ordenar concatenando diferentes metodos ORM's"""
    #data_context = Owner.objects.filter(nombre="Marcelo").order_by("edad")
    """Acortar datos - numero fijo de filas"""
    #data_context = Owner.objects.all()[0:5]
    #data_context = Owner.objects.get(id=1)
    #data_context.delete()

    # Actualizar datos

    #Owner.objects.filter(id = 10).update(pais='USA')

    """Utiolizando F expressions"""
    #Owner.objects.filter(edad__lte=25).update(edad=F('edad')+10)
    """Consutlas complejas"""

    query = Q(pais__startswith='Pe') | Q(pais__startswith='Es')
    data_context = Owner.objects.filter(query, edad=25)

    """Negar Q"""
    #query = Q(pais__startswith='Pe') & ~Q(edad=25)
    #data_context = Owner.objects.filter(query)

    #query = Q(pais__startswith='Pe') | Q(pais__startswith='Es')
    #data_context = Owner.objects.filter(query, edad=19)

    #data_context = Owner.objects.all()

    return render(request, 'owner/owner_list.html', context={
        "data_context": data_context
    })


def owner_search(request):

    query = request.GET.get('q', '')
    print("Query {}".format(query))

    result = Q(nombre__icontains=query)

    data_context = Owner.objects.filter(result).distinct()

    return render(request, 'owner/owner_search.html', context={
        'data': data_context,
        'query': query
    })


def owner_details(request):
    """Obtener todos los elementos de una tabla de la BD"""
    owners = Owner.objects.all()
    return render(request, 'owner/owner_details.html', context={
        'owners': owners
    })


def owner_create(request):
    form = OwnerForm(request.POST)

    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        edad = form.cleaned_data['edad']
        pais = form.cleaned_data['pais']
        form.save()
        return redirect('owner_details')
    else:
        form = OwnerForm()

    return render(request, 'owner/owner_create.html', {'form': form})


def owner_delete(request, id_owner):
    print("ID Owner: {}".format(id_owner))
    owner = Owner.objects.get(id=id_owner)
    owner.delete()
    return redirect('owner_details')


def owner_edit(request, id_owner):
    #print("ID Owner a editar: {}".format(id_owner))
    owner = Owner.objects.get(id=id_owner)
    form = OwnerForm(initial={'nombre': owner.nombre, 'edad': owner.edad, 'pais': owner.pais, 'dni': owner.dni})
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_details')

    return render(request, 'owner/owner_update.html', context={'form': form})


"""Vistas basadas en clases"""
"""ListView"""


class OwnerList(ListView):
    model = Owner
    template_name = 'owner/owner_list_vc.html'


class OwnerCreate(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner_create.html'
    success_url = reverse_lazy('owner_list_vc')


class OwnerUpdate(UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner_update_vc.html'
    success_url = reverse_lazy('owner_list_vc')


class OwnerDelete(DeleteView):
    model = Owner
    success_url = reverse_lazy('owner_list_vc')
    template_name = 'owner/owner_confirm_delete.html'

"""Serializers"""

def ListOwnerSerializer(request):
    lista_owner = ssr.serialize('json', Owner.objects.all(), fields=['nombre', 'pais', 'edad', 'dni'])
    return HttpResponse(lista_owner, content_type="application/json")
