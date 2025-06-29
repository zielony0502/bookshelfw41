import pytest
from django.test import TestCase
from django.test import Client
from django.urls import reverse

from books.models import Author, Publisher


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

@pytest.mark.django_db
def test_add_author_view_post(authors):
    c = Client()
    url = reverse('add_author')
    data = {
        'first_name': 'John',
        'last_name': 'Doe',
    }
    response = c.post(url, data)
    assert response.status_code == 302
    assert Author.objects.get(**data)


@pytest.mark.django_db
def test_add_publisher_post():
    c = Client()
    url = reverse('add_publisher')
    data = {
        'name':'ala_ma_kotas',
        'year':1999
    }
    response = c.post(url, data)
    assert response.status_code == 302
    assert Publisher.objects.get(**data)


@pytest.mark.django_db
def test_add_publisher_post_not_valid():
    c = Client()
    url = reverse('add_publisher')
    data = {
        'name':'ala_ma_kota',
        'year':1999
    }

    response = c.post(url, data)
    form = response.context["form"]

    assert response.status_code == 200
    assert form.errors
    assert not Publisher.objects.exists()