# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 18:02:03 2020

@author: Filipa Serrano
"""
#indicate paths for files to open and create
# former_members_csv = input("Path to former members csv file:")
# active_members_csv = input("Path to active members csv file:")
# artist_output= input("Artists table output path:")

former_members_csv = "/home/duartb/Desktop/Masters/TBD/Project/GIT_Project/raw_csv/band-former_member-member_name.csv"
active_members_csv = "/home/duartb/Desktop/Masters/TBD/Project/GIT_Project/raw_csv/band-member-member_name.csv"
artist_output = "/home/duartb/Desktop/Masters/TBD/Project/GIT_Project/new_sets/Artists.csv"

artist_url_list = []


def addArtists(artist_list, artist_csv):
#creates a list with unique artist_urls

    band_members = open(artist_csv,"r")

    for line in band_members:
        artist_url = line.split(";")[1].replace('"',"")

        if artist_url.startswith("http://dbpedia.org/resource/"):

            if artist_url not in artist_list:

                artist_list.append(artist_url)

    band_members.close()


def writeArtistCsv(artist_list, output_path):

    artist_csv = open(output_path, "w")

    artist_csv.write("Artist_ID;Artist_URL\n")
    id = 1

    for artist in artist_list:
        output_line = str(id) + ";" + artist + "\n"
        artist_csv.write(output_line)
        id += 1

    artist_csv.close()



addArtists(artist_url_list, former_members_csv)
addArtists(artist_url_list, active_members_csv)
writeArtistCsv(artist_url_list, artist_output)
