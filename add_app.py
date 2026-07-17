import streamlit as st

def adder(a):
    return a + a 

def fun(a, s):
    s= str(s)
    a= int(a)
    c= "Hello, "+ s + " your number is " + str(adder(a))
    return c

st.write("# Adder")
st.write("Hola, anota tu nombre y dame un numero entero: ")
send= st.button("Enviar")

number= st.text_input("number= ", key="number")
name= st.text_input("name= ", key="name")
if send: 
    if name and number:
        result= fun(number, name)
        st.write(result)