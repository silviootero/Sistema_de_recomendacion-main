import pandas as pd
import streamlit as st
import csv
import lzma
import dill as pickle

@st.cache
def load_modelB():
    with lzma.open('lista_de_juegos.pkl', 'rb') as file:
        B = pickle.load(file)
        return B

p = load_modelB()

@st.cache
def load_modelA():
    with lzma.open('header.pkl', 'rb') as file:
        A = pickle.load(file)
        return A

lista_videojuegos = load_modelA()

def main():
    df = pd.read_csv('base_original.csv', encoding="utf-8")
    df2 = pd.read_csv('base_actualizada.csv', encoding="utf-8")

    st.title("Ingresar usuario")
    options = st.multiselect(
        'Seleccione los juegos que ha jugado',
        p,
        [])

    st.write('You selected:', options)
    indice = []
    variable = []
    st.text( "por favor mire la lista de usuarios ya creados abajo , evite ingresar nombres que ya estan o repetir nombres , de lo contrario la aplicacion tendra comportamientos inesperados")
    Nombre = st.text_input("Ingrese su Nombre")




    for i in options:
        valoracion = st.slider("Ingrese la valoracion de " + str(i), 0, 10)
        variable = variable + [i]
        indice = indice + [valoracion]

    def actualizar(lista_original, lista_con_scores, lista_de_juegos, nombre):
        lista_corregida = []
        lista_de_puntajes = []
        puntajes_corregidos = []
        lista_def = [nombre]
        o = 0
        for i in lista_original:
            for j in lista_de_juegos:
                if i == j:
                    lista_corregida = lista_corregida + [j]
        for h in lista_corregida:
            u = 0
            for g in lista_de_juegos:
                if h == g:
                    puntajes_corregidos = puntajes_corregidos + [lista_con_scores[u]]
                else:
                    u = u + 1
        for r in lista_original:
            flag = False
            for k in lista_corregida:
                if r == k:
                    lista_de_puntajes = lista_de_puntajes + [puntajes_corregidos[o]]
                    lista_def = lista_def + [puntajes_corregidos[o]]
                    o = o + 1
                    flag = True
            if flag == False:
                lista_de_puntajes = lista_de_puntajes + [0]
                lista_def = lista_def + [0]

        return lista_def

    Nuevo_usuario = actualizar(p, indice, variable, Nombre)

    def actualizar_csv(data1, data2, header, nueva_info):
        a = data1.values.tolist()
        b = data2.values.tolist()
        if a == b:
            a.append(nueva_info)
            with open('base_actualizada.csv', 'w', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(a)
        else:
            b.append(nueva_info)
            with open('base_actualizada.csv', 'w', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(b)

    st.text(
        "el sistema actualizara cada minimo cambio mientras la opcion este marcada, primero rellene toda la info antes de marcar la opcion de ingresar , "
        " una vez rellene la informacion , marque la opcion de ingresar datos y desmarque enseguida para volver a ingresar datos")

    actualizar = st.checkbox('desea ingresar datos:')

    if actualizar:
        actualizar_csv(df, df2, lista_videojuegos, Nuevo_usuario)

    st.title("Comparacion")

    usuario = st.text_input("Ingrese su nombre de usuario")

    info_del_usuario = df2.loc[df2['Nombre'] == usuario]
    info_de_la_poblacion = df2.loc[df2['Nombre'] != usuario]
    st.dataframe(info_de_la_poblacion)
    st.dataframe(info_del_usuario)
    st.header("Juegos que jugastes comparado con el resto de la poblacion")
    juegos_del_usuario_que_la_poblacion_jugo = info_de_la_poblacion.loc[:, (info_del_usuario != 0).any(axis=0)]

    juegos_del_usuario = info_del_usuario.loc[:, (info_del_usuario != 0).any(axis=0)]

    st.dataframe(juegos_del_usuario_que_la_poblacion_jugo)
    st.dataframe(juegos_del_usuario)


    tabla = juegos_del_usuario_que_la_poblacion_jugo.filter(['Nombre'], axis=1)
    suma_col = juegos_del_usuario.sum(axis=1)
    tabla['Distancia'] = 0
    pp = juegos_del_usuario_que_la_poblacion_jugo.iloc[:, 1:]
    pp = pp.astype(int)
    qq = juegos_del_usuario.iloc[:, 1:]
    #st.dataframe(pp)
    qq = qq.astype(int)
    qqq = qq * -1
    #st.dataframe(qqq)
    maa = qqq.values.tolist()
    cadena2 = maa[0]
    #st.title(cadena2)
    muu = pp.add(cadena2, axis=1)
    porfin = muu ** 2

    #st.dataframe(porfin)

    xx = porfin.sum(axis=1)
    #st.dataframe(xx)
    wahh = xx ** (1 / 2)
    tabla['Distancia'] = xx ** (1 / 2)

    st.header("Afinidad entre usuarios")

    st.dataframe(tabla)

    st.text("Entre mas bajo el puntaje, mas afinidad se tiene con el usuario")
    st.text("Para organizar de mayor a menor o viceversa , de click en la tabla Distancia")

    st.title("Sistema de Recomendacion")
    st.header("Puntuaciones de otros usuarios respecto a juegos que no ha jugado el usuario")
    juegos_que_no_ha_jugado_el_usuario_poblacion = info_de_la_poblacion.loc[:, (info_del_usuario == 0).any(axis=0)]

    st.dataframe(juegos_que_no_ha_jugado_el_usuario_poblacion)

    st.text("juegos que no ha jugado el usuario")
    juegos_que_no_ha_jugado_el_usuario = info_del_usuario.loc[:, (info_del_usuario == 0).any(axis=0)]

    st.dataframe(juegos_que_no_ha_jugado_el_usuario)
    ooo = juegos_que_no_ha_jugado_el_usuario_poblacion.astype(int)
    #st.text("auxiliar")
    #st.dataframe(ooo)
    #st.text("recomendaciones")
    kk = ooo.mul(wahh, axis=0)
    #st.dataframe(kk)
    #st.text("auxiliar2")
    el_2 = kk.div(ooo, axis=0)
    el_3 = el_2.fillna(0)
    #st.dataframe(el_3)

    #st.title("suma recomendaciones")
    uuuuu = kk.sum(axis=0)
    #st.dataframe(uuuuu)
    #st.title("peso ponderado")
    eeeee = el_3.sum(axis=0)
    #st.dataframe(eeeee)
    st.header("Recomendacion de juegos que el usuario no ha jugado")
    jajaja = uuuuu.div(eeeee)
    st.dataframe(jajaja)
    st.text("Entre mayor puntaje mas afinidad tendras con el juego")


if __name__ == "__main__":
    main()