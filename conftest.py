import pytest

from main import BooksCollector

@pytest.fixture # фикстура, которая добавляет книгу
def add_book():
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    return collector
