
import json
from typing import Dict, Union, List

class Book:
    """
    Класс, представляющий книгу в библиотеке.

    Атрибуты:
        id (int): Уникальный идентификатор книги.
        title (str): Название книги.
        author (str): Автор книги.
        year (str): Год издания книги.
        status (str): Статус книги (в наличии, выдана).
    """

    def __init__(self, title: str, author: str, year: str, status: str) -> None:
        """
        Инициализирует новый экземпляр класса Book.

        Параметры:
            title (str): Название книги.
            author (str): Автор книги.
            year (str): Год издания книги.
            status (str): Статус книги.
        """
        self.id = None
        self.title = title
        self.author = author
        self.year = year
        self.status = status
    
    def to_dict(self) -> Dict[str, Union[str, int]]:
        """
        Преобразует объект книги в словарь.

        Возвращает:
            dict: Словарь, представляющий книгу.
        """
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }

    @staticmethod
    def from_dict(data: Dict[str, str]) -> 'Book':
        """
        Создает объект книги из словаря.

        Параметры:
            data (dict): Словарь с данными книги.

        Возвращает:
            Book: Объект книги.
        """
        book = Book(data['title'], data['author'], data['year'], data['status'])
        book.id = data['id']
        return book
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта книги.

        Возвращает:
            str: Строковое представление книги.
        """
        return f"ID: {self.id}, Название: {self.title}, Автор: {self.author}, "\
                f"Год издания: {self.year}, Статус: {self.status}"

class Library:
    """
    Класс, представляющий библиотеку.

    Атрибуты:
        books (list): Список книг в библиотеке.
    """

    def __init__(self) -> None:
        """
        Инициализирует новый экземпляр класса Library и загружает книги из файла.
        """
        self.books: List[Book] = []
        self.load_from_file()

    def add_book(self, title: str, author: str, year: str, status: str ="в наличии") -> None:
        """
        Добавляет новую книгу в библиотеку и сохраняет изменения в файл.

        Параметры:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
            status (str): Статус книги (по умолчанию "в наличии").
        """
        book = Book(title, author, year, status)
        book.id = len(self.books) + 1
        self.books.append(book)
        self.save_to_file()

    def remove_book(self, book_id: int) -> bool:
        """
        Удаляет книгу по её идентификатору и сохраняет изменения в файл.

        Параметры:
            book_id (int): Идентификатор книги для удаления.
        """
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_to_file()
                return True
        return False

    def search_book(self, keyword: str) -> List[Book]:
        """
        Поиск книг по ключевому слову в названии, авторе или году издания.

        Параметры:
            keyword (str): Ключевое слово для поиска.

        Возвращает:
            list: Список найденных книг, соответствующих ключевому слову.
        """
        found_books: List[Book] = []
        for book in self.books:
            if (keyword.lower() in book.title.lower() or
                keyword.lower() in book.author.lower() or
                keyword in book.year):
                found_books.append(book)
        return found_books

    def change_status(self, book_id: int, new_status: str) -> bool:
        """
        Изменяет статус книги по её идентификатору.

        Параметры:
            book_id (int): Идентификатор книги.
            new_status (str): Новый статус книги.

        Возвращает:
            bool: True, если статус книги был успешно изменён, иначе False.
        """
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                self.save_to_file()
                return True
        return False

    def list_books(self) -> List[Book]:
        """
        Возвращает список всех книг в библиотеке.

        Возвращает:
            list: Список книг.
        """
        return self.books

    def save_to_file(self) -> None:
        """
        Сохраняет текущий список книг в файл в формате JSON.
        """
        with open('library.json', 'w') as file:
            json.dump([book.to_dict() for book in self.books], file)

    def load_from_file(self) -> None:
        """
        Загружает список книг из файла в формате JSON. Если файл не найден, создаёт пустой список книг.
        """
        try:
            with open('library.json', 'r') as file:
                self.books = [Book.from_dict(book_dict) for book_dict in json.load(file)]
        except FileNotFoundError:
            self.books = []
