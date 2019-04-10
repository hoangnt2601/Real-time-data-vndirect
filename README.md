# Introduction
This is small example of how to retrieve and parse realtime market feed from VNDIRECT service.
Check ```main.py``` for sample code.
Check ```parser.py``` for detail fields of each message.

# Message types
### SP="StockPartial"
This message is sent whenever there is a match. Stock partial là trả về dữ liệu stock 

### BA="BidAsk"
This message is sent whenever there is a change in top 3 bid or ask prices. Generally you will see this message a lot more than SP. Bid: là giá chào mua, Ask: giá chào bán,

### DE="DerivativeOpt"
This message is for derivative market feed. The difference is there is top 10 bid or ask prices instead of just 3 like in cash market. Derivative là các thông tin về giá phái sinh.

### MI="MarketInformation"
This message carries update for index. 02: HNX - 03: UPCOM - 12: HNX30 10: VNINDEX - 11: VN30 - 13: VNXALL

