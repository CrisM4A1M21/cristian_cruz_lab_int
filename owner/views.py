from django.shortcuts import render

# Create your views here.

def owner_list(request):
    #data_context = {
    #    'nombre': 'Cristian Cruz',
    #    'edad': 24,
    #    'dni': 88842232,
    #    'pais': 'Perú',
    #    'vigente': False
    #}

    data_context = [
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

    return render(request, 'owner/owner_list.html', context={
        "data_context": data_context
    })
