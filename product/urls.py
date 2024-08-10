from django.urls import path
from . import views


urlpatterns = [
    path('products/',views.show_product,name='show-product'),
    path('details/<int:id>/',views.show_details,name='about-product'),
    path('remove_product/<int:id>/',views.remove_product,name='remove-product'),
    # path('add_product/',views.add_product,name="add-product")
    path('add_product/',views.AddProduct.as_view(),name="add-product"),
    path('update_product/<int:id>/',views.UpdateProduct.as_view(),name="update-product"),
    path('serach_product/category/<str:name>',views.filter_product_by_category,name='category'),
    path('serach_product/category/<str:name>/brand/<str:b_name>/',views.filter_product_by_brand,name='brand')


    
    
]
