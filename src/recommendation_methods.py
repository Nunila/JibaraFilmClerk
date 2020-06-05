import os
from os.path import normpath, join
import requests
import urllib.parse as urlparse
from random import randint

# TMDb returns results as only one page. To select a movie, I will randomize the page # and then select a random entry


class MovieRecommendation:

    def get_movie_recommendation(self):

        # Make request
        main_url = "https://api.themoviedb.org/3/discover/movie"
        params = self.create_params_object()

        url_parse = urlparse.urlparse(main_url)
        query = url_parse.query
        url_dict = dict(urlparse.parse_qsl(query))
        url_dict.update(params)
        url_new_query = urlparse.urlencode(url_dict)
        url_parse = url_parse._replace(query=url_new_query)
        full_url = urlparse.urlunparse(url_parse)

        result_index = randint(0, 20)
        r = requests.get(url=full_url, )
        data = r.json()
        movie_result = data['results'][result_index]

        print(movie_result)
        self.generate_email(movie_result)

    def create_params_object(self):
        # Read API Key from local file
        path = normpath(join(os.getcwd(), "../CredsInfo/TMDbInfo.txt"))
        f = open(path, "r")
        line = ""
        while "V3 API" not in line:
            line = f.readline()
        api_key = line.split(":")[1].strip()
        f.close()

        # Generate random num for page # and result index
        page_number = randint(0, 500)
        params = {'api_key': api_key,
                  'language': 'en-US',
                  'sort_by': 'popularity.desc',
                  'include_adult': True,
                  'include_video': False,
                  'page': page_number,
                  'vote_average.gte': 5,
                  'with_genres': '27|9648|878|53',
                  }
        return params

    def generate_email(self, movie_result):

        # Get url of movie poster
        base_image_path = "http://image.tmdb.org/t/p/"
        poster_size = "w342"  # w185
        complete_image_path = base_image_path + poster_size + movie_result['poster_path']
        print("Poster path ", complete_image_path)
