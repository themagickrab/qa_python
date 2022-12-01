from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_book(self, add_book): #тест на добавление книги +
        collector = add_book.get_books_rating()
        assert len(collector) == 1

    def test_add_new_book_add_book_twice(self, add_book): #тест нельзя добавить одну и ту же книгу дважды +
        add_book.add_new_book('Гордость и предубеждение и зомби')
        collector = add_book.get_books_rating()
        assert len(collector) == 1

    def test_set_book_rating_impossible_to_set_rating_for_book_that_is_not_in_the_list(self, add_book): #Нельзя выставить рейтинг книге, которой нет в списке
        book = 'Что делать, если ваш кот хочет вас убить'
        add_book.set_book_rating(book, 5)
        rating = add_book.get_books_with_specific_rating(5)
        assert book not in rating

    def test_set_book_rating_you_cannot_set_rating_less_than_one(self, add_book): #Нельзя выставить рейтинг меньше 1
        add_book.set_book_rating('Гордость и предубеждение и зомби', 0)
        rating_list = add_book.get_books_with_specific_rating(0)
        assert len(rating_list) == 0

    def test_set_book_rating_you_cannot_set_score_greater_than_10(self, add_book): #Нельзя выставить рейтинг больше 10
        add_book.set_book_rating('Гордость и предубеждение и зомби', 11)
        rating_list = add_book.get_books_with_specific_rating(11)
        assert len(rating_list) == 0

    def test_get_book_rating_book_that_was_not_added_has_no_rating(self, add_book): #У не добавленной книги нет рейтинга.
        add_book.set_book_rating('Что делать, если ваш кот хочет вас убить', 5)
        rating_book = add_book.get_book_rating('Что делать, если ваш кот хочет вас убить')
        assert rating_book == None
    def test_add_book_in_favorites_adding_book_favorites(self, add_book): #Добавление книги в избранное +
        add_book.add_book_in_favorites('Гордость и предубеждение и зомби')
        favorites_book = add_book.get_list_of_favorites_books()
        assert 'Гордость и предубеждение и зомби' in favorites_book

    def test_add_book_in_favorites_cannot_add_book_to_favorites_if_not_in_books_rating_dictionary(self, add_book): #Нельзя добавить книгу в избранное, если её нет в словаре books_rating
        add_book.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        favorites_book = add_book.get_list_of_favorites_books()
        assert 'Что делать, если ваш кот хочет вас убить' not in favorites_book

    def test_delete_book_from_favorites_deleting_book_from_favorites(self,add_book): #Проверка удаления книги из избранного
        add_book.add_book_in_favorites('Гордость и предубеждение и зомби')
        add_book.delete_book_from_favorites('Гордость и предубеждение и зомби')
        favorites_book = add_book.get_list_of_favorites_books()
        assert 'Гордость и предубеждение и зомби' not in favorites_book

    def test_get_books_with_specific_rating_getting_list_of_books_by_rating(self, add_book): #Получение списка книг по рейтингу
        add_book.add_new_book('Война и мир')
        book_list = add_book.get_books_with_specific_rating(1)
        assert 'Война и мир' and 'Гордость и предубеждение и зомби' in book_list

    def test_get_list_of_favorites_books_getting_list_favorite_books(self, add_book):
        add_book.add_new_book('Война и мир')
        add_book.add_book_in_favorites('Гордость и предубеждение и зомби')
        add_book.add_book_in_favorites('Война и мир')
        favorites_books = add_book.get_list_of_favorites_books()
        assert 'Война и мир' and 'Гордость и предубеждение и зомби' in favorites_books








