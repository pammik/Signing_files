import shutil
import socket
from typing import List
from pathlib import Path
from fastapi.responses import JSONResponse
from fastapi import FastAPI, UploadFile, File, HTTPException
from copy_fs import copy_files

upload_folder = Path("Download")
upload_folder.mkdir(parents=True, exist_ok=True)

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


@app.post("/uploadfile/")
async def create_upload_file(fld_down: str, file: List[UploadFile] = File(...)):
    try:
        for i in file:
            print(i.filename)
            hostname = socket.gethostname()
            # Save the uploaded file
            fin_path = upload_folder / fld_down
            fin_path.mkdir(parents=True, exist_ok=True)
            file_path = fin_path / i.filename
            with file_path.open("wb") as f:
                shutil.copyfileobj(i.file, f)

        return {"filename": i.filename, "file_path": str(file_path)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/sign_files")
def sign(fld_down: str):
    a = f"F:\git\Signing_files\Download\{fld_down}"
    b = f"F:\git\Signing_files\Download\\ready\{fld_down}"
    copy_files(a, b)


# Additional route to serve the uploaded files
@app.get("/files/{filename}")
async def read_file(filename: str):
    file_path = upload_folder / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")

    return JSONResponse(content={"file_path": str(file_path)}, status_code=200)


@app.get("/ready_signing_files")
def signing_files():
    pass