from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""
When ArtistRepsoitory#all is called
A list of artist objects is returned
"""
def test_all(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)
    assert repository.all() == [
        Artist(1, 'Red Hot Chili Peppers', 'Rock'),
        Artist(2, 'Nirvana', 'Grunge'),
        Artist(3, 'Pearl Jam', 'Grunge')
    ]

"""
When ArtistRepsoitory#create is called
A new artist is added to the list of artist objects
This is reflected when all is called
"""
def test_create(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)
    new_artist = Artist(None, 'Test Artist', 'Test Genre')
    repository.create(new_artist)
    assert repository.all() == [
        Artist(1, 'Red Hot Chili Peppers', 'Rock'),
        Artist(2, 'Nirvana', 'Grunge'),
        Artist(3, 'Pearl Jam', 'Grunge'),
        Artist(4, 'Test Artist', 'Test Genre')
    ]

