from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("api/scheduler/start-parce")
def start_parce():

    return {"XYZ": "123"}



@app.post("api/schedule/add-push")
def add_push(tg_username:str = None):
    # добавляем в бд эту херню со статусом 1
    return

@app.post("api/schedule/delete-push")
def add_push(tg_username: str = None):
    # добавляем в бд эту херню со статусом 0
    #
    return

@app.get("api/schedule/get-info")
def add_push(tg_username: str = None):
    # добавляем в бд эту херню со статусом 1
    return