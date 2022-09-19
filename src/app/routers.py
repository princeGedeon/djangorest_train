from rest_framework.routers import DefaultRouter

from app.views import ProductViewSet

router=DefaultRouter()

router.register("product",ProductViewSet,basename="product-app")

urlpatterns=router.urls