import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==============================
# 1. Load Dataset
# ==============================

movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

print("Movies Dataset Loaded")
print("Total Movies:", len(movies))

print("\nSample Movies:")
print(movies.head())


# ==============================
# 2. Data Preprocessing
# ==============================

# Check missing values
movies["genres"] = movies["genres"].fillna("")

# Combine movie title and genres
movies["features"] = movies["title"] + " " + movies["genres"]

print("\nData Preprocessing Completed")


# ==============================
# 3. Convert Text into Numbers
# ==============================

tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(movies["features"])

print("Text converted into numerical vectors")
print("Matrix Shape:", tfidf_matrix.shape)


# ==============================
# 4. Calculate Similarity
# ==============================

similarity = cosine_similarity(tfidf_matrix)

print("Similarity Calculation Completed")


# ==============================
# 5. Movie Recommendation Function
# ==============================

def recommend_movies(movie_name, number_of_recommendations=5):

    # Convert movie name to lowercase search
    movie_name = movie_name.lower()

    # Find movie index
    movie_index = movies[
        movies["title"].str.lower().str.contains(movie_name, na=False)
    ].index

    if len(movie_index) == 0:
        print("Movie not found!")
        return

    index = movie_index[0]

    # Get similarity scores
    similarity_scores = list(enumerate(similarity[index]))

    # Sort movies based on similarity
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommended Movies:")

    count = 0

    for movie in similarity_scores[1:]:

        movie_id = movie[0]

        print(
            count + 1,
            ".",
            movies.iloc[movie_id]["title"]
        )

        count += 1

        if count == number_of_recommendations:
            break



# ==============================
# 6. User Input
# ==============================

while True:

    user_movie = input(
        "\nEnter a movie name (type exit to stop): "
    )

    if user_movie.lower() == "exit":
        print("Thank you!")
        break

    recommend_movies(user_movie)