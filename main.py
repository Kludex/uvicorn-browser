from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World"}


# @app.get("/hello")
# def hello():
#     return {"message": "Hello World"}
