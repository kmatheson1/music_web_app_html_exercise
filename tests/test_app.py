from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    div_tags = page.locator("div")
    
    expect(div_tags).to_have_text([
        "Title: Californication\nReleased: 1999",
        "Title: Nevermind\nReleased: 1991",
        "Title: In Utero\nReleased: 1993",
        "Title: Ten\nReleased: 1991",
        "Title: By the Way\nReleased: 2002"
    ])
