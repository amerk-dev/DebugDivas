from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from pars import setEventValueToDB

app = FastAPI()

def interval_task_24h():
    res = setEventValueToDB()
    print(res)

scheduler = BackgroundScheduler()
scheduler.add_job(interval_task_24h, 'interval', hours=24)
scheduler.start()
@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/scheduler/start-parce")
def start_parce():
    res = setEventValueToDB()
    return {"message": res}


@app.post("/api/schedule/add-push")
def add_push(tg_username:str = None):
    # добавляем в бд эту херню со статусом 1
    return

@app.post("/api/schedule/delete-push")
def add_push(tg_username: str = None):
    # добавляем в бд эту херню со статусом 0
    #
    return

@app.get("/api/schedule/get-info")
def add_push(tg_username: str = None):
    # добавляем в бд эту херню со статусом 1
    return