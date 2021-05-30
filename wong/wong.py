from model import Book
from loader import load_db
from render import render_table
from repository import BookRepository


def main():
    books = load_db('./book-db.csv')
    repository = BookRepository(books)
    result: list[Book] = repository.find_by_author('Dan')
    render_table(result)


if __name__ == '__main__':
    main()
