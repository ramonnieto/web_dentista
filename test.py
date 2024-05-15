from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
template = Jinja2Templates(directory="template")

alumnos = [
    {"nombre":"Juan","apellido":"Lopez"},
    {"nombre":"Pedro","apellido":"Perez"},
    {"nombre":"Antonio","apellido":"Sanchez"},
] 

@app.get("/HelloTemplate/{Ramon}")
def Htemplate(request:Request,Ramon):
    return template.TemplateResponse("template.html", {"request":request,"hola":f"Soy {Ramon}"})


#bucle que dibuja tabla
@app.get("/alumnos")
def list_alumnos(request: Request):
    return template.TemplateResponse(
        "alumno.html",
        {
            "request": request,
            "name": "Director",
            "alumnos": alumnos
        })

@app.get("/hello")
def hello():
    return "Hello world!"

@app.get("/ramon")
def ramon():
    return "Hello Ramón!"

@app.get("/hello/{name}")
def llamada(name):
    return f"Hello, bienvenido {name}!"

@app.get("/home",response_class=HTMLResponse)
def read_root():
    return HTMLResponse("<h1>Hello World</h1>")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("test:app", reload=True)