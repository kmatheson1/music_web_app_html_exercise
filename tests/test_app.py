from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    list_tags = page.locator("li")
    expect(list_tags).to_have_text([
        "Californication",
        "Nevermind",
        "In Utero",
        "Ten",
        "By the Way"
    ])

def test_get_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    release_year_tag = page.locator(".t-release-year")
    h1_tags = page.locator("h1")
    expect(h1_tags).to_have_text("Album: Californication")
    expect(release_year_tag).to_have_text("Released: 1999")

"""
The page returned by GET /albums should contain a link for each album listed. It should link to /albums/<id>, where <id> is the corresponding album's id. That page should then show information about the specific album.
"""
def test_visit_album_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Californication'")
    h1_tag = page.locator("h1")
    release_year_tag = page.locator(".t-release-year")
    expect(h1_tag).to_have_text("Album: Californication")
    expect(release_year_tag).to_have_text("Released: 1999")

def test_visit_album_show_page_and_go_back(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Californication'")
    page.click("text='Go back to album list'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Albums")

def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/artists")
    list_tags = page.locator("li")
    expect(list_tags).to_have_text([
        "Red Hot Chili Peppers",
        "Nirvana",
        "Pearl Jam",
    ])

def test_get_artist_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Red Hot Chili Peppers'")
    h1_tag = page.locator("h1")
    genre_tag = page.locator(".t-genre")
    expect(h1_tag).to_have_text("Artist: Red Hot Chili Peppers")
    expect(genre_tag).to_have_text("Genre: Rock")

def test_visit_album_show_page_and_go_back(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Red Hot Chili Peppers'")
    page.click("text='Go back to artist list'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Artists")

def test_create_album(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add a new album'")

    page.fill("input[name='title']", "Test Album")
    page.fill("input[name='release_year']", "9999")
    page.click('text ="Add album"')

    h1_tag = page.locator("h1")
    release_year_tag = page.locator(".t-release-year")
    expect(h1_tag).to_have_text("Album: Test Album")
    expect(release_year_tag).to_have_text("Released: 9999")

def test_validate_album(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click('text="Add a new album"')
    page.click('text="Add album"')

    errors_tag = page.locator(".t-errors")
    expect(errors_tag).to_have_text(
        "Your submission contains errors: " \
        "Title must not be blank, " \
        "Release year must be a number"
    )

def test_create_artist(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Add a new artist'")

    page.fill("input[name='name']", "Test Artist")
    page.fill("input[name='genre']", "Test Genre")
    page.click('text ="Add artist"')

    h1_tag = page.locator("h1")
    release_year_tag = page.locator(".t-genre")
    expect(h1_tag).to_have_text("Artist: Test Artist")
    expect(release_year_tag).to_have_text("Genre: Test Genre")

def test_validate_album(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click('text="Add a new artist"')
    page.click('text="Add artist"')

    errors_tag = page.locator(".t-errors")
    expect(errors_tag).to_have_text(
        "Your submission contains errors: " \
        "Name must not be blank, " \
        "Genre must not be blank"
    )