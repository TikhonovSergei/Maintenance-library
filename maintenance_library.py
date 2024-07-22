"""
Библиотека книг представляет собой простую систему управления библиотекой,
позволяющую добавлять, удалять, искать и изменять статус книг.
"""
from library import Book, Library
from typing import NoReturn


class ConsoleApp:
    """
    Класс ConsoleApp предоставляет текстовый интерфейс пользователя
    для управления библиотекой книг.
    """
     
    def __init__(self) -> None:
        """
        Инициализирует новый экземпляр ConsoleApp с пустой библиотекой.
        """
        self.library = Library()

    def run(self) -> NoReturn:
        """
        Запускает основной цикл приложения, предоставляя пользователю
        меню для выполнения различных действий с книгами.
        """
        while True:
            print("Выберите действие:")
            print("1. Добавить книгу")
            print("2. Удалить книгу")
            print("3. Поиск книги")
            print("4. Отобразить все книги")
            print("5. Изменить статус книги")
            print("0. Выход")
            command = input("Введите номер действия: ")
            if command == '1':
                self.add_book()
            elif command == '2':
                self.remove_book()
            elif command == '3':
                self.find_book()
            elif command == '4':
                self.list_books()
            elif command == '5':
                self.change_status()
            elif command == '0':
                print("Выход из программы.")
                break
            else:
                print("Неизвестная команда. Попробуйте еще раз.")

    def add_book(self) -> None:
        """
        Запрашивает у пользователя данные о книге и добавляет её в библиотеку.
        """
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = input("Введите год издания книги: ")
        self.library.add_book(title, author, year)
        print("Книга добавлена.")

    def remove_book(self) -> None:
        """
        Запрашивает у пользователя идентификатор книги и удаляет её из библиотеки.
        """
        book_id = input("Введите id книги для удаления: ")
        try:
            book_id = int(book_id)
        except ValueError:
            print("Некорректный id книги. Введите число.")
            return
        if self.library.remove_book(book_id):
            print("Книга удалена.")
        else:
            print("Книга не найдена.")

    def find_book(self) -> None:
        """
        Запрашивает у пользователя ключевое слово для поиска книги и
        отображает результаты поиска. Если книги найдены, выводит их список.
        В противном случае сообщает о том, что книги не найдены.
        """
        keyword = input("Введите значение для поиска книги: ")
        books = self.library.search_book(keyword)
        if books:
            print(f"Найдено:")
            for book in books:
                print(book)
        else:
            print("Книга не найдена.")
    
    def change_status(self, book_id: str=None) -> None:
        """
        Запрашивает у пользователя идентификатор книги и новый статус для неё.
        Позволяет изменить статус книги на "в наличии" или "выдана".
        В случае некорректного ввода идентификатора или выбора несуществующего статуса,
        сообщает об ошибке.
        """
        if not book_id:
            book_id = input("Введите id книги: ")
        print("Введите новый статус:")
        print("1. В наличии")
        print("2. Выдана")
        number_status = input("Введите номер статуса: ")
        if number_status == '1':
            new_status = "в наличии"
        elif number_status == '2':
            new_status = "выдана"
        else:
            print("Неизвестный статус.")
            self.change_status(book_id)
        try:
            book_id = int(book_id)
        except ValueError:
            print("Некорректный id книги. Введите число.")
            return
        if self.library.change_status(int(book_id), new_status):
            print("Статус книги изменен.")
        else:
            print("Книга не найдена.")

    def list_books(self) -> None:
        """
        Отображает список всех книг в библиотеке.
        Если список книг не пуст, выводит их. В противном случае сообщает,
        что книги отсутствуют.
        """
        books = self.library.list_books()
        if books:
            print("Список всех книг:")
            for book in books:
                print(book)
        else:
            print("Библиотека пуста.")

def main():
    app = ConsoleApp()
    app.run()

if __name__ == "__main__":
    main()