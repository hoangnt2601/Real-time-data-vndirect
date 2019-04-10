import json
import price

def try_float(x):
    try:
        return float(x)
    except ValueError:
        return 0

def arr2ba(arr):
    return {
        "time": arr[0],
        "code": arr[1],
        "bidPrice01": try_float(arr[2]),
        "bidQtty01": try_float(arr[3]),
        "bidPrice02": try_float(arr[4]),
        "bidQtty02": try_float(arr[5]),
        "bidPrice03": try_float(arr[6]),
        "bidQtty03": try_float(arr[7]),
        "offerPrice01": try_float(arr[8]),
        "offerQtty01": try_float(arr[9]),
        "offerPrice02": try_float(arr[10]),
        "offerQtty02": try_float(arr[11]),
        "offerPrice03": try_float(arr[12]),
        "offerQtty03": try_float(arr[13]),
        "accumulatedVol": try_float(arr[14]),
        "matchPrice": try_float(arr[15]),
        "matchQtty": try_float(arr[16]),
        "matchValue": try_float(arr[17]),
        "totalOfferQtty": try_float(arr[18]),
        "totalBidQtty": try_float(arr[19]),
    }

def arr2sp(arr):
    return {
        "floorCode": arr[0],
        "tradingDate": arr[1],
        "time": arr[2],
        "code": arr[3],
        "companyName": arr[4],
        "stockType": arr[5],
        "totalRoom": try_float(arr[6]),
        "currentRoom": try_float(arr[7]),
        "basicPrice": try_float(arr[8]),
        "openPrice": try_float(arr[9]),
        "closePrice": try_float(arr[10]),
        "currentPrice": try_float(arr[11]),
        "currentQtty": try_float(arr[12]),
        "highestPrice": try_float(arr[13]),
        "lowestPrice": try_float(arr[14]),
        "ceilingPrice": try_float(arr[15]),
        "floorPrice": try_float(arr[16]),
        "averagePrice": try_float(arr[17]),
        "accumulatedVal": try_float(arr[18]),
        "buyForeignQtty": try_float(arr[19]),
        "sellForeignQtty": try_float(arr[20]),
        "projectOpen": try_float(arr[21]),
        "sequence": arr[22],
    }


def arr2mi(arr):
    return {
        "marketID": arr[0],
        "totalTrade": try_float(arr[1]),
        "totalShareTraded": try_float(arr[2]),
        "totalValueTraded": try_float(arr[3]),
        "advance": try_float(arr[4]),
        "decline": try_float(arr[5]),
        "noChange": try_float(arr[6]),
        "indexValue": try_float(arr[7]),
        "changed": try_float(arr[8]),
        "tradingTime": arr[9],
        "tradingDate": arr[10],
        "floorCode": arr[11],
        "marketIndex": try_float(arr[12]),
        "priorMarketIndex": try_float(arr[13]),
        "highestIndex": try_float(arr[14]),
        "lowestIndex": try_float(arr[15]),
        "shareTraded": try_float(arr[16]),
        "status": arr[17],
        "sequence": arr[18],
        "predictionMarketIndex": try_float(arr[19]),
    }


def arr2de(arr):
    return {
        "accumulatedVal": float(arr[0]),
        "accumulatedVol": float(arr[1]),
        "basicPrice": float(arr[2]),
        "bidPrice01": float(arr[3]),
        "bidPrice02": float(arr[4]),
        "bidPrice03": float(arr[5]),
        "bidQtty01": float(arr[6]),
        "bidQtty02": float(arr[7]),
        "bidQtty03": float(arr[8]),
        "buyForeignQtty": float(arr[9]),
        "ceilingPrice": float(arr[10]),
        "code": arr[11],
        "currentPrice": float(arr[12]),
        "currentQtty": float(arr[13]),
        "highestPrice": float(arr[14]),
        "lastTradingDate": arr[15],
        "lowestPrice": float(arr[16]),
        "matchPrice": float(arr[17]),
        "matchQtty": float(arr[18]),
        "offerPrice01": float(arr[19]),
        "offerPrice02": float(arr[20]),
        "offerPrice03": float(arr[21]),
        "offerQtty01": float(arr[22]),
        "offerQtty02": float(arr[23]),
        "offerQtty03": float(arr[24]),
        "openInterest": float(arr[25]),
        "openPrice": float(arr[26]),
        "sellForeignQtty": float(arr[27]),
        "tradingSessionId": arr[28],
        "bidPrice04": float(arr[29]),
        "bidPrice05": float(arr[30]),
        "bidPrice06": float(arr[31]),
        "bidPrice07": float(arr[32]),
        "bidPrice08": float(arr[33]),
        "bidPrice09": float(arr[34]),
        "bidPrice10": float(arr[35]),
        "bidQtty04": float(arr[36]),
        "bidQtty05": float(arr[37]),
        "bidQtty06": float(arr[38]),
        "bidQtty07": float(arr[39]),
        "bidQtty08": float(arr[40]),
        "bidQtty09": float(arr[41]),
        "bidQtty10": float(arr[42]),
        "offerPrice04": float(arr[43]),
        "offerPrice05": float(arr[44]),
        "offerPrice06": float(arr[45]),
        "offerPrice07": float(arr[46]),
        "offerPrice08": float(arr[47]),
        "offerPrice09": float(arr[48]),
        "offerPrice10": float(arr[49]),
        "offerQtty04": float(arr[50]),
        "offerQtty05": float(arr[51]),
        "offerQtty06": float(arr[52]),
        "offerQtty07": float(arr[53]),
        "offerQtty08": float(arr[54]),
        "offerQtty09": float(arr[55]),
        "offerQtty10": float(arr[56]),
        "time": arr[57],
        "floorPrice": float(arr[58]),
    }


