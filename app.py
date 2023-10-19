import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album
from lib.artist import Artist
from lib.album_parameters_validator import AlbumParametersValidator
from lib.artist_parameters_validator import ArtistParametersValidator

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

@app.route('/artists')
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template("artists/index.html", artists=artists)

@app.route('/artists/<id>')
def get_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.find(id)
    return render_template("artists/artist.html", artist=artist)

@app.route('/albums/new')
def get_album_new():
    return render_template("albums/new.html")

@app.route('/albums', methods=["POST"])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    validator = AlbumParametersValidator(
        request.form['title'],
        request.form['release_year']
    )

    if not validator.is_valid():
        errors = validator.generate_errors()
        return render_template("albums/new.html", errors=errors)
    
    album = Album(
        None,
        validator.get_valid_title(),
        validator.get_valid_year(),
        1)

    repository.create(album)
    return redirect(f'/albums/{album.id}')

@app.route('/artists/new')
def get_artist_new():
    return render_template("artists/new.html")

@app.route('/artists', methods=['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    validator = ArtistParametersValidator(
        request.form['name'],
        request.form['genre']
    )

    if not validator.is_valid():
        errors = validator.generate_errors()
        return render_template("artists/new.html", errors=errors)
    
    artist = Artist(
        None,
        validator.get_valid_name(),
        validator.get_valid_genre())

    repository.create(artist)
    return redirect(f'/artists/{artist.id}')

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
