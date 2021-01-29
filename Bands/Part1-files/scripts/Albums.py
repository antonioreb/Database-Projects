#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 23:06:26 2020

@author: marco
"""
import csv
from csv import reader
band_open = open('Bands.csv')
albums = open('band-album_data.csv')
band_read = reader(band_open, delimiter=';')
bands = list(band_read)


album_list=[]
# create the field names
field_names =  ('band_id','name','release','sales','time','abstract')

for line in albums:
    line = line.split(';')
    band_url = line[0]
    album_name = line[1]
    release = line[2]
    abstract = line[3]
    time = line[4]
    sales = line[5] 

    for band in bands:
        if band[1] == band_url:
            band_id = band[0]

    info = {
            'band_id': band_id,
            'name': album_name,
            'release': release,
            'sales': sales,
            'time': time,
            'abstract': abstract}
    album_list.append(info)
    

    

with open('Albums.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names, delimiter=';')
    writer.writeheader()
    writer.writerows(album_list)

