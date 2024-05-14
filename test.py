from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return "Hello world!"

@app.get("/ramon")
def ramon():
    return "Hello Ramón!"

@app.get("/hello/{name}")
def llamada(name):
    return f"Hello {name}!"

@app.get("/home")
def home():
    return "<html><body><h1>Hola !! </h1></body></html>"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("test:app", reload=True)