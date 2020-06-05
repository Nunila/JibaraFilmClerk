# Jíbara Film Clerk will send daily emails containing a movie recommendation based on the user's desired genres.
# This will work only locally and will be hard-coded to only fit my favorite movie genres.
# Movie Genres I prefer: Thriller, Horror, Sci-fi

# Movie Db used: TMDb APIs
# This product uses the TMDb API but is not endorsed or certified by TMDb.
# Found at: https://www.themoviedb.org/

from src.recommendation_methods import MovieRecommendation

if __name__ == '__main__':
    MovieRecommendation().get_movie_recommendation()

