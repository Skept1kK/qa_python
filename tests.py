import pytest

from main import BooksCollector


class TestBooksCollector:


    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2


    @pytest.mark.parametrize('name, genre', [('Цветы для Элджернона', 'Фантастика'),('Сияние', 'Ужасы'),('Шерлок Холмс','Детективы')])
    def test_set_book_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name, genre,expected_genre', [('Цветы для Элджернона', 'Фантастика','Фантастика'),('Шантарам','Проза', '')])
    def test_set_book_genre_invalid(self,name, genre, expected_genre ):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == expected_genre
        if expected_genre:
            assert collector.get_book_genre(name) == expected_genre
        else:
            assert collector.get_book_genre(name) == ''

    @pytest.mark.parametrize('name, expected_genre', [('Цветы для Элджернона', 'Фантастика'),('Сияние', 'Ужасы'),('Венецианский купец', 'Комедии')])
    def test_get_book_genre(self, name, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, expected_genre)
        assert collector.get_book_genre(name) == expected_genre

    @pytest.mark.parametrize('genre, expected_books', [('Фантастика', ['Цветы для Элджернона']),('Ужасы', ['Сияние']), ('Детективы', ['Шерлок Холмс'])])
    def test_get_books_with_specific_genre(self, genre, expected_books):
        collector = BooksCollector()
        for book in expected_books:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        assert collector.get_books_with_specific_genre(genre) == expected_books

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Цветы для Элджернона')
        collector.set_book_genre('Цветы для Элджернона', 'Фантастика')
        assert collector.get_books_genre() == {'Цветы для Элджернона': 'Фантастика'}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Чипполино')
        collector.set_book_genre('Приключения Чипполино', 'Мультфильмы')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        books_for_children = collector.get_books_for_children()
        assert 'Приключения Чипполино' in books_for_children
        assert 'Сияние' not in books_for_children

    @pytest.mark.parametrize('name', [('Сияние'),('Цветы для Элджернона')])
    def test_add_book_in_favorites(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites

    def test_add_book_in_favorites_invalid(self):
        collector = BooksCollector()
        collector.add_new_book('Цветы для Элджернона')
        collector.add_book_in_favorites('')
        assert 'Цветы для Элджернона' not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('name', [ ('Цветы для Элджернона'),('Шерлок Холмс') ])
    def test_delete_book_from_favorites(self,name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')
        assert collector.get_list_of_favorites_books() == ['Шерлок Холмс']