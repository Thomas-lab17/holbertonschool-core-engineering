#!/usr/bin/env python3
"""Minimal WebSocket echo server."""
import asyncio

import websockets


async def connection_handler(websocket):
    """Echo back every text message received on the connection."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the WebSocket server on localhost:8765."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
