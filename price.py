import parser_message
import json

class Price():

    def __init__(self, ws):
        self.ws = ws

    async def subscribe(self, msgType, symbol_list):
        msg = {
            "type": "registConsumer",
            "data": {
                "sequence": 0,
                "params": {
                    "name": msgType,
                    "codes": symbol_list,
                }
            }
        }
        msg = json.dumps(msg)
        await self.ws.send(msg)

    async def recv(self):
        data = await self.ws.recv()
        return parser_message.load(data)


async def connect(url=''):
    async with websockets.connect(url, ssl=True) as ws:
        yield Price(ws)

