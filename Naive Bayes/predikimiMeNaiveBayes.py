# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 21:54:46 2018

@author: ssheh

Testimi i algoritmit te naiveBayes.py
"""
from naiveBayes import naiveBayes

k = naiveBayes(shteguDataBaze = "tabele_shembull.csv", AtributiKlase = "play" )
k.kalkulo_propabilitetin_AtributitKlase()
k.hipoteza = {"outlook":"sunny", "temp":"high", "humidity":"high", "windy":"true"}

k.Kalkulo_propabilitetin_kushtezues(k.hipoteza)
k.klasifiko()