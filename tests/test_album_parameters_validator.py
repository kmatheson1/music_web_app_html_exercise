from lib.album_parameters_validator import AlbumParametersValidator
import pytest

def test_is_valid():
    validator = AlbumParametersValidator("My Title", "9999")
    assert validator.is_valid() == True

def test_is_not_valid_with_bad_title():
    validator_1 = AlbumParametersValidator("", "9999")
    assert validator_1.is_valid() == False
    validator_2 = AlbumParametersValidator(None, "9999")
    assert validator_2.is_valid() == False

def test_is_not_valid_with_non_int_release_year():
    validator_1 = AlbumParametersValidator("My Title", "")
    assert validator_1.is_valid() == False
    validator_2 = AlbumParametersValidator("My Title", None)
    assert validator_2.is_valid() == False
    validator_3 = AlbumParametersValidator("My Title", "word")
    assert validator_3.is_valid() == False

def test_errors():
    validator_1 = AlbumParametersValidator("", "")
    assert validator_1.generate_errors() == [
        "Title must not be blank",
        "Release year must be a number"
    ]
    validator_2 = AlbumParametersValidator("title", "")
    assert validator_2.generate_errors() == ["Release year must be a number"]
    validator_3 = AlbumParametersValidator("", "9999")
    assert validator_3.generate_errors() == ["Title must not be blank"]

def test_get_valid_title_if_title_valid():
    validator_1 = AlbumParametersValidator("My Title", "1990")
    assert validator_1.get_valid_title() == "My Title"

def test_get_valid_title_refuses_if_title_invalid():
    validator_1 = AlbumParametersValidator("", "1990")
    with pytest.raises(ValueError) as e:
        validator_1.get_valid_title()
    assert str(e.value) == "Cannot get valid title"

def test_get_valid_year_if_year_valid():
    validator_1 = AlbumParametersValidator("My Title", "1990")
    assert validator_1.get_valid_year() == "1990"

def test_get_valid_year_refuses_if_year_invalid():
    validator_1 = AlbumParametersValidator("My Title", "word")
    with pytest.raises(ValueError) as e:
        validator_1.get_valid_year()
    assert str(e.value) == "Cannot get valid release year"