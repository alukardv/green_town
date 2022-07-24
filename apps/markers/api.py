from rest_framework import routers
from apps.markers.viewsets import MarkerViewSet


router = routers.DefaultRouter()
router.register(r"markers", MarkerViewSet)

urlpatterns = router.urls