from lib.album import Album

def test_album_constructs():
    album = Album(1, "test title", 9999, 2)
    assert album.id == 1
    assert album.title == 'test title'
    assert album.release_year == 9999
    assert album.artist_id == 2

def test_equality():
    album1 = Album(1, "test title", 9999, 2)
    album2 = Album(1, "test title", 9999, 2)
    assert album1 == album2

def test_format():
    album = Album(1, "test title", 9999, 2)
    assert str(album) == "Album(1, test title, 9999, 2)"