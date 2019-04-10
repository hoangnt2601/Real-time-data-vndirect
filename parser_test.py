import parser_message

def test_sanity():
    msg = '{"type":"BA","data":"14:53:34|LPB|9.1|690|9|50350|8.9|23950|9.2|3000|9.3|10000|9.4|8840|100790|9.4|290|0.02726|157580|198110|"}'
    obj = parser_message.load(msg)
    assert obj['time'] == "14:53:34"
    assert obj['totalBidQtty'] == 198110