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
}
""")

sparql.setReturnFormat(JSON)

results = sparql.query().convert()

Usuario1=["Usuario1"]
Usuario2=["Usuario2"]
Usuario3=["Usuario3"]
Usuario4=["Usuario4"]

lista_videojuegos=["Nombre"]
for result in results["results"]["bindings"]:
  lista_videojuegos=lista_videojuegos+[result["titulo"]["value"]]

import random

Usuario1=["Usuario1"]
Usuario2=["Usuario2"]
Usuario3=["Usuario3"]
Usuario4=["Usuario4"]
Usuario5=["Usuario5"]
Usuario6=["Usuario6"]
Usuario7=["Usuario7"]
Usuario8=["Usuario8"]
Usuario9=["Usuario9"]
Usuario10=["Usuario10"]
n=len(lista_videojuegos)-1
for i in range(n):
    Usuario1.append(secrets.randbelow(0,10))
    Usuario2.append(secrets.randbelow(0, 10))
    Usuario3.append(secrets.randbelow(0, 10))
    Usuario4.append(secrets.randbelow(0, 10))
    Usuario5.append(secrets.randbelow(0, 10))
    Usuario6.append(secrets.randbelow(0, 10))
    Usuario7.append(secrets.randbelow(0, 10))
    Usuario8.append(secrets.randbelow(0, 10))
    Usuario9.append(secrets.randbelow(0, 10))
    Usuario10.append(secrets.randbelow(0, 10))


print(lista_videojuegos)
print(len(lista_videojuegos))
print(len(Usuario1))
print(len(Usuario2))
print(len(Usuario3))
print(len(Usuario4))
print(len(Usuario5))
print(len(Usuario6))
print(len(Usuario7))
print(len(Usuario8))
print(len(Usuario9))
print(len(Usuario10))
lista_def1=lista_videojuegos[1:]
lista_def=[Usuario1,Usuario2,Usuario3,Usuario4,Usuario5,Usuario6,Usuario7,Usuario8,Usuario9,Usuario10]
print(lista_def)
with open('base_original_random.csv', 'w', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(lista_videojuegos)
    writer.writerows(lista_def)

print(lista_def1)

with lzma.open("lista_de_juegos2.pkl", "wb") as f:
    pickle.dump(lista_def1, f)

with lzma.open("header2.pkl", "wb") as f:
    pickle.dump(lista_videojuegos, f)

with lzma.open("body2.pkl", "wb") as f:
    pickle.dump(lista_def, f)

