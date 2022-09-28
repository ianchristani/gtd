from django.urls import path
from . import views

app_name='crud'

urlpatterns = [
    path('', views.index, name='index'),
    path('list_products/', views.list_products, name='list_products'),
    path('new/', views.create_product, name='create_product'),
    path('update/<int:id>', views.update_product, name='update_product'),
    path('delete/<int:id>', views.delete_product, name='delete_product'),
]