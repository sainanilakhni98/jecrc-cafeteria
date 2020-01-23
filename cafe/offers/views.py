from django.shortcuts import render
from menu.models import Menu
from .models import Offer

# Create your views here.


def offers(request):
    allProds = []
    catprods = Offer.objects.values('category')
    print(catprods,"This Is CatProds")
    cats = {item['category'] for item in catprods}
    print(cats,"This Is Cats")

    for cat in cats:
        prod = Offer.objects.filter(category=cat)
        allProds.append(prod)
    print(allProds,"This is All Prods")
    params = {'allProds':allProds}
    
    return render(request,'offers/offers.html',params)

def offercategory(request,name):
    if name == "Burger":
        prod = Offer.objects.filter(category=name)
        print(prod)
        params = {'allProds':prod}
        return render(request,"offers/offer-category.html",params)
    if name == "Pizza":
        prod = Offer.objects.filter(category=name)
        print(prod)
        params = {'allProds':prod}
        return render(request,"offers/offer-category.html",params)
    if name == "Maggi":
        prod = Offer.objects.filter(category=name)
        print(prod)
        params = {'allProds':prod}
        return render(request,"offers/offer-category.html",params)
    if name == "Sandwich":
        prod = Offer.objects.filter(category=name)
        print(prod)
        params = {'allProds':prod}
        return render(request,"offers/offer-category.html",params)
    if name == "Chinese":
        prod = Offer.objects.filter(category=name)
        print(prod)
        params = {'allProds':prod}
        return render(request,"offers/offer-category.html",params)
    if name == "Quick Bites":
        prod = Offer.objects.filter(category=name)
        print(prod)
        params = {'allProds':prod}
        return render(request,"offers/offer-category.html",params)
    if name == "Beverages":
        prod = Offer.objects.filter(category=name)
        print(prod)
        params = {'allProds':prod}
        return render(request,"offers/offer-category.html",params)
    if name == "Chat":
        prod = Offer.objects.filter(category=name)
        print(prod)
        params = {'allProds':prod}
        return render(request,"offers/offer-category.html",params)
    if name == "South Indian":
        prod = Offer.objects.filter(category=name)
        print(prod)
        params = {'allProds':prod}
        return render(request,"offers/offer-category.html",params)
    if name == "others":
        prod = Offer.objects.filter(category=name)
        print(prod)
        params = {'allProds':prod}
        return render(request,"offers/offer-category.html",params)

def specials(request):
    
    allProds = []
    catprods = Offer.objects.values('category')
    print(catprods,"This Is CatProds")
    cats = {item['category'] for item in catprods}
    print(cats,"This Is Cats")

    for cat in cats:
        prod = Offer.objects.filter(category=cat)
        allProds.append(prod)
    print(allProds,"This is All Prods")
    params = {'allProds':allProds}
    
    return render(request,'offers/specials.html',params)
