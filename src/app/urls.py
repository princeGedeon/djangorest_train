from django.urls import path



from app.views import add_product,product_all

urlpatterns = [
  path('product_all', product_all, name="product_all"),
  path('add_product',add_product,name="add_product")

]
