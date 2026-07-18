# Movie Recommendation System

## Project Description

The Movie Recommendation System is a Machine Learning project that recommends movies to users based on their interests.

This project uses Content-Based Filtering to suggest similar movies by analyzing movie titles and genres. The system uses TF-IDF Vectorization to convert text data into numerical features and Cosine Similarity to measure the similarity between movies.

The main goal of this project is to build an AI-based recommendation system that helps users discover movies similar to their favorite movies.

## Features

- Recommends movies based on user input
- Uses Machine Learning techniques for recommendation
- Implements Content-Based Filtering
- Analyzes movie titles and genres
- Provides top similar movie suggestions
- Interactive movie search system

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
- Machine Learning

## Algorithm Used

Content-Based Filtering

The recommendation system works using the following steps:

1. Load the MovieLens dataset.
2. Extract movie titles and genres.
3. Combine movie information into feature data.
4. Convert text data into numerical vectors using TF-IDF.
5. Calculate similarity between movies using Cosine Similarity.
6. Recommend movies with the highest similarity scores.

## Dataset

MovieLens Small Dataset

The dataset used in this project is the MovieLens Small Dataset provided by GroupLens Research.

The dataset contains:
- Movie information
- Movie genres
- User ratings

Files used:
- movies.csv
- ratings.csv

## Project Structure

Movie-Recommendation-System

- movie_recommender.py
- movies.csv
- ratings.csv
- README.md

## How to Run the Project

Step 1: Install Required Libraries

pip install pandas numpy scikit-learn

Step 2: Run the Python Program

python movie_recommender.py

Step 3: Enter a movie name

Example:

Enter a movie name: Toy Story

Output:

Recommended Movies:

1. Toy Story 2 (1999)
2. Toy Story 3 (2010)
3. A Bug's Life (1998)
4. Monsters, Inc. (2001)
5. Finding Nemo (2003)

## Applications

- Movie recommendation platforms
- Personalized content recommendation
- Entertainment systems
- AI-based recommendation engines

## Future Improvements

- Implement Collaborative Filtering
- Add user-based recommendations
- Improve recommendations using ratings
- Build a web application using Flask or Streamlit
- Deploy the project online

## Author

Jalaka Umadevi

Artificial Intelligence Intern

## Project Information

Project Name: Movie Recommendation System

Domain: Artificial Intelligence and Machine Learning

Technique: Content-Based Filtering

Status: Completed

## Acknowledgement

Thanks to GroupLens Research for providing the MovieLens dataset used in this project.
