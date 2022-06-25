from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Item(BaseModel):
    title: str
    text: str

app = FastAPI()

origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    todo = {
        "todo": [
            {
                "id": 1,
                "name": "洗濯",
                "desc": "今日までにやる"
            },
            {
                "id": 2,
                "name": "ごはん食べる",
                "desc": "今日までにやる"
            }
        ]
    }
    return todo