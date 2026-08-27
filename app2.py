import streamlit as st 

st.title ("Bootcamp-Data-Analytics-SPE")
st.sidebar.title('Parámetros')

modulos = st.sidebar.selectbox('Seleccione un módulo', ["Introducción a variables", 'Funciones'])

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