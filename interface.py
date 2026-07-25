import streamlit as st
import dataBase as db
import errors as e

def find(query:str, data_base: db.my_db):
    data_base.set_query(query)
    return data_base.search_db()

def write_db(query: str, data_base: db.my_db):
    data_base.set_query(query)
    return data_base.change_db()

@st.cache_resource
def connect():
    return db.my_db()

def rules():
    st.markdown("Escribe el nombre de la pelicula y presiona **Preguntar**"
            " para saber si tengo esa pelicula o no.")
    st.markdown("Presiona **Reservar** una vez hayas comprado fisicamente la pelicula")
    st.markdown("* No uses acentos en las peliculas")
    st.markdown("* Si es una saga 'lineal' como Harry Potter, busca como harry potter n"
                " con n el numero de la pelicula")
    st.markdown("* Si es una saga con precuelas, escribe las iniciales en español y luego el año")
    st.markdown("* ej: jw 2016 para john wick del 2016")
             


if __name__ == "__main__":
    movies_base= connect()
    st.title("Buscador de peliculas", text_alignment="center" )
    st.header("Te diré si tengo la pelicula o no", text_alignment="center")

    rules()

    send_question= st.button("Preguntar", type= "primary")

    question= st.text_input("pelicula= ")

    send_change= st.button("Reservar", type= "secondary", icon= "💵")

    if send_question and len(question) > 0:
        amount, total_films= find(question, movies_base)

        if total_films == 0 or amount== 0:
            st.write("No tengo esa pelicula :loudspeaker:")

        else:
            st.write(f"Tengo {amount} de esa pelicula :sunglasses:")

    elif send_change and len(question) > 0:
        try:
            cant= write_db(question, movies_base)
            if cant > 0:
                st.write("Operacion realizada exitosamente :tada:")
                print(cant)
            else:
                st.write("No tengo más stock de esa pelicula")
        except :
            st.error(":rotating_light: Pelicula poco especifica. Tengo varias con ese nombre ")
        
    