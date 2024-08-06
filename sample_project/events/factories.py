import factory.django

from sample_project.events.models import Event
from sample_project.organizations.factories import OrganizationFactory


class EventFactory(factory.django.DjangoModelFactory):
    organization = factory.SubFactory(OrganizationFactory)
    name = factory.Faker('name')

    class Meta:
        model = Event
