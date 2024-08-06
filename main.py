from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"name": "Prashant Karwasra"}

@app.get("/blog")
def abc(limit=10, published:bool=True, sort: Optional[str]=None):
    if published:
        return {'data': f"{limit} published blogs from the db"}
    else:
        return {'data': f"{limit} unpublished blog from the db"}


@app.get("/blog/unpublished")
def unpublished_blog():
    return {"the given below are unpublished blog"}

@app.get("/blog/{id}")
def show(id: int ):
    # fetech the detail whose id = id
    return {'data': id}



@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    # fetech the comments whose id= id
    return {'commnets': ['1','2','3']}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
def create_blog(blog: Blog):
    return {"data":f"blog is created with titled: {blog.title}"}


# if __name__  == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)