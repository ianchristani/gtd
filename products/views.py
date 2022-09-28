from django.shortcuts import render, redirect
from .models import products_model
from .forms import products_form

# Create your views here.
def index(request):
    return render(request, 'index.html')

def list_products(request):
    products_list = products_model.objects.all()
    return render(request, 'products.html', {'products':products_list})

def create_product(request):
    form_instance = products_form(request.POST or None)

    if form_instance.is_valid():
        form_instance.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'product_form':form_instance})

def update_product(request, id):
    selected_product = products_model.objects.get(id=id)
    form_instance = products_form(request.POST or None, instance=selected_product)

    if form_instance.is_valid():
        form_instance.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'product_form':form_instance, 'id':selected_product})

def delete_product(request, id):
    selected_product = products_model.objects.get(id=id)
    
    if request.method == 'POST':
        selected_product.delete()
        return redirect('list_products')

    return render(request, 'prod-delete-confirmation.html', {'product_to_delete':selected_product})

