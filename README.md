# myWorld
My own trip to develop a web site using python

## intent vs goal
Intent: what I want to do right now

Goal: my final destination

## Intent
I'll write the newest intent on the top, so you can trace what i've done and you can check different branches for that particular purpose

- [ ] Add file persistance to (ngrok + docker)_app
    * branch: readFile

- [X] Create a basic streamlit app that takes a number and a string and prints something like "Hello \<name> your result is 2*\<number>"
    * branch: simpleAdder (check docker section in simpleAdder/README.md)

- [X] Create docker file for a very simple python program (add_app)
    * branch: simpleAdder (ignore docker files)

- [X]  Install and run first (helloWorld) **streamlit** app
    * branch: helloStreamlit


For running the app:
```bash
uv sync &&
streamlit run app.py
```

## Goal
To create a web app for a seller I know

## Trip
```
Docker + Streamlit + Ngrok
```
* I'll write everything with python.

* Using streamlite, I'll be able to have a web interface

* With Docker, the service will be conteined

* Ngrok for an https link