import pytest
from django.urls import resolve


@pytest.mark.parametrize('path,view,kwargs', [
    ('/organizations/', 'OrganizationViewSet', {}),
    ('/organizations/1', 'OrganizationViewSet', {'pk': '1'}),
])
def test_resolve(path, view, kwargs):
    r = resolve(path)

    assert r.func.cls.__name__ == view
    assert r.kwargs == kwargs
