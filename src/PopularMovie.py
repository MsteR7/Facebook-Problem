from collections import Counter


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
        self.__users = []
        self.__movies = []

    def addUser(self, user: User):
        self.__users.append(user)

    def addMovies(self, movie: Movie):
        self.__movies.append(movie)

    def getMovies(self):
        return self.__movies

    def getMovieById(self, id):
        for index, movie in enumerate(self.__movies):
            if index == id:
                return movie
            
    def getUserById(self, id):
        id = id - 1
        for index, user in enumerate(self.__users):
            if index == id:
                return user

    def getUserByName(self, name):
        for user in self.__users:
            if user.get_name() == name:
                return user

    def getUsers(self):
        return self.__users


def MostPopularMovieOnNetwork(user: User, userVisited: list, plateform: Facebook, isRootCall=True):
    userVisited.append(user.get_name())
    movieCounter = Counter(user.get_moviesList())
    #print(movieCounter)

    for friend in user.get_friends():
        #print(f"Current friend {plateform.getUserById(friend).get_name()}")
        movieCounter.update(plateform.getUserById(friend).get_moviesList())
        if plateform.getUserById(friend).get_name() not in userVisited:
            #print("Not visited yet!")
            #print("Updated")
            #print(movieCounter)
            MostPopularMovieOnNetwork(plateform.getUserById(friend), userVisited, plateform, isRootCall=False)
        continue

    PopularMovie = plateform.getMovieById(movieCounter.most_common(1)[0][0])

    if isRootCall:
        print(f"The most popular on {userVisited[0]}'s network is {PopularMovie.title}")
    return PopularMovie.title