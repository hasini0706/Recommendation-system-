from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def build_content_model(movies):
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(movies['genre'])
    similarity = cosine_similarity(matrix)
    return similarity


def recommend_content(movie_name, movies, similarity):
    idx = movies[movies['movie'] == movie_name].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recs = []
    for i in scores[1:4]:
        recs.append(movies.iloc[i[0]]['movie'])
    return recs
