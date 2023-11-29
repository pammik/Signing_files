import shutil
from fastapi import FastAPI, UploadFile, File

app = FastAPI(
    title="Signing files"
)

buildagents = [
    {"id": 1, "role": "agent", "folder": "ba-01"},
    {"id": 2, "role": "agent", "folder": "ba-02"}
]

@app.get("/")
def hello():
    return "Hello World!"

@app.get("/buildagents/{ba_id}")
def get_ba(ba_id: int):
    return [agent for agent in buildagents if agent.get("id") == ba_id]

buildagents_22 = [
    {"id": 1, "role": "agent", "folder": "ba-01"},
    {"id": 2, "role": "agent", "folder": "ba-02"},
    {"id": 3, "role": "agent", "folder": "ba-03"}
]

@app.post("/buildagents/{ba_id}")
def change_folder(ba_id: int, new_folder: str):
    cur_host = list(filter(lambda host: host.get("id") == ba_id, buildagents_22))[0]
    cur_host["folder"] = new_folder
    return {"status": 200, "data": cur_host}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    with open('test.txt', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"file_name": file.filename}

@app.get("/ready_signing_files")
def signing_files():
    pass