import pytest
from django.urls import resolve


@pytest.mark.parametrize('path,view,kwargs', [
    ('/organizations/1/events', 'EventViewSet', {'organization_id': 1}),
    ('/organizations/1/events/2', 'EventViewSet', {'organization_id': 1, 'pk': '2'})
])
def test_resolve(path, view, kwargs):
    r = resolve(path)

    assert r.func.cls.__name__ == view
    assert r.kwargs == kwargs
