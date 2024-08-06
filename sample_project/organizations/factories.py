import factory.django

from sample_project.organizations.models import Organization


class OrganizationFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    email = factory.Faker('email')

    class Meta:
        model = Organization
