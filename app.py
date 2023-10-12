import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("albums/index.html", albums=albums)

@app.route('/albums/<id>')
def get_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    return render_template("albums/album.html", album=album)



# @app.route('/albums', methods=['POST'])
# def post_album():
#     if has_invalid_album_parameters(request.form):
#         return 'Title, release_year, artist_id must be submitted', 400
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     album = Album(
#         None,
#         request.form['title'],
#         request.form['release_year'],
#         request.form['artist_id']
#     )
#     repository.create(album)
#     return '', 200


# @app.route('/artists')
# def get_artists():
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     artists = repository.all()
#     return ', '.join(f'{artist.name}' for artist in artists), 200

# @app.route('/artists', methods=['POST'])
# def post_artists():
#     if has_invalid_artist_parameters(request.form):
#         return 'Name, Genre must be submitted', 400
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     artist = Artist(
#         None,
#         request.form['name'],
#         request.form['genre']
#     )
#     repository.create(artist)
#     return '', 200

# def has_invalid_album_parameters(form):
#     return 'title' not in form or \
#         'release_year' not in form or \
#         'artist_id' not in form

# def has_invalid_artist_parameters(form):
#     return 'name' not in form or \
#         'genre' not in form


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
