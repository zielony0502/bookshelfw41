import pytest
from django.test import TestCase
from django.test import Client
from django.urls import reverse

from books.models import Author


# Create your tests here.
@pytest.mark.django_db
def test_index_view():
    c = Client()
    url = "/"
    response = c.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_author_view_get(authors):
    c = Client()
    url = reverse('add_author')
    response = c.get(url)
    assert response.status_code == 200
    assert response.context["authors"].count() == len(authors)
    for author in authors:
        assert author in response.context["authors"]