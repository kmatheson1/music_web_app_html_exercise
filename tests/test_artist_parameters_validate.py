from lib.artist_parameters_validator import ArtistParametersValidator
import pytest

def test_is_valid():
    validator = ArtistParametersValidator("Name", "Genre")
    assert validator.is_valid() == True

def test_is_not_valid_with_bad_name():
    validator_1 = ArtistParametersValidator("", "Genre")
    assert validator_1.is_valid() == False
    validator_2 = ArtistParametersValidator(None, "Genre")
    assert validator_2.is_valid() == False

def test_is_not_valid_with_non_int_release_year():
    validator_1 = ArtistParametersValidator("My Name", "")
    assert validator_1.is_valid() == False
    validator_2 = ArtistParametersValidator("My Name", None)
    assert validator_2.is_valid() == False

def test_errors():
    validator_1 = ArtistParametersValidator("", "")
    assert validator_1.generate_errors() == [
        "Name must not be blank",
        "Genre must not be blank"
    ]
    validator_2 = ArtistParametersValidator("", "genre")
    assert validator_2.generate_errors() == ["Name must not be blank"]
    validator_3 = ArtistParametersValidator("name", "")
    assert validator_3.generate_errors() == ["Genre must not be blank"]

def test_get_valid_name_if_name_valid():
    validator_1 = ArtistParametersValidator("My Title", "1990")
    assert validator_1.get_valid_name() == "My Title"

def test_get_valid_title_refuses_if_title_invalid():
    validator_1 = ArtistParametersValidator("", "genre")
    with pytest.raises(ValueError) as e:
        validator_1.get_valid_name()
    assert str(e.value) == "Cannot get valid name"

def test_get_valid_genre_if_genre_valid():
    validator_1 = ArtistParametersValidator("Name", "Genre")
    assert validator_1.get_valid_genre() == "Genre"

def test_get_valid_year_refuses_if_year_invalid():
    validator_1 = ArtistParametersValidator("Name", "")
    with pytest.raises(ValueError) as e:
        validator_1.get_valid_genre()
    assert str(e.value) == "Cannot get valid genre"
