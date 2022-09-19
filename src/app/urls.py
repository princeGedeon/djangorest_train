from django.urls import path



from app.views import ListProduct,ListCreateApiView,DeleteProduct,DetailApiView,CreateApiView,UpdateProductView

urlpatterns = [

path("delete/<int:pk>",DeleteProduct.as_view(),name="delete"),
path("update/<int:pk>",UpdateProductView.as_view(),name="update"),
  path("detail/<int:pk>",DetailApiView.as_view(),name="projet"),
  path('create/',CreateApiView.as_view(),name="create"),
  path('list_create/',ListCreateApiView.as_view(),name="list_create"),
  path('list/', ListProduct.as_view(), name="list")

]
