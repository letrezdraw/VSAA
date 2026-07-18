from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel

api = FastAPI()

@api.get("/")
def home():
    return {"message": "Video Streaming Analytics API is running"}

class Heartbeat(BaseModel):
    user_id: int
    video_id: int
    watch_duration: int
    timestamp: datetime
    
@api.post("/heartbeat")
def receive_heartbeat(data: Heartbeat):
    return{
        "message": "Heartbeat received successfully",
        "data": data
    }