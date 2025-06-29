import pytest
from books.models import Author


@pytest.fixture
def authors():
    lst = []
    lst.append(Author.objects.create(first_name="Adam",last_name="Mckiewicz"))
    lst.append(Author.objects.create(first_name="Juliusz",last_name="Słowacki"))
    lst.append(Author.objects.create(first_name="Andrzej",last_name="Sapkowski"))
    lst.append(Author.objects.create(first_name="JRR",last_name="Tolkien"))
    lst.append(Author.objects.create(first_name="Andre",last_name="Norton"))
    return lst
