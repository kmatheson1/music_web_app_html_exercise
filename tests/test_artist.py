from lib.artist import Artist

def test_artist_constructs():
    artist = Artist(1, "test artist", "test genre")
    assert artist.id == 1
    assert artist.name == "test artist"
    assert artist.genre == "test genre"

def test_equality():
    artist1 = Artist(1, "test artist", "test genre")
    artist2 = Artist(1, "test artist", "test genre")
    assert artist1 == artist2

def test_formats():
    artist = Artist(1, "test artist", "test genre")
    assert str(artist) == "Artist(1, test artist, test genre)"