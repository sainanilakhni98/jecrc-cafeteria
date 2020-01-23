from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu,FeedBack
from .forms import Showdata
# Create your views here.

def menu(request):
    allProds = []
    catprods = Menu.objects.values('category')
    print(catprods,"This Is CatProds")
    cats = {item['category'] for item in catprods} 
    print(cats,"This Is Cats")

    for cat in cats:
        prod = Menu.objects.filter(category=cat)
        allProds.append(prod)
    print(allProds,"This is All Prods")
    params = {'allProds':allProds}
    
    return render(request,'menu/menu.html',params)

def SeeFeedback(request):
    allProds = []
    catprods = FeedBack.objects.values('product_name')
    print(catprods,"This Is CatProds")
    # product_image= Menu.objects.values('product_name')
    # cats = {item['product_name'] for item in catprods} 
    # print(cats,"This Is Cats")

    # l=[]
    # for cat in cats:
    #     prod_image = Menu.objects.filter(product_name=cat)
    #     l.append(prod_image)    
    cats = {item['product_name'] for item in catprods} 
    print(cats,"This Is Cats")
    for cat in cats:
        prod = FeedBack.objects.filter(product_name=cat)
        prod_image = Menu.objects.filter(product_name=cat)
        # if prod.product_name in prod_image:
        s=0
        avg_rating=0
        for product in prod:
            s=s+product.product_ratings
        else:
            if len(prod)!=0:
                avg_rating = s/len(prod)
        allProds.append([prod,avg_rating,prod_image])
    print(allProds,"This is All Prods")
    params = {'allProds':allProds}
    return render(request,'menu/SeeFeedback.html',params)
    # return HttpResponse(catprods)
def singlecategory(request,name):
    if name == "Burger":
        prod = Menu.objects.filter(category=name)
        l=[]
        for i in prod:
            if i in l :
                pass
            else:
                l.append(i)
        l=set(l)
        print(l,"fjfffiyfiyfyf")

        print(prod)
        params = {'allProds':l}
        return render(request,"menu/single-category.html",params)
    if name == "Pizza":
        prod = Menu.objects.filter(category=name)
        prod=set(prod)
        print(prod)
        params = {'allProds':prod}
        return render(request,"menu/single-category.html",params)
    if name == "Maggi":
        prod = Menu.objects.filter(category=name)
        prod=set(prod)
        print(prod)
        params = {'allProds':prod}
        return render(request,"menu/single-category.html",params)
    if name == "Sandwich":
        prod = Menu.objects.filter(category=name)
        prod=set(prod)
        print(prod)
        params = {'allProds':prod}
        return render(request,"menu/single-category.html",params)
    if name == "South Indian":
        prod = Menu.objects.filter(category=name)
        prod=set(prod)
        print(prod)
        params = {'allProds':prod}
        return render(request,"menu/single-category.html",params)
    if name == "Quick Bites":
        prod = Menu.objects.filter(category=name)
        prod=set(prod)
        print(prod)
        params = {'allProds':prod}
        return render(request,"menu/single-category.html",params)
    if name == "Chat":
        prod = Menu.objects.filter(category=name)
        prod=set(prod)
        print(prod)
        params = {'allProds':prod}
        return render(request,"menu/single-category.html",params)
    if name == "Chinese":
        prod = Menu.objects.filter(category=name)
        prod=set(prod)
        print(prod)
        params = {'allProds':prod}
        return render(request,"menu/single-category.html",params)
    if name == "Others":
        prod = Menu.objects.filter(category=name)
        prod=set(prod)
        print(prod)
        params = {'allProds':prod}
        return render(request,"menu/single-category.html",params)
   
# def searchMatch(query, item):
#     '''return true only if query matches the item'''
#     if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
#         return True
#     else:
#         return False

def search(request):
    query = request.POST.get('search')
    
    print(query)
    # allProds = []
    # catprods = Product.objects.values('category')
    # cats = {item['category'] for item in catprods} 
    # for cat in cats:
    #     if cat == 'Burger':
    #         prodtemp = Product.objects.filter(category=cat)
    #         prod = [item for item in prodtemp if searchMatch(query, item)]
            
    #         n = len(prod)
    #         if len(prod) != 0:
    #             allProds.append(prod)
    #         params = {'allProds': allProds, "msg": ""}
    #         return render(request,menu/search.html
    #         , params)
    
    # data = Menu.objects.filter(category=query)
    # params = {'data':data}
    # return render(request,"menu/search.html",params)
    query = query.title()
    prod = Menu.objects.filter(category=query)
    print(prod,"this is a product")
    params = {'allProds':prod}
    return render(request,"menu/single-category.html",params)

def feedback(request):
    
    form = Showdata()
    return render(request,"menu/feedback.html")

def showdata(request):
    form = Showdata(request.POST)
    data="Your form is submitted"
    if form.is_valid():
        if request.method == "POST":
            dict = {
                    'product_name' : form.cleaned_data['product_name'],
                    'product_ratings' : form.cleaned_data['product_ratings'],
                    'comment' : form.cleaned_data['comment']
                } 
            new_user = FeedBack.objects.create(**dict)
            new_user.save()
            return render(request,"menu/OtherFeedback.html")
            # return HttpResponse("Success")

def OtherFeedback(request):
    allProds = []
    catprods = FeedBack.objects.values('product_ratings')
    print(catprods,"This Is CatProds")
    # cats = {item['category'] for item in catprods}
    # print(cats,"This Is Cats")

    # for cat in cats:
    #     prod = Menu.objects.filter(category=cat)
    #     allProds.append(prod)
    # print(allProds,"This is All Prods")
    # params = {'allProds':allProds}
    
    # return render(request,'menu/menu.html',params)
    return HttpResponse("Success")

def offers(request):
    allProds = []
    catprods = Menu.objects.values('category')
    print(catprods,"This Is CatProds")
    cats = {item['category'] for item in catprods}
    print(cats,"This Is Cats")

    for cat in cats:
        prod = Menu.objects.filter(category=cat)
        allProds.append(prod)
    print(allProds,"This is All Prods")
    params = {'allProds':allProds}
    
    return render(request,'menu/offers.html',params)
def about(request):
    return render(request,'menu/about.html')
  
