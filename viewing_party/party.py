movies_dict = {}

user_data = {"watched": [],
            "watchlist" : []}

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title or genre or rating is False:
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
    if title not in user_data["watchlist"]:
        return user_data
    
    for movie in user_data["watchlist"]:
        if title in user_data["watchlist"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
        
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

