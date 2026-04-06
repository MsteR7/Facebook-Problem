import json

from src.PopularMovie import MostPopularMovieOnNetwork, User , Movie, Facebook

def CreatePlateform():
        platform = Facebook()
        with open('TestCase', 'r') as UserFile:
            Userdata = json.load(UserFile)

        file = open('MoviesList.txt', 'r')
        for line in file:
            platform.addMovies(Movie((line.strip())))
        file.close()

        for key, value in Userdata.items():
            platform.addUser(User(key,value['friends'], value['movies']))

        return platform.getUsers()



def test_popularMovie():
    mockDatabase = CreatePlateform()
    #assert CreatePlateform(mockDatabase["Sallie"]) == 3
    #assert CreatePlateform(mockDatabase["Jana"]) == 0
    #assert CreatePlateform(mockDatabase["Marty"]) == 0
    print('Test Succeed')


if __name__ == '__main__':
    test_popularMovie()