from django.shortcuts import render

import requests
from django.http import JsonResponse
from django.shortcuts import render

BASE_URL = 'https://anapioficeandfire.com/api'

def get_character(request):
    character_id = request.GET.get('id', '583')  # Default to Jon Snow
    url = f'{BASE_URL}/characters/{character_id}'
    response = requests.get(url)
    character_data = response.json()

    context = {
        'name': character_data.get('name', 'Unknown'),
        'gender': character_data.get('gender', 'Unknown'),
        'culture': character_data.get('culture', 'Unknown'),
        'born': character_data.get('born', 'Unknown'),
        'titles': character_data.get('titles', []),
    }
    return render(request, 'iceandfire/character.html', context)

def get_house(request):
    house_id = request.GET.get('id', '362')  # Default to House Stark
    url = f'{BASE_URL}/houses/{house_id}'
    response = requests.get(url)
    house_data = response.json()

    context = {
        'name': house_data.get('name', 'Unknown'),
        'region': house_data.get('region', 'Unknown'),
        'coatOfArms': house_data.get('coatOfArms', 'Unknown'),
        'words': house_data.get('words', 'Unknown'),
        'titles': house_data.get('titles', []),
    }
    return render(request, 'iceandfire/house.html', context)

def get_book(request):
    book_id = request.GET.get('id', '1')  # Default to the first book
    url = f'{BASE_URL}/books/{book_id}'
    response = requests.get(url)
    book_data = response.json()

    context = {
        'name': book_data.get('name', 'Unknown'),
        'authors': book_data.get('authors', []),
        'numberOfPages': book_data.get('numberOfPages', 'Unknown'),
        'publisher': book_data.get('publisher', 'Unknown'),
        'released': book_data.get('released', 'Unknown'),
    }
    return render(request, 'iceandfire/book.html', context)

def get_character(request):
    character_id = request.GET.get('id', '583')  # Default to Jon Snow
    url = f'https://anapioficeandfire.com/api/characters/{character_id}'
    response = requests.get(url)
    character_data = response.json()

    context = {
        'name': character_data.get('name', 'Unknown'),
        'gender': character_data.get('gender', 'Unknown'),
        'culture': character_data.get('culture', 'Unknown'),
        'born': character_data.get('born', 'Unknown'),
        'titles': character_data.get('titles', []),
    }
    return render(request, 'iceandfire/character.html', context)

def api_get_character(request):
    character_id = request.GET.get('id', '583')  # Default to Jon Snow
    url = f'https://anapioficeandfire.com/api/characters/{character_id}'
    response = requests.get(url)
    character_data = response.json()

    data = {
        'name': character_data.get('name', 'Unknown'),
        'gender': character_data.get('gender', 'Unknown'),
        'culture': character_data.get('culture', 'Unknown'),
        'born': character_data.get('born', 'Unknown'),
        'titles': character_data.get('titles', []),
    }
    return JsonResponse(data)

def index(request):
    return render(request, 'iceandfire/index.html')
