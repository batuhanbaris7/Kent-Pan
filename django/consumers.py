import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"message": "🟢 WebSocket bağlantısı başarılı!"}))

    async def disconnect(self, close_code):
        print("🔌 WebSocket bağlantısı kapandı:", close_code)

    async def receive(self, text_data):
        print("📩 Gelen mesaj:", text_data)
        await self.send(text_data=json.dumps({"echo": text_data}))

