from django.shortcuts import redirect, render
from .models import BannerCards, Cards
from django.contrib.auth.models import auth
# Create your views here.

def home(request):
    bannerCards = BannerCards.objects.all()
    cards = Cards.objects.all()
    context = {
        'bannerCards': bannerCards,
        'cards': cards,
    }
    return render(request, "Home/home.html", context)

def search(request):
    query = request.GET['query']
    title = Cards.objects.filter(title__icontains=query)
    category = Cards.objects.filter(category__icontains=query)
    allCards = title.union(category)
    context = {
        'allCards': allCards,
        "query": query,
    }
    return render(request, "Home/search.html", context)

def logout(request):
    auth.logout(request)
    return redirect("/")