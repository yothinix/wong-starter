from rich.console import Console
from rich.table import Table

from model import Book


def render_table(books: list[Book]) -> None:
    table = Table(title="Kamar Tarj Library")

    table.add_column('Name', justify='right', style='cyan')
    table.add_column('Author', justify='right', style='red')

    for book in books:
        table.add_row(book['name'], book['author'])    
    
    console = Console()
    console.print(table)
