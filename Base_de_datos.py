import numpy as np
import secrets
import pandas as pd
import streamlit as st
from SPARQLWrapper import SPARQLWrapper, JSON, DIGEST, POST
import csv
import lzma
import dill as pickle


sparql = SPARQLWrapper("https://query.wikidata.org/sparql")

sparql.setQuery("""
prefix wdt: <https://www.wikidata.org/prop/direct/>
prefix wd: <https://www.wikidata.org/entity/>

SELECT DISTINCT ?titulo
WHERE 
{
      ?videojuego wdt:P31 wd:Q7889.
      ?videojuego rdfs:label ?titulo
      FILTER(LANG(?titulo) = "en").
      ?videojuego wdt:P577 ?fecha
      FILTER("2010-01-01"^^xsd:dateTime < ?fecha).
      ?videojuego wdt:P2664 ?ventas
      FILTER(10000000 < ?ventas).
}LIMIT 10
""")

sparql.setReturnFormat(JSON)

results = sparql.query().convert()

lista_videojuegos=["Nombre"]
for result in results["results"]["bindings"]:
  lista_videojuegos=lista_videojuegos+[result["titulo"]["value"]]

import random

rand_list=[]
n=10
for i in range(n):
    rand_list.append(secrets.choice(3,9))
print(rand_list)

print(lista_videojuegos)

Usuario1=["Andres",7,0,0,8,0,0,7,9,8,10]
Usuario2=["Johan",3,4,5,0,0,1,10,0,9,0]
Usuario3=["Eladio",5,1,6,5,0,1,5,7,0,10]
Usuario4=["Hernan",7,9,2,4,5,6,7,4,3,2]
print(len(Usuario1))
print(len(Usuario2))
print(len(Usuario3))
print(len(Usuario4))

lista_def1=lista_videojuegos[1:]
lista_def=[Usuario1,Usuario2,Usuario3,Usuario4]
print(lista_def)
with open('base_original.csv', 'w', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(lista_videojuegos)
    writer.writerows(lista_def)

print(lista_def1)

with lzma.open("lista_de_juegos.pkl", "wb") as f:
    pickle.dump(lista_def1, f)

with lzma.open("header.pkl", "wb") as f:
    pickle.dump(lista_videojuegos, f)

with lzma.open("body.pkl", "wb") as f:
    pickle.dump(lista_def, f)

