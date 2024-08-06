from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from sample_project.organizations.models import Organization
from sample_project.organizations.serializers import OrganizationSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationRelatedMixin:
    def __init__(self, *args, **kw):
        self.organization = None

    def initial(self, *args, **kw):
        super().initial(*args, **kw)
        print('pass here')
        if 'organization_id' in self.kwargs:
            self.organization = get_object_or_404(Organization.objects.all(), pk=self.kwargs['organization_id'])
        else:
            self.organization = None
