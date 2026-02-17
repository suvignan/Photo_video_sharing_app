from fastapi import FastAPI,HTTPException
from src.scheams import PostCreate,PostResponse

app =FastAPI()


text_posts ={

    1:{
        "title":"New Post",
        "content":"Test Post"
    }

}
@app.get('/posts')

def get_all_posts(limit:int=None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get('/posts/{id}')

def get_post(id:int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404,detail="Post Not Found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post:PostCreate)->PostResponse:
    new_post={"title":post.title,"content":post.content}
    text_posts[max(text_posts.keys())+1]=new_post
    return new_post

@app.delete("/post")

def delete_post():
    pass
