from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# http://127.0.0.1:8000/blog?limit=104
@app.get('/blog')
def index(limit=10, published:bool=True):
    # return published
    if published:
        # http://127.0.0.1:8000/blog?limit=104&published=true
        return {'data': f'{limit} published blogs from db.'}
    else:
        # http://127.0.0.1:8000/blog?limit=104&published=false
        return {'data': f'{limit} blogs from db.'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


#Keep the dynamic routing below the static ones
@app.get('/blog/{id}')
def show(id:int):
    #fetch blog with id = id
    return {'data': id}



@app.get('/blog/{id}/comments')
def comments(id):
    return {"data": {'1', '2'}}



class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data':f'blog post has been created with title {blog.title}'}