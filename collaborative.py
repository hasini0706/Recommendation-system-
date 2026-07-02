import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def build_user_matrix(ratings):
    return ratings.pivot_table(index='user', columns='movie', values='rating').fillna(0)


def get_user_similarity(matrix):
    return cosine_similarity(matrix)


def recommend_collab(user, ratings, matrix, sim):
    users = list(matrix.index)
    idx = users.index(user)

    sim_scores = list(enumerate(sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:]

    watched = set(ratings[ratings['user'] == user]['movie'])

    rec = {}

    for i, score in sim_scores:
        similar_user = users[i]
        user_movies = ratings[ratings['user'] == similar_user]

        for _, row in user_movies.iterrows():
            if row['movie'] not in watched:
                rec[row['movie']] = rec.get(row['movie'], 0) + score * row['rating']

    return sorted(rec, key=rec.get, reverse=True)[:3]
