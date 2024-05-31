from django.urls import reverse
from django.test import RequestFactory
import pytest
from ..views import main, category_list
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books.settings')
import django
django.setup()


@pytest.fixture
def rf():
    return RequestFactory()

@pytest.mark.django_db
def test_main_view(rf):
    request = rf.get('/')
    response = main(request)
    assert response.status_code == 200

@pytest.mark.django_db
def test_category_list_view(rf):
    request = rf.get(reverse('category_list'))
    response = category_list(request)
    assert response.status_code == 200