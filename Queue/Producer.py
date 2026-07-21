from pydantic import BaseModel
import json
def publish(heartbeat):
    """
    Publish object from the API like Heartbeat to the Queue.
    """
    print(f"Publishing heartbeat of usser {heartbeat.user_id}")
    
    heartbeat_dict = heartbeat.model_dump() #convets object to dict
    print(f"Heartbeat data: {heartbeat_dict}")
     
    heartbeat_json = json.dumps(heartbeat_dict) #convets the dict to json 
    print(f"Heartbeat JSON: {heartbeat_json}") 