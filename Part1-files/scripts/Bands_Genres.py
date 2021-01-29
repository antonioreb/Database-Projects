#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 00:10:39 2020

@author: marco
"""

import csv
from csv import reader
band_open = open('/home/duartb/Desktop/Masters/TBD/Project/GIT_Project/new_sets/Bands.csv')
genre_open = open('/home/duartb/Desktop/Masters/TBD/Project/GIT_Project/new_sets/Genres.csv')
bg_open = open('/home/duartb/Desktop/Masters/TBD/Project/GIT_Project/raw_csv/band-genre_name.csv')
band_read = reader(band_open, delimiter=';')
genre_read = reader(genre_open, delimiter=';')
bands = list(band_read)
genres = list(genre_read)

bg_list = []
# create the field names
field_names =  ('band_id','genre_id')

for line in bg_open:
    line = line.split(';')
    band_url = line[0].replace('"','')
    genre_name = line[1].replace('"','').strip()

    for band in bands:
        if band[1] == band_url:
            band_id = band[0]
    for genre in genres:
        if genre[1] == genre_name:
            genre_id = genre[0]

    info = {
            'band_id': band_id,
            'genre_id': genre_id}
    bg_list.append(info)




with open('Bands_Genres.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names, delimiter=';')
    writer.writeheader()
    writer.writerows(bg_list)
