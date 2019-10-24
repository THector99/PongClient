import asyncio
import websockets

async def hello():
    uri = "ws://pwebsock.herokuapp.com/:3000"
    async with websockets.connect(uri) as ws:
        name = input("What's your name? ")

        await ws.send(name)
        print(f"> {name}")

        greeting = await ws.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())