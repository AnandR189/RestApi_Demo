from fastapi import FastAPI

app = FastAPI()

movie = []

@app.get("/")
async def default():
    return {"Hello":"World"}


@app.get("/movies")
async def view():
    return movie

@app.get("/movies/{id}")
async def get_movie(id:int):
    for i in movie:
        if i["id"]==id:
            return i
        
        
@app.post("/movies/{id}/{name}")
async def add_movie(id:int,name:str):
    movie.append({"id":id,"name":name})
    return {"message":"added successfully"}

@app.put("/movies/{id}/{name}")
async def update_movie(id:int,name:str):
    for i in range(len(movie)):
        if movie[i]["id"] == id:
            movie[i]["name"] = name
            return {"message":"value updated!"}
        else:
            return {"mesage":"value not found!"}

@app.delete("/movies/{id}")
async def delete_movie(id:int):
    for i in range(len(movie)):
        if movie[i]["id"] == id:
            del movie[i]
            return {"message":"record deleted successfully"}
        else:
            return {"message":"value not found!"}
            
    


