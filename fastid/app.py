from authlib.integrations.starlette_client import OAuth

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file = '.env'
    )

    DOMAIN: str
    CLIENT_ID: str
    CLIENT_SECRET: str

settings = Settings()

oauth = OAuth()
oauth.register(
    'auth0',
    client_id=settings.CLIENT_ID,
    client_secret=settings.CLIENT_SECRET,
    client_kwargs={
        'scope': 'openid profile email',
    },
    server_metadata_url=f'https://{settings.DOMAIN}/.well-known/openid-configuration',
)

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

@app.get("/login")
async def login(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name='profile.html')