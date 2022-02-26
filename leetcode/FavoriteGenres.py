userSongs = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}
songGenres = {  
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"], 
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

# userSongs = {  
#    "David": ["song1", "song2"],
#    "Emma":  ["song3", "song4"]
# }
# songGenres = {}

output = dict()
for i in userSongs:
    output[i] = []
    for j in songGenres:
        common_songs = len(set(userSongs[i]).intersection(set(songGenres[j])))
        if len(songGenres[j]) == common_songs  and common_songs>1:
            output[i].append(j)