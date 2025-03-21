from email.policy import default

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Text, Optional
from datetime import  datetime

app = FastAPI()

posts = []

# Post Model
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False

@app.get('/')
def read_root():
    return {'Welcome': 'Welcome to my REST API'}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts')
def save_post(post: Post):
    posts.append(post.dict())
    return "Post Received"