import asyncio
import json
import uvicorn

from fastapi import FastAPI

app = FastAPI()

file = open('response_b.json')
json_data = json.load(file)
booking_list = list(json_data)

@app.post('/search/{booking_id}')
async def search(booking_id: int):
    await asyncio.sleep(3)
    return booking_list[booking_id]

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=9002)