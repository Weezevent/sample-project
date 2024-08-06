from rest_framework import viewsets

from sample_project.events.models import Event
from sample_project.events.serializers import EventSerializer
from sample_project.organizations.views import OrganizationRelatedMixin


class EventViewSet(OrganizationRelatedMixin, viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        return super().get_queryset().filter(organization_id=self.organization.id)
