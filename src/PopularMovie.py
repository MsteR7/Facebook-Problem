
class User:
    def __init__(self, name, friends, movies):
        self.__id
        self.__name = name
        self.__friends = []
        self.__moviesList = []

    def get_name(self):
        return self.__name

    def get_friends(self):
        return self.__friends

    def get_moviesList(self):
        return self.__moviesList

    def set_userId(self, id):
        self.__id = id

    def displayFriends(self):
        for friend in self.__friends:
            print(friend)


class Movie:
    def __init__(self, title):
        self.__id
        self.title = title

    def set_movieId(self, id):
        self.__id = id


class Facebook:
    def __init__(self):
        self.__users = []
        self.__movies = []

    def addUser(self, user: User):
        self.users.append(user)

    def addMovies(self, movie: Movie):
        self.movies.append(movie)

    def getMovies(self):
        return self.movies

    def getUsers(self):
        return self.users


def MostPopularMovieOnNetwork():
    return None