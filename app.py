import streamlit as st

st.title("🎬 Movie Recommendation System (Hybrid AI)")

# -----------------------
# SAMPLE DATA
# -----------------------
movies = ["Avengers", "Iron Man", "Titanic", "Interstellar", "Gravity", "Notebook"]

content_recommendations = {
    "Avengers": ["Iron Man", "Interstellar"],
    "Iron Man": ["Avengers", "Gravity"],
    "Titanic": ["Notebook"],
    "Interstellar": ["Gravity", "Avengers"],
    "Gravity": ["Interstellar"],
    "Notebook": ["Titanic"]
}

collab_recommendations = {
    "U1": ["Interstellar", "Gravity"],
    "U2": ["Avengers", "Titanic"],
    "U3": ["Gravity", "Notebook"],
    "U4": ["Interstellar", "Avengers"]
}

# -----------------------
# USER INPUT
# -----------------------
user = st.selectbox("Select User", ["U1", "U2", "U3", "U4"])
movie = st.selectbox("Select Movie", movies)

# -----------------------
# HYBRID LOGIC
# -----------------------
def hybrid(user, movie):
    content = content_recommendations.get(movie, [])
    collab = collab_recommendations.get(user, [])

    # combine both and remove duplicates
    result = list(set(content + collab))
    return result

# -----------------------
# BUTTON ACTION
# -----------------------
if st.button("Recommend"):
    results = hybrid(user, movie)

    st.subheader("🎯 Recommended Movies:")
    if results:
        for r in results:
            st.write("👉", r)
    else:
        st.write("No recommendations found")