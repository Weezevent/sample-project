from rest_framework.routers import DefaultRouter

from sample_project.events.views import EventViewSet

router = DefaultRouter(trailing_slash=False)
router.register('events', EventViewSet)

urlpatterns = router.urls
