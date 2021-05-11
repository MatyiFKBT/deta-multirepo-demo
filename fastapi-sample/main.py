from deta import App
from fastapi import FastAPI

app = App(FastAPI())

# triggered with an HTTP request
@app.get("/")
def http():
    return "Hello deta, i am running with HTTP using fastapi"