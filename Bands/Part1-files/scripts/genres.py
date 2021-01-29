genres_csv = open("/home/duartb/Desktop/Masters/TBD/Project/GIT_Project/raw_csv/band-genre_name.csv","r")
genres_out = open("/home/duartb/Desktop/Masters/TBD/Project/GIT_Project/new_sets/Genres.csv","w")

id = 1
genres = set()

for line in genres_csv:
    line = line.replace('"','').split(";")
    genres.add(line[1])

for genre in genres:
    out = str(id) + ";" + genre
    genres_out.write(out)
    id += 1
