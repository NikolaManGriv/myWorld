# myWorld
My own trip to develop a web site using python

## intent vs goal
Intent: what I want to do right now

Goal: my final destination

## Intent
I'll write the newest intent on the top, so you can trace what i've done and you can check different branches for that particular purpose

- [X] Create a basic streamlit + docker app that takes a number and a string and prints something like "Hello \<name> your result is \<2*number>"
    * branch: simpleAdder (below I explain how to use docker files)

- [X] Create docker file for a very simple python program (add_app)
    * branch: simpleAdder

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

### WTF all those Docker files?
Those are used in order to create a docker image for adder app. That way you can create a personal server for that python program. 

These files do not take care of persistent data, I'll check that later.

### Steps on how to create the Docker Image
0. Assumpions:
    * You used UV in your own project
    * You already have a streamlit app ready to go
    * You created a NGROK account (it's free)
    * You installed docker and docker compose
1. This will create the requirements for your docker image.  
```bash
uv export --format requirements-txt --no-hashes -o requirements.txt
```
2. Using the Docker file in this repo, be free to change the CMD section to your python app name:
```docker
CMD ["python", "your_app.py"]  
```
3. Paste the ngrok token in docker-compose.yml
4. In order to create the image and don't freeze your terminal
```bash
docker-compose up --build -d
```
5. Check your NGROK account to see your https url
6. Each time someone new enters to your link an ugly error message will print in their screens but that's ok, just press "visit site" button and you are fine.