from cgitb import text
import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print("Connected!")
        self.accept()

    def disconnect(self, code):
        print("Disconnected!")
        pass

    def receive(self, text_data=None, bytes_data=None):
        print("Recived!")
        decoded_data = json.loads(text_data)
        messgae = decoded_data['message']
        print(messgae)
        self.send(text_data=json.dumps({'message':messgae}))