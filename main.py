from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Akshay'}}

@app.get('/about')
def about():
    return 'This is an About page.'