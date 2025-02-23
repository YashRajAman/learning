from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import List, Annotated
import os

app = FastAPI()

UPLOAD_DIRECTORY = "D:\\github-repo\\learning\\python3\\rest_api\\uploaded_files"

# Ensure the upload directory exists
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@app.post("/files/")
async def create_files(files: Annotated[List[bytes], File()]):
    return {"file_sizes": [len(file) for file in files]}

@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile]):
    saved_filenames = []
    for file in files:
        # Save each uploaded file to the specified directory
        file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
        with open(file_location, "wb") as f:
            f.write(await file.read())
        saved_filenames.append(file.filename)
    return {"filenames": saved_filenames}

@app.get("/", response_class=HTMLResponse)
async def main():
    content = """
    <body>
        <form action="/files/" enctype="multipart/form-data" method="post">
            <input name="files" type="file" multiple>
            <input type="submit">
        </form>
        <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
            <input name="files" type="file" multiple>
            <input type="submit">
        </form>
    </body>
    """
    return content

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("upload_api:app", host="0.0.0.0", port=8000, log_level="debug", reload=True)
