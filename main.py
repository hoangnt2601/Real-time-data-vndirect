
import asyncio
import pathlib
import ssl
import websockets
import logging
import price
import parser_message
logging.basicConfig(filename='test_BA.txt',level=logging.INFO)


async def load_price():
    url = "wss://price-cmc-04.vndirect.com.vn/realtime/websocket"
    async with websockets.connect(url, ssl=True) as ws:
        logging.info(f"Connected")
        ps = price.Price(ws)
        await ps.subscribe(parser_message.BA, ["VND", "AAA"])
        #await ps.subscribe(parser_message.SP, ["VND", "AAA"])
        #await ps.subscribe(parser_message.DE, ["VN30F0204"])
        #await ps.subscribe(parser_message.MI, ["10", "11", "12", "13", "02", "03"]) #02: HNX - 03: UPCOM - 12: HNX30 - 10: VNINDEX - 11: VN30 - 13: VNXALL
        while True:
            msg = await ps.recv()
            logging.info(f"< {str(msg)}")


if __name__ == "__main__":
    logging.info("Start...")
    asyncio.get_event_loop().run_until_complete(load_price())
