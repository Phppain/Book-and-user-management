"""main.py"""

from book import Book
from user import User
# Создаем книги
book1 = Book("1984", "George Orwell")
book2 = Book("Brave New World", "Aldous Huxley")
# Создаем пользователей
user1 = User("Alice")
user2 = User("Bob")
# Выводим информацию о книгах и пользователях
print(book1)
print(book2)
print(user1)
print(user2)