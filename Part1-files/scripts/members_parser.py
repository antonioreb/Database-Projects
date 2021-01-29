former_members_csv = input("Path to former members csv file:")
active_members_csv = input("Path to active members csv file:")
artist_table = input("Artists table output path:")
artist_band_table = input("Artist_Band association table output path:")

artist_dict = {}

def addArtists(artist_dict, artist_csv):

    band_members = open(artist_csv,"r")

    for line in band_members:
        artist_url = line.split(",")[1].replace('"',"")
        band_url = line.split(",")[0].replace('"',"")

        if artist_url.startswith("http://dbpedia.org/resource/"):

            artist_name = line.split(",")[2].replace('"',"").strip()

            if artist_url not in artist_dict.keys() and "former" in artist_csv:
                artist_dict[artist_url] = [[artist_name],band_url,"False"]
            elif artist_url not in artist_dict.keys() and "former" not in artist_csv:
                artist_dict[artist_url] = [[artist_name],band_url,"True"]
            elif artist_url in artist_dict and artist_name not in artist_dict[artist_url][0]:
                artist_dict[artist_url][0].append(artist_name)

    band_members.close()


def writeArtistCsv(artist_dict, output_path):

    artist_csv = open(output_path, "w")

    artist_csv.write("Artist_URL,Artist_Names\n")

    for key in artist_dict.keys():
        output_line = key + "," + '{%s}' % str(artist_dict[key][0]).strip('[]') + "\n"
        artist_csv.write(output_line)

    artist_csv.close()



def writeBandArtist(artist_dict, output_path):

    artist_band_csv = open(output_path, "w")

    artist_band_csv.write("Band_URL,Artist_URL,isActive\n")

    for key in artist_dict.keys():
        band_url = artist_dict[key][1]
        output_line = band_url + "," + key + "," + artist_dict[key][2] + "\n"

        artist_band_csv.write(output_line)
        artist_band_csv.close
        

if __name__ == '__main__':

    addArtists(artist_dict,
               former_members_csv)

    addArtists(artist_dict,
               active_members_csv)

    writeArtistCsv(artist_dict,
                   artist_table)

    writeBandArtist(artist_dict,
                    artist_band_table)
