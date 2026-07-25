import streamlit as st
import dataBase as db
import errors as e

def find(query:str, data_base: db.my_db):
    data_base.set_query(query)
    return data_base.search_db()

def write_db(query: str, data_base: db.my_db):
    data_base.set_query(query)
    data_base.change_db()

@st.cache_resource
def connect():
    return db.my_db()

if __name__ == "__main__":
    movies_base= connect()
    st.title("Buscador de peliculas", text_alignment="center" )
    st.header("Te diré si tengo la pelicula o no", text_alignment="center")

    send_question= st.button("Preguntar", type= "primary")

    question= st.text_input("pelicula= ")

    send_change= st.button("Reservar", type= "secondary", icon= "💵")

    if send_question and len(question) > 0:
        amount, total_films= find(question, movies_base)
        if total_films == 0:
            st.write("No tengo esa pelicula :loudspeaker:")
        elif amount == 0:
            st.write("No tengo de esa pelicula")

        else:
            st.write(f"Tengo {amount} de esa pelicula :sunglasses:")

    elif send_change and len(question) > 0:
        try:
            write_db(question, movies_base)
            st.write("Operacion realizada exitosamente :tada:")
        except :
            st.error(":rotating_light: Pelicula poco especifica. Tengo varias con ese nombre ")
        
    