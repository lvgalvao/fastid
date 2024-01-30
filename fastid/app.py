from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

app = FastAPI()
app.mount(
    '/static', 
    StaticFiles(directory='static'),
    name='static'
)

templates = Jinja2Templates(directory='templates')

@app.get("/")
async def read_root(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name='home.html')