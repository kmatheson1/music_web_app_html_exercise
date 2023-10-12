from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When I call AlbumRepository#all albums
I get all the albums in the album table 
"""

def test_all(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, 'Californication',1999, 1),
        Album(2, 'Nevermind', 1991, 2),
        Album(3, 'In Utero', 1993, 2),
        Album(4, 'Ten', 1991, 3),
        Album(5, 'By the Way', 2002, 1)
    ]

"""
When I call AlbumRepository#create albums
A new album is added to list of albums
"""

def test_all(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, 'New Album', 9999, 3)
    repository.create(album)
    assert repository.all() == [
        Album(1, 'Californication',1999, 1),
        Album(2, 'Nevermind', 1991, 2),
        Album(3, 'In Utero', 1993, 2),
        Album(4, 'Ten', 1991, 3),
        Album(5, 'By the Way', 2002, 1),
        Album(6, 'New Album', 9999, 3)
    ]