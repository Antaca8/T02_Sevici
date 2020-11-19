# -*- coding: utf-8 -*-
'''
Created on 4 nov. 2020

@author: anton
'''
from sevici import *

def test_lee_estaciones():
    mostrar = lee_estaciones("../data/estaciones.csv")
    print(mostrar)
    
if __name__ == '__main__':
    ESTACIONES = lee_estaciones("../data/estaciones.csv")
    test_lee_estaciones()
    
