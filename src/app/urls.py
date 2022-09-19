from django.urls import path, include

#from app.views import ProductMixinView,ListProduct,ListCreateApiView,DeleteProduct,DetailApiView,CreateApiView,UpdateProductView
from rest_framework.authtoken.views import obtain_auth_token
"""
path("delete/<int:pk>",DeleteProduct.as_view(),name="delete"),
path("update/<int:pk>",UpdateProductView.as_view(),name="update"),
  path("detail/<int:pk>",DetailApiView.as_view(),name="projet"),
  path('create/',CreateApiView.as_view(),name="create"),
  path('list_create/',ListCreateApiView.as_view(),name="list_create"),
  path('mixins/', ProductMixinView.as_view(), name="list"),
  """
urlpatterns = [

  path('auth',obtain_auth_token),
  path('product/v2',include("app.routers"))
]
