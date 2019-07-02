import asyncio
import pathlib
import ssl
import websockets
import logging
import price
import parser_message
logging.basicConfig(filename='realtime.txt',level=logging.INFO)

stock_ids_hnx = open("StockIDs/HNX.txt", "r")
stock_ids_hsx = open("StockIDs/HSX.txt", "r")
stock_ids_upc = open("StockIDs/UPC.txt", "r")
list_id_hnx = stock_ids_hnx.read().split('\n')
list_id_hsx = stock_ids_hnx.read().split('\n')
list_id_upc = stock_ids_hnx.read().split('\n')
stock_ids_hnx.close()
stock_ids_hsx.close()
stock_ids_upc.close()
list_ids = list_id_hnx + list_id_hsx + list_id_upc
#print(list_ids)

async def load_price():
    url = "wss://price-cmc-04.vndirect.com.vn/realtime/websocket"
    async with websockets.connect(url, ssl=True) as ws:
        logging.info(f"Connected")
        ps = price.Price(ws)
        print("Subscribing BA...")
        await ps.subscribe(parser_message.BA, list_ids)
        print("Subscribing SP...")
        await ps.subscribe(parser_message.SP, list_ids)
        print("Subscribing SP...")
        await ps.subscribe(parser_message.DE, list_ids)
        print("Subscribing MI...")
        await ps.subscribe(parser_message.MI, ["10", "11", "12", "13", "02", "03"]) #02: HNX - 03: UPCOM - 12: HNX30 - 10: VNINDEX - 11: VN30 - 13: VNXALL
        while True:
            msg = await ps.recv()
            logging.info(f"< {str(msg)}")


if __name__ == "__main__":
    logging.info("Start...")
    asyncio.get_event_loop().run_until_complete(load_price())