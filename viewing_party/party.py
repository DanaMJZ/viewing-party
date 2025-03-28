movies_dict = {}

user_data = {"watched": [],
            "watchlist" : []}

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    
    movies_dict["title"] = title
    movies_dict["genre"] = genre
    movies_dict["rating"] = rating

    return movies_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):

    for movie_info in user_data["watchlist"]:
        if movie_info["title"] == title:
            user_data["watchlist"].remove(movie_info)
            user_data["watched"].append(movie_info)
    
    return user_data


# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) == 0:
        return 0.0
    
    rating_total = 0
    for movie in user_data["watched"]:
        rating_total += movie["rating"]
    average = rating_total / len(user_data["watched"])
    return average
    
def get_most_watched_genre(user_data):

    if len(user_data["watched"]) == 0.0:
        return None
    genre_count = {}
    for movie in user_data["watched"]:
        watched_genre = movie["genre"]
        if watched_genre not in genre_count:
            genre_count[watched_genre] = 1
        else:
            genre_count[watched_genre] += 1

    most_frequent_genre = None
    top_contender_count = -1 
    for genre, count in genre_count.items():
        if count > top_contender_count:
            top_contender_count = count
            most_frequent_genre = genre
    
    return most_frequent_genre


# ------------- WAVE 3 --------------------

def get_unique_watched(user_data):
    user_movies = set()
    for movie in user_data["watched"]:
        user_movies.add(movie["title"])
    
    friend_movies = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.add(movie["title"])

    if len(user_movies) == 0 or len(friend_movies) == 0:
        return []

    set_of_difference_titles = user_movies.difference(friend_movies)

    result = []
    for title in set_of_difference_titles:
        for movie in user_data["watched"]:
            if title == movie["title"]:
                result.append(movie)
    return result

def get_friends_unique_watched(user_data):
    user_movies = set()
    for movie in user_data["watched"]:
        user_movies.add(movie["title"])
    
    friend_movies = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.add(movie["title"])

    if len(user_movies) == 0 or len(friend_movies) == 0:
        return []

    set_of_difference_titles = friend_movies.difference(user_movies)

    result = []
    result_check_set = set()
    for title in set_of_difference_titles:
        for friend in user_data["friends"]:
            for movie in friend["watched"]:
                if title == movie["title"]:
                    if title not in result_check_set:
                        result.append(movie)
                        result_check_set.add(movie["title"])
    return result

        
# ------------- WAVE 4 --------------------
# failing last test, we need to return empty list if all compatible recommended movies
# us and friends have watched.
# compatible = on streaming service we have access to.

def get_available_recs(user_data):
    rec_movies = []
    rec_movie_set = set()
    friends_list = user_data["friends"].copy()
    for friend in friends_list:
        for movie in friend["watched"]:
            movie_host = movie["host"]
            title = movie["title"]
            
            if movie_host in user_data["subscriptions"]: 
                if title not in rec_movie_set:
                    rec_movies.append(movie)
                    rec_movie_set.add(movie["title"])
            

    my_movies = user_data["watched"]
    my_titles = []
    for movie in user_data["watched"]:
        my_titles.append(movie["title"])
    

    for rec_movie in rec_movies:
        if rec_movie["title"] in my_titles:
            rec_movies.remove(rec_movie)

    return rec_movies



# -----------------------------------------
# ------------- WAVE 5 --------------------
# determain most frequant genre, loop through list of movies
# count how much genre appeared and return genre:key, value:counter.
# save that list as varaible
# create empty list recommended movies
# make copy of friends movie list, loop through it and remove each movie that has a match
# with title we have seen
# loop through list of movie and remove movie that its genre doesnt match with genre variable
# return updated list of recommended movies
# approch duplicates by creating another set to compare sets before adding to the result.

