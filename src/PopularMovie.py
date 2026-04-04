
class User:
    def __init__(self, name, friends, movies):
        self.__name = name
        self.__friends = friends
        self.__moviesList = movies

    def get_name(self):
        return self.__name

    def get_friends(self):
        return self.__friends

    def get_moviesList(self):
        return self.__moviesList


class Movie:
    def __init__(self, title):
        self.title = title


def MostPopularMovieOnNetwork():
    return None