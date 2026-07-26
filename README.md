# myWorld
My own trip to develop a web site using python

## intent vs goal
Intent: what I want to do right now

Goal: my final destination

## Intent
I'll write the newest intent on the top, so you can trace what i've done and you can check different branches for that particular purpose

- [X] Add file persistance to (ngrok + docker)_app
    * branch: readFile (simple readin)
    * branch: stream_bd (for a compleate and final product)

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

## How to run all this?
### Locally
If you want to run locally, you can by simple doing
* preparation:
    *  uv installed
    * The csv data file

```bash
uv sync && streamlit interface.py
```
This will open your browser and you will be able to run queries as you wish. But it will execute on local host.

### Internet
* Preparation:
    * uv installed
    * The csv data file
    * ngrok token


```bash
uv sync && python init_db.py && streamlit interface.py
```
It will create an duckdb file needed for docker to create the container.

now run
1. This will create the requirements for your docker image
```bash
uv export --format requirements-txt --no-hashes -o requirements.txt
```
2. Paste the ngrok token in docker-compose.yml

3. Create the container 
```bash
docker compose up -d --build
```
4. Check your ngrok account to see your https link and share it with your friends

5. When you are done, shut down your container
```bash
docker compose down
```
6. You can easly create the final result as
```bash
python export_csv.py
```

7. To wake up your container:
```bash
docker compose up -d
```