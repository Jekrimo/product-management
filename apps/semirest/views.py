from django.shortcuts import render, HttpResponse, redirect
from .models import Products

def index(request):
    context = {
        "Products" : Products.objects.all()
    }
    return render(request, "semirest/index.html", context)

def new(request):
    return render(request, "semirest/new.html")

def create(request):
    Products.objects.create(name = request.POST['name'], description = request.POST['description'], price = request.POST['price'])
    return redirect('/products')

def show(request, id):
     product = Products.objects.get(id=id)
     context = {
         'Product' : product,
         'id' : id
     }
     return render(request, 'semirest/show.html', context)
def edit(request, id):
    product = Products.objects.get(id=id)
    context = {
        'Product' : product,
        'id' : id
    }
    return render(request, "semirest/edit.html", context)

def update(request, id):
    Products.objects.filter(id=id).update(name = request.POST['name'], description = request.POST['description'], price = request.POST['price'])
    return redirect('/products')

def destroy(request, id):
    Products.objects.filter(id=id).delete()
    return redirect('/products')
