"""
    This module will lets user to iterate through the list
    which have inbuilt list
"""

def printMoviesList(movies):
    for nested_movie in movies:
        if isinstance(nested_movie,list):
            printMoviesList(nested_movie)
        else:
            print nested_movie
