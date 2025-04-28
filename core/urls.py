from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CustomerViewSet, OrderViewSet, SyncDataViewSet, StatsViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')
router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'sync', SyncDataViewSet, basename='sync')
router.register(r'summary', StatsViewSet, basename='summary')

urlpatterns = router.urls
