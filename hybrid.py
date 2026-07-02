from content_based import recommend_content
from collaborative import recommend_collab

def hybrid_recommend(user, movie, movies, ratings, content_sim, user_matrix, user_sim):

    content_recs = recommend_content(movie, movies, content_sim)
    collab_recs = recommend_collab(user, ratings, user_matrix, user_sim)

    # Combine both (weighted)
    final = list(set(content_recs + collab_recs))

    return final[:5]
