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
    # remove from watch list and add to watched
    # loop over user data watch list array
    # check each dictionary in array if they have the title we have
    for movie_info in user_data["watchlist"]:
        if movie_info["title"] == title:
            user_data["watchlist"].remove(movie_info)
            user_data["watched"].append(movie_info)
    
    return user_data

#def watch_movie(user_data, title):
# Look through each movie in the watchlist
#    for movie in user_data["watchlist"]:
#       if movie["title"] == title:
#            # When found, remove from watchlist and add to watched
#            user_data["watchlist"].remove(movie)
#            user_data["watched"].append(movie)
#            # Return immediately since we're done
#            return user_data
#    
# If movie wasn't found, return original data
#    return user_data

# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) == 0:
        return 0.0
    
    rating_total = 0
    for movie in user_data["watched"]:
        rating_total += movie["rating"]
    average = rating_total / len(user_data["watched"])
    return average
    
def most_watched_genre(user_data):
    if len(user_data["watched"]) == None:
        return None
    genre_count = {}
    for movie in user_data["watched"]:
        watched_genre = movie["genre"]
        if watched_genre not in genre_count:
            genre_count[watched_genre] = 1
        else:
            genre_count[watched_genre] += 1





#   if len movie("watchlist") = 0
#return 0.0
# for movie in watchedlist we need to add movie ratings
# avr = total movies/ len of watched list
# return avr

# ------------- WAVE 3 --------------------

def get_unique_watched(user_data):
    pass

def get_friends_unique_watched(user_data):
    pass
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

