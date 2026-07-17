#!/usr/bin/env python3
"""Minimal WebSocket client."""
import asyncio

import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Connect to uri, send text once, receive one response and return it."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
    return response


async def main():
    """Send the demo string and print the response with no final newline."""
    response = await connect_and_send("ws://localhost:8765", "demo")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
