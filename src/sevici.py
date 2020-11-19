# -*- coding: utf-8 -*-
'''
Created on 4 nov. 2020

@author: anton
'''
import csv

def lee_estaciones (fichero):
    estaciones = []
    with open (fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for name, slots, empty_slots, free_bikes, latitude, longitude in lector:
            slots = int(slots)
            empty_slots = int(empty_slots)
            free_bikes = int(free_bikes)
            latitude = float(latitude)
            longitude = float(longitude)
            estaciones.append((name, slots, empty_slots, free_bikes, latitude, longitude))
    return estaciones

def lee_estaciones2 (fichero):
    estaciones = []
    with open (fichero, encoding = 'utf-8') as f:
        lector = csv.DictReader(f)
        next(lector)
        for registro in lector:
            name = registro['name']
            slots = int(registro['slots'])
            empty_slots = int(registro['empty_slots'])
            free_bikes = int(registro['free_bikes'])
            latitude = float(registro['latitude'])
            longitude = float(registro['longitude'])
            tupla = (name, slots, empty_slots, free_bikes, latitude, longitude)
            estaciones.append(tupla)
    return estaciones