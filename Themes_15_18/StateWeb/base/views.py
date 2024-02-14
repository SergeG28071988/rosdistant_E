from django.shortcuts import render, redirect, get_object_or_404

from .models import Human
from .human_form import HumanForm
from .models import City
from .city_form import CityForm
from .models import Country
from .country_form import CountryForm

# Create your views here.


# Маршруты для работы с людьми 
def human_list(request):
    humans = Human.objects.all()
    context = {'title': 'Главная страница сайта', 'humans': humans}
    return render(request, 'human_list.html', context)

def add_human(request):
    if request.method == 'POST':
        form = HumanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('human_list')  # перенаправляем на страницу успешного добавления
    else:
        form = HumanForm()
    return render(request, 'add_human.html', {'form': form})


def human_detail(request, pk):
    human = get_object_or_404(Human, pk=pk)
    return render(request, 'human_detail.html', {'human': human})


def delete_human(request, pk):
    human = get_object_or_404(Human, pk=pk)
    human.delete()
    return redirect('human_list')


def edit_human(request, pk):
    human = get_object_or_404(Human, pk=pk)
    if request.method == 'POST':
        form = HumanForm(request.POST, instance=human)
        if form.is_valid():
            form.save()
            return redirect('human_list')
    else:
        form = HumanForm(instance=human)

    return render(request, 'edit_human.html', {'form': form})


# Маршруты для работы с городами
def city_list(request):
    cities = City.objects.all()
    context = {'title': 'Города', 'cities': cities}
    return render(request, 'city_list.html', context)

def add_city(request):
    error = ''
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('city_list')
        else:
            error = "Форма была не верной"
    form = CityForm()
    context = {        
        'form': form,
        'error': error
    }
    return render(request, 'add_city.html', context)

def city_detail(request, pk):
    citie = get_object_or_404(City, pk=pk)
    return render(request, 'city_detail.html', {'citie': citie})


def delete_city(request, pk):
    citie = get_object_or_404(City, pk=pk)
    citie.delete()
    return redirect('city_list')


def edit_city(request, pk):
    citie = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        form = CityForm(request.POST, instance=citie)
        if form.is_valid():
            form.save()
            return redirect('city_list')
    else:
        form = CityForm(instance=citie)

    return render(request, 'edit_city.html', {'form': form})


# Маршруты для работы со странами
def country_list(request):
    countries = Country.objects.all()
    context = {'title': 'Страны', 'countries': countries}
    return render(request, 'country_list.html', context)

def add_country(request):
    error = ''
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('country_list')
        else:
            error = "Форма была не верной"
    form = CountryForm()
    context = {        
        'form': form,
        'error': error
    }
    return render(request, 'add_country.html', context)

def country_detail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    return render(request, 'country_detail.html', {'country': country})


def delete_country(request, pk):
    country = get_object_or_404(Country, pk=pk)
    country.delete()
    return redirect('country_list')


def edit_country(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('country_list')
    else:
        form = CountryForm(instance=country)

    return render(request, 'edit_country.html', {'form': form})