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

