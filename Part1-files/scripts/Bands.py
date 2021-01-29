#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 23:06:26 2020

@author: marco
"""
import csv

file = open('band-band_name.csv')

band_list = []
index = 1
# create the field names
field_names =  ('band_id','band_url','name')

for line in file:

    line = line.split(';')
    bandurl = line[0].replace('"','')
    bandname = line[1].replace('"','')
    bandname = bandname.replace('\n','')
    if bandurl != "band":
        info = {
                'band_id': index,
                'band_url': bandurl,
                'name': bandname}
        band_list.append(info)

        index += 1
    

with open('Bands.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names, delimiter=';')
    writer.writeheader()
    writer.writerows(band_list)

