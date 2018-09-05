#!/usr/bin/env python

# WS client example

import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://localhost:8095') as websocket:

        greeting = await websocket.recv()
        print(f"< {greeting}")
asyncio.async(hello())
asyncio.get_event_loop().run_forever()