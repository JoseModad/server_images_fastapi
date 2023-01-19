from fastapi import APIRouter, UploadFile, File

from os import getcwd

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    with open(getcwd() + "/" + file.filename, "wb") as myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()
    return "Success"