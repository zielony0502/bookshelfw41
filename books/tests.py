import pytest
from django.test import TestCase
from django.test import Client
# Create your tests here.
@pytest.mark.django_db
def test_index_view():
    c = Client()
    url = "/"
    response = c.get(url)
    assert response.status_code == 200