# -*- coding: utf-8 -*-
'''
Created on 4 nov. 2020

@author: anton
'''
from sevici import *

def test_lee_estaciones():
    print(ESTACIONES[:3])
    
def test_estaciones_bicis_libres():
    estaciones_libres = estaciones_bicis_libres(ESTACIONES, 10)
    print(estaciones_libres[:3])

def test_ubicacion_estaciones():
    print(ubicacion_estaciones(ESTACIONES))

if __name__ == '__main__':
    ESTACIONES = lee_estaciones("../data/estaciones.csv")
    #test_lee_estaciones()
    #test_estaciones_bicis_libres()
    test_ubicacion_estaciones()