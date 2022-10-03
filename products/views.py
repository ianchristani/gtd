from django.shortcuts import render, redirect
from .models import products_model
from .forms import products_form


# pagina inicial de usuarios logados no CRUD
def list_products(request):
    products_list = products_model.objects.all()
    return render(request, 'products.html', {'products':products_list})

# pagina de inclusao de dados
def create_product(request):
    form_instance = products_form(request.POST or None, request.FILES or None)

    if form_instance.is_valid():
        form_instance.save()
        return redirect('crud:list_products')

    return render(request, 'products-form.html', {'product_form':form_instance})

# pagina de edicao de dados
def update_product(request, id):
    selected_product = products_model.objects.get(id=id)
    form_instance = products_form(request.POST or None, request.FILES or None, instance=selected_product)

    if form_instance.is_valid():
        form_instance.save()
        return redirect('crud:list_products')
    
    return render(request, 'products-form.html', {'product_form':form_instance, 'id':selected_product})

# pagina de exclusao de dados
def delete_product(request, id):
    selected_product = products_model.objects.get(id=id)
    
    if request.method == 'POST':
        selected_product.delete()
        return redirect('crud:list_products')

    return render(request, 'prod-delete-confirmation.html', {'product_to_delete':selected_product})

