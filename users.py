from fastapi import requests,responses,FastAPI

app = FastAPI()

app.route('/users')
def users():
    return {
        'name':
            ['anand','aditya','sujal','sahil'],
        'age':[20,21,22,25]
        }