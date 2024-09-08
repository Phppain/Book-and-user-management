"""user.py"""

class User:
    def __init__(self, name: str):
        self.name = name
    
    def __str__(self):
        return f"User's name: {self.name}"
