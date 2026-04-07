import json
from collections import Counter

from src.PopularMovie import MostPopularMovieOnNetwork, User , Movie, Facebook

def CreatePlateform():
        platform = Facebook()
        with open('tests/BasicTest', 'r') as UserFile:
            Userdata = json.load(UserFile)

        file = open('tests/MoviesList.txt', 'r')
        for line in file:
            platform.addMovies(Movie((line.strip())))
        file.close()

        for key, value in Userdata.items():
            platform.addUser(User(key,value['friends'], value['movies']))

        return platform



def test_popularMovie():
    mockDatabase = CreatePlateform()
    assert MostPopularMovieOnNetwork(mockDatabase.getUserById(1), [], mockDatabase, isRootCall=True) == "Mafioso"
    assert MostPopularMovieOnNetwork(mockDatabase.getUserById(2), [], mockDatabase, isRootCall=True) == "Spotlight"
    assert MostPopularMovieOnNetwork(mockDatabase.getUserById(5), [], mockDatabase, isRootCall=True) == "Psycho"
    print('Test Succeed')


if __name__ == '__main__':
    test_popularMovie()