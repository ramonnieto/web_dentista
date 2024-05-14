from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

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