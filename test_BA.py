import asyncio
import pathlib
import ssl
import websockets
import logging
import price
import parser_message
logging.basicConfig(filename='test_BA.txt',level=logging.INFO)


stock_ids = open("./StockIDs/HNX.txt", "r")
list_id = stock_ids.read().split('\n')
stock_ids.close()
print(list_id)

async def load_price():
    url = "wss://price-cmc-04.vndirect.com.vn/realtime/websocket"
    async with websockets.connect(url, ssl=True) as ws:
        logging.info(f"Connected")
        ps = price.Price(ws)
        await ps.subscribe(parser_message.BA, list_id)
        while True:
            msg = await ps.recv()
            logging.info(f"< {str(msg)}")


if __name__ == "__main__":
    logging.info("Start...")
    asyncio.get_event_loop().run_until_complete(load_price())

