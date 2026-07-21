"""with open("my_file.txt", "r")as file:
    for line in file:
        print(line.strip())
"""
import streamlit as st

FILE= "my_file.txt"

def suma():
    with open(FILE, "r") as file:
        linea= file.readlines()
        linea[0] = str ( int(linea[0])+1 ) + "\n"
    with open(FILE, "w") as file:
        file.writelines(linea)

def resta():
    with open(FILE, "r") as file:
        linea= file.readlines()
        linea[0] = str ( int(linea[0])-1 ) + "\n"
    with open(FILE, "w") as file:
        file.writelines(linea)


st.write("# File changer")
st.write("Let's add +1 to a file")
btn_sum= st.button("add +1", on_click= suma)
btn_rst= st.button("add -1", on_click= resta)

with open(FILE, "r") as file:
    linea= file.readline().strip("\n")
st.write("El archivo actualmente: " + linea)