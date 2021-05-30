from ward import test

from repository import BookRepository


@test('test find by author should return list of book')
def _():
    books = [
        {
            'name': 'The gatuk book',
            'author': 'Gatuk'
        },
        {
            'name': 'The Human book',
            'author': 'Human'
        }
    ]

    repository = BookRepository(books)
    actual = repository.find_by_author(name='Gatuk')
    assert 1 == len(actual)
    assert 'Gatuk' == actual[0]['author']
