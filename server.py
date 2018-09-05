import asyncio
import websockets

async def periodic(websocket):
    while True:
        await websocket.send('Hablame')
        await asyncio.sleep(2)

async def hello(websocket, path):
    await websocket.send('Hablame')
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, 'localhost', 8095)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()