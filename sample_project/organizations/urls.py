from rest_framework.routers import DefaultRouter
from django.urls import path, include

from sample_project.organizations.views import OrganizationViewSet

router = DefaultRouter(trailing_slash=False)
router.register('', OrganizationViewSet)

urlpatterns = router.urls

