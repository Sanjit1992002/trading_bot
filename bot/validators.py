def validate_symbol(symbol: str) -> str:
    if not symbol:
        raise ValueError("Symbol is required.")
    symbol = symbol.strip().upper()
    if not symbol.isalnum():
        raise ValueError("Symbol must be alphanumeric, for example BTCUSDT.")
    return symbol


def validate_side(side: str) -> str:
    if not side:
        raise ValueError("Side is required.")
    side = side.strip().upper()
    if side not in {"BUY", "SELL"}:
        raise ValueError("Side must be BUY or SELL.")
    return side


def validate_order_type(order_type: str) -> str:
    if not order_type:
        raise ValueError("Order type is required.")
    order_type = order_type.strip().upper()
    if order_type not in {"MARKET", "LIMIT"}:
        raise ValueError("Order type must be MARKET or LIMIT.")
    return order_type


def validate_quantity(quantity) -> float:
    if quantity is None:
        raise ValueError("Quantity is required.")
    try:
        quantity = float(quantity)
    except (ValueError, TypeError):
        raise ValueError("Quantity must be a valid number.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")
    return quantity


def validate_price(price, order_type: str):
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")
        try:
            price = float(price)
        except (ValueError, TypeError):
            raise ValueError("Price must be a valid number.")

        if price <= 0:
            raise ValueError("Price must be greater than 0.")
        return price

    return None


def validate_inputs(symbol, side, order_type, quantity, price=None):
    symbol = validate_symbol(symbol)
    side = validate_side(side)
    order_type = validate_order_type(order_type)
    quantity = validate_quantity(quantity)
    price = validate_price(price, order_type)

    return {
        "symbol": symbol,
        "side": side,
        "order_type": order_type,
        "quantity": quantity,
        "price": price,
    }