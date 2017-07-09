from rest_framework.routers import DefaultRouter
from .views import RandomNumberViewset

router = DefaultRouter()
router.register(r'random', RandomNumberViewset)
urlpatterns = router.urls
