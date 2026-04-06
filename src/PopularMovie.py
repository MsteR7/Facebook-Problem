
class User:
    def __init__(self, name, friends, movies):
        self.__name = name
        self.__friendsList = friends
        self.__moviesList = movies

    def get_name(self):
        return self.__name

    def get_friends(self):
        return self.__friendsList

    def get_moviesList(self):
        return self.__moviesList

    def displayFriends(self):
        for friend in self.__friendsList:
            print(friend)


class Movie:
    def __init__(self, title):
        self.title = title



class Facebook:
    def __init__(self):
        self.__users = {}
        self.__movies = []

    def addUser(self, user: User):
        self.__users[user.get_name()] = [user.get_friends(), user.get_moviesList()]

    def addMovies(self, movie: Movie):
        self.__movies.append(movie.title)

    def getMovies(self):
        return self.__movies

    def getMovieById(self, id):
        id -= 1
        for index, movie in enumerate(self.__movies):
            if index == id:
                return movie


    def getUsers(self):
        return self.__users


def MostPopularMovieOnNetwork(user):
    return "None"