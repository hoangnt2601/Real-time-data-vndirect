# Introduction
This is small example of how to retrieve and parse realtime market feed from VNDIRECT service.
Check ```main.py``` for sample code.
Check ```parser.py``` for detail fields of each message.

# Message types
### SP="StockPartial"
This message is sent whenever there is a match.

### BA="BidAsk"
This message is sent whenever there is a change in top 3 bid or ask prices. Generally you will see this message a lot more than SP.

### DE="DerivativeOpt"
This message is for derivative market feed. The difference is there is top 10 bid or ask prices instead of just 3 like in cash market.

### MI="MarketInformation"
This message carries update for index.

