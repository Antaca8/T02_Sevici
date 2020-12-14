# -*- coding: utf-8 -*-
'''
Created on 4 nov. 2020

@author: anton
'''
import csv
from coordenadas import *
from collections import namedtuple

Estacion = namedtuple('Estacion', 'name slots empty_slots free_bikes coordenada')
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
            tupla_coord = Coordenada(latitude, longitude)
            estaciones.append(Estacion(name, slots, empty_slots, free_bikes, tupla_coord))
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
            tupla_coord = Coordenada(latitude, longitude)
            tupla = Estacion(name, slots, empty_slots, free_bikes, tupla_coord)
            estaciones.append(tupla)
    return estaciones

def estaciones_bicis_libres(estaciones, k=5):
    lista_res =[]
    for t_estacion in estaciones:
        if t_estacion.free_bikes >= k:
            lista_res.append((t_estacion.free_bikes, t_estacion.name))
    
    lista_res = sorted(lista_res)      
    return lista_res

def ubicacion_estaciones(estaciones):
    lista = []
    for name, _, _, _, coordenadas in estaciones:
        lista.append(name, coordenadas)
    return lista