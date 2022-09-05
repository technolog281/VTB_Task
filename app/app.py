from fastapi import FastAPI, Request, Response
from fastapi.responses import FileResponse
from app.storage import show, add, file_path
from typing import Union
import os
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get('/', response_class=FileResponse)
async def home_page():
    script_dir = os.path.dirname(__file__)
    abs_path = os.path.join(script_dir, 'static/index.html')
    return abs_path


@app.get('/api/v1/storage/json')
async def read_storage_key(key: str):
    return JSONResponse(content=show(key))


@app.get('/api/v1/storage/json/{path}')
async def get_all(path: str, key: Union[str, None] = None):
    if path == 'all':
        return JSONResponse(content=show('all'))
    elif path == 'read':
        return JSONResponse(content=show(key))


@app.post('/api/v1/storage/json/write')
async def post_data(request: Request):
    get_data = await request.json()
    for key in get_data:
        add(key, get_data.get(key))
        return Response(status_code=200)


@app.on_event("shutdown")
def shutdown_event():
    os.remove(file_path)
