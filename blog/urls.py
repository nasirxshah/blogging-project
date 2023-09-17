from rest_framework.routers import SimpleRouter
from .views import BlogPostViewSet

router = SimpleRouter()
router.register('blogs',BlogPostViewSet, basename="blogs")

urlpatterns = router.urls