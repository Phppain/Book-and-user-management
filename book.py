"""book.py"""

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"Title: {self.title} –– Author: {self.author}"
