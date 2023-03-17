from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from data_base.models import *


# Create your views here.
dataCat = Categories.objects.all()
dataNameCat = NameCategories.objects.all()
raz = Raz.objects.all()
glav = Glav.objects.all()
dataTheme = Theme.objects.all()
newsData = News.objects.all().order_by('-date')[:6]
ab = About.objects.all()


def index(request):
    context = {
        'dataCat': dataCat,
        'dataNameCat': dataNameCat,
        'news': newsData,
    }
    return render(request, 'website/index.html', context)


def cat(request, pk):
    raz = Raz.objects.all().filter(categori_id=pk)
    dNames = NameCategories.objects.all().filter(id=pk)

    context = {
        'dataCat': dataCat,
        'dataNameCat': dataNameCat,
        'dataTheme': dataTheme,
        'razs': raz,
        'dNames': dNames,
        'glavs': glav,
    }
    return render(request, 'website/cat.html', context)


def them_cat(request, pk, bi):
    them = Theme.objects.all().filter(id=bi)
    raz = Raz.objects.all().filter(categori_id=pk)
    dNames = NameCategories.objects.all().filter(id=pk)

    context = {
        'them': them,
        'dataCat': dataCat,
        'dataNameCat': dataNameCat,
        'dataTheme': dataTheme,
        'razs': raz,
        'glavs': glav,
        'dNames': dNames
    }

    return render(request, 'website/them_cat.html', context)


def footer(request):
    dNames = NameCategories.objects.all().filter(id)
    return render(request, 'website/includes/footer.html', {'dNames': dNames})

def news(requet):
    return render(requet, )

def about(request):
    context = {
        'ab': ab
    }
    return render(request, 'website/about.html', context)

def InfoView(request, pk):
    post = News.objects.all().filter(id=pk)
    context = {
        'dataCat': dataCat,
        'dataNameCat': dataNameCat,
        'news': newsData,
        'post': post
    }
    return render(request, 'website/news.html', context)


def information(request):
    context = {
        'dataCat': dataCat,
        'dataNameCat': dataNameCat,
        'news': newsData,
    }
    return render(request, 'website/info.html', context)