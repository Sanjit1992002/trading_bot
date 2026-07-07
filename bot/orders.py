def build_order_payload(symbol, side, order_type, quantity, price=None):
    payload = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
        "newOrderRespType": "RESULT",
    }

    if order_type == "LIMIT":
        payload["price"] = price
        payload["timeInForce"] = "GTC"

    return payload