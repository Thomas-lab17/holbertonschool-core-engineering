#!/usr/bin/env python3
"""WebSocket server with unicast communication."""
import asyncio

import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def connection_handler(websocket):
    """Send each incoming message back only to its sender."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await websocket.send("U:{}".format(message))
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the WebSocket server on localhost:8765."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
