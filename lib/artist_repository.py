from lib.artist import Artist

class ArtistRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from artists')
        return [Artist(row['id'], row['name'], row['genre']) for row in rows]
    
    def find(self, id):
        rows = self._connection.execute('SELECT * from artists WHERE id = %s', [id])
        row = rows[0]
        return Artist(row['id'], row['name'], row['genre'])

    def create(self, artist):
        self._connection.execute('INSERT INTO artists (name, genre)' \
                                'VALUES (%s, %s)'
                                , [artist.name, artist.genre])
        return None