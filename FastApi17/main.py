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
    