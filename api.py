from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/assets", StaticFiles(directory="templates/assets"), name="assets")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def welcome() -> dict:
    return {"Welcome": "Hola mundo"}


@app.get("/test/", response_class=HTMLResponse)
async def testhtml():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """

@app.get("/layout", response_class=HTMLResponse)
async def view_layout(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/landing", response_class=HTMLResponse)
async def view_layout(request: Request):
    return templates.TemplateResponse(request=request, name="landing.html")

@app.get("/home", response_class=HTMLResponse)
async def view_layout(request: Request):
    return templates.TemplateResponse(request=request, name="pages/blog/home.html")