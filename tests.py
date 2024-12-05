import pytest

from main import BooksCollector


class TestBooksCollector:


    def test_add_new_book_add_two_books(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2


    @pytest.mark.parametrize('name, genre', [('Цветы для Элджернона', 'Фантастика'),('Сияние', 'Ужасы'),('Шерлок Холмс','Детективы')])
    def test_set_book_genre(self, name, genre,collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_add_book_without_name(self,collector):
        book_not_name=''
        collector.add_new_book(book_not_name)
        assert book_not_name not in collector.get_books_genre()

    def test_add_duplicate_book(self, collector):
        collector.add_new_book('Венецианский купец')
        collector.add_new_book('Венецианский купец')
        assert list(collector.books_genre.keys()).count('Венецианский купец') == 1


    def test_get_books_with_specific_genre(self,collector):
        collector.add_new_book('Цветы для Элджернона')
        collector.set_book_genre('Цветы для Элджернона', 'Фантастика')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Сияние']

    def test_get_books_genre(self,collector):
        collector.add_new_book('Цветы для Элджернона')
        collector.set_book_genre('Цветы для Элджернона', 'Фантастика')
        assert collector.get_books_genre() == {'Цветы для Элджернона': 'Фантастика'}

    def test_get_books_for_children(self,collector):
        collector.add_new_book('Приключения Чипполино')
        collector.set_book_genre('Приключения Чипполино', 'Мультфильмы')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        books_for_children = collector.get_books_for_children()
        assert 'Сияние' not in books_for_children

    @pytest.mark.parametrize('name', [('Сияние'),('Цветы для Элджернона')])
    def test_add_book_in_favorites(self, name,collector):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites

    def test_add_book_in_favorites_invalid(self,collector):
        collector.add_new_book('Цветы для Элджернона')
        collector.add_book_in_favorites('')
        assert collector.get_list_of_favorites_books() ==[]

    @pytest.mark.parametrize('name', [ ('Цветы для Элджернона'),('Шерлок Холмс') ])
    def test_delete_book_from_favorites(self,name,collector):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites

    def test_get_list_of_favorites_books(self,collector):
        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Сияние')
        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')
        collector.delete_book_from_favorites('Шерлок Холмс')
        assert collector.get_list_of_favorites_books() == ['Сияние']