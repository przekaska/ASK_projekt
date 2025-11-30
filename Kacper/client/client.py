import asyncio
import websockets
import json
import time

async def send_json():
    uri = "ws://serwer:8765"
    print(uri)
    while True:
        try:
            async with websockets.connect(uri) as websocket:
                data = {"time": time.time()}
                await websocket.send(json.dumps(data))
                print(f"DATA SENT: {data}")
                await asyncio.sleep(1)
        except Exception as e:
            print(f"Connection failed: {e}. Retrying in 1 second...")
            await asyncio.sleep(1)

asyncio.run(send_json())
