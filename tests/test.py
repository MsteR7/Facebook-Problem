import json
from collections import Counter

from src.PopularMovie import MostPopularMovieOnNetwork, User , Movie, Facebook

def CreatePlateform():
        platform = Facebook()
        try:
            with open('tests/BasicTest', 'r') as UserFile:
                Userdata = json.load(UserFile)
        except json.JSONDecodeError as e:
            print("Invalid JSON syntax:", e)
    
        try:
            file = open('tests/MoviesList.txt', 'r')
            for line in file:
                platform.addMovies(Movie((line.strip())))
            file.close()
        except FileNotFoundError:
             print("The file 'MoviesList.txt' was not found.")
        except IOError:
             print("An error occurred while reading the file 'MoviesList.txt'.")

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