def arr2de(arr):
    return {
        'accumulatedVal': try_float(arr[0]),
        'accumulatedVol': try_float(arr[1]),
        'basicPrice': try_float(arr[2]) * 1000,
        'bidPrice01': try_float(arr[3]) * 1000,
        'bidPrice02': try_float(arr[4]) * 1000,
        'bidPrice03': try_float(arr[5]) * 1000,
        'bidQtty01': try_float(arr[6]),
        'bidQtty02': try_float(arr[7]),
        'bidQtty03': try_float(arr[8]),
        'buyForeignQtty': try_float(arr[9]),
        'ceilingPrice': try_float(arr[10]) * 1000,
        'code': try_float(arr[11]),
        'currentPrice': try_float(arr[12]) * 1000,
        'currentQtty': try_float(arr[13]),
        'highestPrice': try_float(arr[14]) * 1000,
        'lastTradingDate': try_float(arr[15]),
        'lowestPrice': try_float(arr[16]) * 1000,
        'matchPrice': try_float(arr[17]) * 1000,
        'matchQtty': try_float(arr[18]),
        'offerPrice01': try_float(arr[19]) * 1000,
        'offerPrice02': try_float(arr[20]) * 1000,
        'offerPrice03': try_float(arr[21]) * 1000,
        'offerQtty01': try_float(arr[22]),
        'offerQtty02': try_float(arr[23]),
        'offerQtty03': try_float(arr[24]),
        'openInterest': try_float(arr[25]),
        'openPrice': try_float(arr[26]) * 1000,
        'sellForeignQtty': try_float(arr[27]),
        'tradingSessionId': try_float(arr[28]),
        'bidPrice04': try_float(arr[29]) * 1000,
        'bidPrice05': try_float(arr[30]) * 1000,
        'bidPrice06': try_float(arr[31]) * 1000,
        'bidPrice07': try_float(arr[32]) * 1000,
        'bidPrice08': try_float(arr[33]) * 1000,
        'bidPrice09': try_float(arr[34]) * 1000,
        'bidPrice10': try_float(arr[35]) * 1000,
        'bidQtty04': try_float(arr[36]),
        'bidQtty05': try_float(arr[37]),
        'bidQtty06': try_float(arr[38]),
        'bidQtty07': try_float(arr[39]),
        'bidQtty08': try_float(arr[40]),
        'bidQtty09': try_float(arr[41]),
        'bidQtty10': try_float(arr[42]),
        'offerPrice04': try_float(arr[43]) * 1000,
        'offerPrice05': try_float(arr[44]) * 1000,
        'offerPrice06': try_float(arr[45]) * 1000,
        'offerPrice07': try_float(arr[46]) * 1000,
        'offerPrice08': try_float(arr[47]) * 1000,
        'offerPrice09': try_float(arr[48]) * 1000,
        'offerPrice10': try_float(arr[49]) * 1000,
        'offerQtty04': try_float(arr[50]),
        'offerQtty05': try_float(arr[51]),
        'offerQtty06': try_float(arr[52]),
        'offerQtty07': try_float(arr[53]),
        'offerQtty08': try_float(arr[54]),
        'offerQtty09': try_float(arr[55]),
        'offerQtty10': try_float(arr[56]),
        'time': try_float(arr[57]),
        'floorPrice': try_float(arr[58]) * 1000,
    }

# message type
BA = "BA"
SP = "SP"
DE = "DERIVATIVE_OPT"
MI = "MI"

arr_map = {
    BA: arr2ba,
    SP: arr2sp,
    MI: arr2mi,
    DE: arr2de,
}

def load(msg):
    obj = json.loads(msg)
    data = obj.get("data")
    msgType = obj.get("type")
    if obj["type"] not in arr_map:
        return {"success": False, "message": "Unknown message type", "original": msg}
    try:
        arr = data.split("|")
        return arr_map.get(obj["type"])(arr)
    except KeyError:
        raise KeyError("Array may not have enough items to convert to object, check input message")
