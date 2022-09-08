from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer
from channels.consumer import AsyncConsumer

class EchoConsumer(AsyncJsonWebsocketConsumer):
    async def on_message(self, message):
        await self.send_json(message)