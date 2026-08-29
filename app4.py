import streamlit as st 
import pandas as pd

from funciones_calculo import(calcular_liquido, calcular_bsw, proyectar_produccion)

from funciones_datos import (filtrar_pozo, resumen_dataframe)

from clase_pozo import Pozo

st.title ("Bootcamp-Data-Analytics-SPE")
st.sidebar.title('Parámetros')

modulos = st.sidebar.selectbox('Seleccione un módulo', ["Introducción a variables", 'Funciones','POO','Importación de librerías'])

if modulos == 'Introducción a variables':

    pozo =  "SPE-001"
    Petroleo_bpd= 1250
    agua_bpd = 350.50
    status = True

    st.write(pozo)
    st.write(Petroleo_bpd)
    st.write(agua_bpd)
    st.write(status)

elif modulos == 'Funciones':
    def calcular_caudal_vogel(caudal_maximo = 1000, presion_yacimiento = 3000, presion_fondo = 200, decimales = 2):
                
            relacion_presion= presion_fondo/presion_yacimiento

            caudal= caudal_maximo*(1 - 0.2*relacion_presion - 0.8*(relacion_presion**2))

            return round(caudal, decimales)

    caudal_maximo = st.number_input('Ingrese el caudal máximo', min_value= 0, max_value= 5000, value= 1200)
    presion_yacimiento= st.number_input('Ingrese la presión del yacimiento',min_value= 0, max_value= 9000, value= 3000)
    presion_fondo= st.number_input('Ingrese la presión de fondo fluyente',min_value= 0, max_value= 5000, value= 1500)
    decimales= st.slider('Seleccione la cantidad de decimales para su resultado', min_value= 0, max_value= 4, value= 2)

    caudal = calcular_caudal_vogel(caudal_maximo, presion_yacimiento, presion_fondo, decimales)

    st.write('El caudal es:', caudal)

elif modulos == 'POO':
    class Pozo:
        def __init__(self,nombre,campo,petroleo, agua):
            self.n = nombre
            self.c = campo
            self.p = petroleo
            self.a = agua
        def mostrar_informacion(self):
            st.write(f'Pozo: {self.n}')
            st.write(f'Campo: {self.c}')
            st.write(f'Petroleo: {self.p} BPD')
            st.write(f'Agua: {self.a} BPD')

        def produccion_total(self):
            total_produccion= self.p+self.a
            return total_produccion

        def proyectar_produccion(self,dias):
            produccion_proyectada = (self.p + self.a)*dias
            return produccion_proyectada

    Nombre_pozo = st.text_input('Ingrese el nombre del pozo')
    Campo_pozo = st.text_input('Ingrese el campo al que pertenece')
    Petroleo = st.number_input('Ingrese la producción de petroleo', min_value= 0, max_value= 5000, value= 1000)
    Agua = st.number_input('Ingrese la producción de agua', min_value= 0, max_value= 5000, value= 200)

    pozo= Pozo(Nombre_pozo,Campo_pozo,Petroleo,Agua)
    st.write(pozo.mostrar_informacion())
    st.write(pozo.produccion_total())
    dias= st.number_input('Ingrese los días a proyectar', min_value= 0, max_value= 365, value= 30)
    st.write(pozo.proyectar_produccion(dias))

elif modulos == 'Importación de librerías':
    st.title('Aplicacion Modular con Funciones y Claases')
    st.header('1.Uso de funciones')

    petroleo = st.number_input(
        "Produccion sde petroleo",
        min_value = 0.0,
        value = 200.0
    )
    agua = st.number_input(
            "Produccion sde agua",
            min_value = 0.0,
            value = 200.0
    )
    días = st.number_input(
            "Días",
            min_value = 1,
            value = 30
    )

    if st.button('Calcular'):
        liquido = calcular_líquido(
            petroleo,
            agua
        )

        bsw= calcular_bsw(
            petroleo,
            agua
        )

        proyeccion = proyectar_produccion(
            petroleo,
            días
        )

        st.write('Produccion líquida', liquido)
        st.write('BSW', round(bsw, 2), '%')
        st.write('Producción proyectada:', proyeccion)
