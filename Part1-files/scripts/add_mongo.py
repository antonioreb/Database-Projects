import pymongo
import datetime

# connect to Mongo Atlas DB (replace <user> and <password>)
client = pymongo.MongoClient("mongodb+srv://<user>:<password>@tbd.y2kgd.mongodb.net/TBD?retryWrites=true&w=majority")
db = client.TBD

band_album = open("raw_csv/band-album_data.csv","r")
band_band = open("raw_csv/band-band_name.csv","r")
band_former_member = open("raw_csv/band-former_member-member_name.csv","r")
band_genre = open("raw_csv/band-genre_name.csv","r")
band_member = open("raw_csv/band-member-member_name.csv", "r")

# open a list that will contain one dictionary for each band
bands = []
# open a set of unique band URLS
band_set = set()

# add bands
for line in band_band:
    line = line.split(";")
    band_url = line[0].strip('"\n')
    band_name = line[1].strip('"\n')

    # add new band URL to band set and create a dictionary entry
    if band_url not in band_set:
        dict_data = {
            "url" : band_url,
            "name" : band_name,
            "genres" : list(),
            "albums" : list(),
            "artists" : list()
        }

    bands.append(dict_data)
    band_set.add(band_url)

# add genres
for line in band_genre:
    line = line.split(";")
    band_url = line[0].strip('"')
    band_genre = line[1].strip('"\n')

    # add genre to corresponding band genres list
    for band in bands:
        if band["url"] == band_url:
            band["genres"].append(band_genre)

# add albums
for line in band_album:
    line = line.split(";")
    band_url = line[0].strip('"')

    # transform realease date str into datetime
    year = int(line[2].strip('"').split("/")[2])
    month = int(line[2].strip('"').split("/")[1])
    day = int(line[2].strip('"').split("/")[0])
    date = datetime.datetime(year, month, day)

    # create present album dictionary (clean data)
    album_dict = {
    "album_name" : line[1].strip('"'),
    "release" : date,
    "sales" : int(line[5].strip('"rowspan=\n').replace(" ","").replace(",","").replace(".","")),
    "time" : float(line[4].strip('"\n')),
    "abstract" : line[3].strip('"')
    }

    # add album dictionary to corresponding band albums list
    for band in bands:
        if band["url"] == band_url:
            band["albums"].append(album_dict)

# add former artists
last_band = ""
member_dict = dict()
member_dict["artist_url"] = []

for line in band_former_member:
    line = line.split(";")
    band_url = line[0].strip('"')
    artist_url = line[1].strip('"')
    artist_name = line[2].strip('"\n')

    # if it's the same band and artist as the last row add a new alias to his names list
    if (band_url == last_band) and (artist_url == member_dict["artist_url"]):
        member_dict["names"].append(artist_name)

    # if the artist hasn't appeared in the present band, add a new entry
    else:
        for band in bands:
            if band["url"] == last_band:
                band["artists"].append(member_dict)

        member_dict = {
            "artist_url" : artist_url,
            "names" : [artist_name],
            "is_active" : False
            }

    last_band = band_url

# add active artists
for line in band_member:
    line = line.split(";")
    band_url = line[0].strip('"')
    artist_url = line[1].strip('"')
    artist_name = line[2].strip('"\n')

    # if it's the same band and artist as the last row add a new alias to his names list
    if (band_url == last_band) and (artist_url == member_dict["artist_url"]):
        member_dict["names"].append(artist_name)
    # if the artist hasn't appeared in the present band, add a new entry
    else:
        for band in bands:
            if band["url"] == last_band:
                band["artists"].append(member_dict)

        member_dict = {
            "artist_url" : artist_url,
            "names" : [artist_name],
            "is_active" : True
            }

    last_band = band_url

# insert band dictionaries into MongoDB
for band in bands:
     db.Bands.insert_one(band)
