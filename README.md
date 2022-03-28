# KimetsuNoFastAPI + MongoDB    

>*Plans: move to asyncPg     
Focused on performance, less own code and infrastructure.*

## Features 

- Docker with [MongoDB](https://www.mongodb.com) and [FastAPI](http://fastapi.tiangolo.com)  
- [Poetry](https://python-poetry.org) as dependency manager    
- Works well **async** (all, with db)  
- Env file parsed by Pydantic    
- **ObjectID** works well with **FastAPI** & **Pydantic** (I've created custom field. Compatible with FastAPI generic docs)    
- Structure with **Dependency Injection** (database implementation)    

Build on **Python: 3.8**.    


## Installation and usage 
> create env file and fill it as in example
1. ```make prepare``` to test code and check it with flake8
2. ```make run``` to run docker containter
## Usage on localhost
1. ```pip install poetry```
2. ```poetry install```
3. ```poetry shell```
4. ```uvicorn app.main:app --bind "0.0.0.0" --port "8000"--workers 2```
