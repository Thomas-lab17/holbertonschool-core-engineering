#!/usr/bin/env python3
"""WebSocket server with broadcast communication."""
import asyncio

import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def connection_handler(websocket):
    """Broadcast each incoming message to all connected clients."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for client in set(connected_clients):
                try:
                    await client.send("B:{}".format(message))
                except ConnectionClosed:
                    connected_clients.discard(client)
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
