import asyncio
import websockets

CONNECTIONS = set()

async def handler(websocket):
    CONNECTIONS.add(websocket)
    async for message in websocket:
        for temp_websocket in CONNECTIONS:
            if temp_websocket != websocket:
                await temp_websocket.send(message)
    
async def main():
    async with websockets.serve(handler, "localhost", 5678):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())