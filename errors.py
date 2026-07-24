NOT_MOVIE= "unset movie"

class Error_name_not_set(Exception):
    def __init__(self, msg= "unset movie name"):
        self.messg= msg
        super().__init__(self.messg)

class Error_movie_unnspecific(Exception):
    def __init__(self, msg= "name refers to multiple movies"):
        self.messg= msg
        super().__init__(self.messg)

class Error_invalid_name(Exception):
    def __init__(self, mssg= "invalid movie title"):
        self.mssg= mssg
        super().__init__(self.mssg)