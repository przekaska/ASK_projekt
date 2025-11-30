import asyncio
import websockets
import json

connected_clients = set()

async def handler(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received: {message}")

            try:
                data = json.loads(message)
            except json.JSONDecodeError:
                data = {"raw": message}

            for client in connected_clients:
                if client != websocket:
                    await client.send(json.dumps(data))

    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    finally:
        connected_clients.remove(websocket)

async def main():
    print("Starting server...")
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("Server started on port 8765")
        await asyncio.Future()

asyncio.run(main())
