from django.urls import path
from shopifyapp.views import(
    IndexPageView, CreateProductView, CreateCategoryView , ViewProduct , EditProduct , DeleteProduct , SearchProduct
)

urlpatterns = [
    path(''   , IndexPageView.as_view() , name="home"),
    path('create-product/' , CreateProductView.as_view() , name="create-product"),
    path('create-category/' , CreateCategoryView.as_view() , name="create-category"),
    path('view-product/<int:id>/' , ViewProduct.as_view() ,name="view-product"),
    path('edit-product/<int:id>/' , EditProduct.as_view() ,name="edit-product"),
    path('delete-product/<int:id>/' , DeleteProduct.as_view() ,name="delete-product"),
    path('search-product/' , SearchProduct.as_view() ,name="search-product"),
]