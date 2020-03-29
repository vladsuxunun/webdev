from django.urls import path

from . import views

app_name='api'

urlpatterns = [
    path('',views.index,name='index'),
    path('categories/',views.categories,name='categories'),
    path('products/',views.products,name='products'),
    path('products/<int:product_id>/',views.product_details,name='product_details'),
    path('categories/<int:category_id>/',views.category_details,name='category_details'),
    path('categories/<int:category_id>/products/',views.categories_products,name='categories_products')
]