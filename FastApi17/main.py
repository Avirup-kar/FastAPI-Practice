from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

#Step-1: Ensure uploads folder exist

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)
    
#STEP-2:Static file set-up
    
app.mount("/files", StaticFiles(directory=UPLOAD_DIR), name="files")

#Step-3: Upload file api
@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    file_path = os.path.join(UPLOAD_DIR, filename)
    
    if not filename:
        raise HTTPException (status_code=400, detail="File not selected")
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    return{
        "message": "File Uploaded successfully",
        "fileName": filename,
        "file_url": f"http://127.0.0.1:8000/files/{filename}"
    }   
    

#Step-4:Get File URL API
@app.get("/files/{filename}")
def get_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    print("Hi", file_path)
    
    if not os.path.exists(file_path):
            raise HTTPException (status_code=404, detail="File not found")
        
    return{
            f"http://127.0.0.1:8000/files/{filename}"
        }      