#!/usr/bin/env python3
"""ASGI WebSocket application using Starlette."""
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect


async def homepage(request):
    """Serve a simple HTML page."""
    return HTMLResponse("<h1>WebSocket App</h1>")


async def websocket_endpoint(websocket):
    """Accept the connection and echo messages back to the sender."""
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except WebSocketDisconnect:
        pass


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
