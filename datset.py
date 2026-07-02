import pandas as pd

def get_movies():
    movies = pd.DataFrame({
        'movie': [
            'Avengers', 'Iron Man', 'Titanic',
            'Interstellar', 'Gravity', 'Notebook'
        ],
        'genre': [
            'action superhero sci-fi',
            'action superhero tech',
            'romance drama love',
            'sci-fi space adventure',
            'sci-fi space survival',
            'romance drama love'
        ]
    })
    return movies


def get_ratings():
    ratings = pd.DataFrame({
        'user': ['U1','U1','U2','U2','U3','U3','U4','U4'],
        'movie': ['Avengers','Titanic','Avengers','Gravity','Titanic','Interstellar','Gravity','Notebook'],
        'rating': [5,3,4,2,5,5,5,4]
    })
    return ratings
