#importamos dependencias para hacer más fácil el manejo de datos
import numpy as np
import pandas as pd
import streamlit as st
# Importamos herramientas necesarias de la librería SPARQLWrapper
import lzma
import dill as pickle

def load_modelB():
    with lzma.open('lista_de_juegos.pkl', 'rb') as file:
        B = pickle.load(file)
        return B
p = load_modelB()


def load_modelA():
    with lzma.open('header.pkl', 'rb') as file:
        A = pickle.load(file)
        return A


lista_videojuegos = load_modelA()


def load_modelC():
    with lzma.open('body.pkl', 'rb') as file:
        C = pickle.load(file)
        return C

C = load_modelC()
df = pd.read_csv('base_original.csv')



a=["Grand Theft Auto V"]
l=[10]
def actualizar(lista_original, lista_con_scores, lista_de_juegos,nombre):
    lista_corregida = []
    lista_de_puntajes = []
    puntajes_corregidos=[]
    lista_def=[nombre]
    o=0
    for i in lista_original:
        for j in lista_de_juegos:
            if i == j:
                lista_corregida = lista_corregida + [j]
    for h in lista_corregida:
        u = 0
        for g in lista_de_juegos:
            if h==g:
                puntajes_corregidos=puntajes_corregidos+[lista_con_scores[u]]
            else:
                u=u+1
    for r in lista_original:
        flag=False
        for k in lista_corregida:
            if r==k:
                lista_de_puntajes=lista_de_puntajes+[puntajes_corregidos[o]]
                lista_def = lista_def + [puntajes_corregidos[o]]
                o=o+1
                flag=True
        if flag==False:
            lista_de_puntajes=lista_de_puntajes+[0]
            lista_def = lista_def + [0]


    return lista_def


from IPython.display import display, HTML


df = pd.read_csv('base_original.csv',encoding="utf-8")
lol = df.values.tolist()
aaa=df.loc[df['Nombre'] == 'Andres']
display(aaa)
print(aaa)


