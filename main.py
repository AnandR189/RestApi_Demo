from fastapi import FastAPI

app = FastAPI()


details={
    'messsge':'Welcome in Rest world'
     
}

mark={
    'names':['anand','raghuwinder','disha','neel'],
    'age':[18,19,20,21],
    'marks':{'maths':[80,40,70,10],'oop':[12,15,18,20]}
}

@app.get('/')
async def read_root():
    return details

@app.get('/marks')
async def marks():
    return mark

