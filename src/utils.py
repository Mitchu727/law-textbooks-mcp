from pathlib import Path

def get_root_path():
    return Path(__file__).parent.parent

def get_books_path():
    return get_root_path() / 'books'