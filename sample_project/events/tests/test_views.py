import pytest

from sample_project.events.factories import EventFactory
from sample_project.events.models import Event
from sample_project.events.views import EventViewSet
from sample_project.organizations.factories import OrganizationFactory


@pytest.fixture
def organization():
    return OrganizationFactory()

@pytest.fixture
def event_viewset_list(api_rf):
    return EventViewSet.as_view({
        'get': 'list',
        'post': 'create',
    },
        pagination_class=None,
        authentication_classes=[],
        permission_classes=[])


@pytest.mark.django_db
def test_list_event(api_rf, event_viewset_list, organization):
    EventFactory(organization=organization)
    request = api_rf.get('/')
    response = event_viewset_list(request, organization_id=organization.id)

    assert response.status_code == 200, response.data
    assert len(response.data) == 1


@pytest.mark.django_db
def test_create_event(api_rf, event_viewset_list, organization):

    data = {
        "name": "my first event",
        "organization": organization.id,
        "type": "conference"
    }
    request = api_rf.post('/', data=data, format='json')

    response = event_viewset_list(request, organization_id=organization.id)

    assert response.status_code == 201, response.data
    event = Event.objects.last()

    assert event.name == "my first event"
