
class AlbumParametersValidator():
    def __init__(self, title, release_year):
        self.title = title
        self.release_year = release_year

    def is_valid(self):
        return self._is_title_valid() and self._is_release_year_valid()
    
    def generate_errors(self):
        errors = []
        if not self._is_title_valid():
            errors.append("Title must not be blank")
        if not self._is_release_year_valid():
            errors.append("Release year must be a number")
        return errors
    
    def get_valid_title(self):
        if not self._is_title_valid():
            raise ValueError("Cannot get valid title")
        return self.title
    
    def get_valid_year(self):
        if not self._is_release_year_valid():
            raise ValueError("Cannot get valid release year")
        return self.release_year

    def _is_title_valid(self):
        if self.title is None:
            return False
        if self.title == "":
            return False
        return True
    
    def _is_release_year_valid(self):
        if self.release_year is None:
            return False
        if not self.release_year.isdigit():
            return False
        return True