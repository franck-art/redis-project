import redis
import json
from fastapi import FastAPI
import random
import config
import uvicorn


app = FastAPI()
r = redis.Redis( host=config.Config.CACHE_REDIS_HOST, port=config.Config.CACHE_REDIS_PORT, db=config.Config.CACHE_REDIS_DB, password=config.Config.CACHE_REDIS_PASSWORD) # Connect to Redis

# Get request
# Path parameters 

# Get users' informations from redis by setting user_id
@app.get("/users/{user_id}")
async def get_users(user_id):
    cache = r.hgetall(user_id)
    if cache:
        return cache

# Get all users from redis with key match "users:*"
@app.get("/all_users")
async def get_all_users():
    keys = []
    for key in r.scan_iter("users:*"):
        keys.append(key)
    return keys

# Query parameters   
# Add users to redis
@app.get("/users/")
async def add_user(name: str , age: int , email: str):
    users_id = random.randint(1, 1000000)
    users = {"name": name, "age": age, "email": email}
    r.hset("users:" + str(users_id), mapping=users) 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
