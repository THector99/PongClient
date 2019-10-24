import asyncio
import websockets

async def hello():
    uri = "ws://pwebsock.herokuapp.com/:3000"
    async with websockets.connect(uri) as ws:
        while True:
            bmsg = await ws.recv()
            print(f"< {bmsg}")
asyncio.get_event_loop().run_until_complete(hello())
