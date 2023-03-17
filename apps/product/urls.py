from rest_framework.routers import DefaultRouter

from . views import ProductView

router = DefaultRouter()
router.register('', ProductView)

urlpatterns = []
urlpatterns += router.urls
