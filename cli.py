import argparse
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.client import BinanceFuturesClient
from bot.orders import build_order_payload
from bot.validators import validate_inputs


def print_order_summary(data):
    print("\nOrder Request Summary")
    print("-" * 30)
    print(f"Symbol     : {data['symbol']}")
    print(f"Side       : {data['side']}")
    print(f"Order Type : {data['order_type']}")
    print(f"Quantity   : {data['quantity']}")
    if data["order_type"] == "LIMIT":
        print(f"Price      : {data['price']}")


def print_order_response(response):
    print("\nOrder Response")
    print("-" * 30)
    print(f"Order ID     : {response.get('orderId')}")
    print(f"Status       : {response.get('status')}")
    print(f"Executed Qty : {response.get('executedQty')}")
    print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")
    print(f"Symbol       : {response.get('symbol')}")
    print(f"Side         : {response.get('side')}")
    print(f"Type         : {response.get('type')}")


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot CLI"
    )

    parser.add_argument("--test-connection", action="store_true", help="Test connection only")
    parser.add_argument("--symbol", help="Trading symbol, e.g. BTCUSDT")
    parser.add_argument("--side", help="BUY or SELL")
    parser.add_argument("--type", dest="order_type", help="MARKET or LIMIT")
    parser.add_argument("--quantity", help="Order quantity")
    parser.add_argument("--price", help="Required for LIMIT orders")

    args = parser.parse_args()

    try:
        client = BinanceFuturesClient()

        if args.test_connection:
            response = client.test_connection()
            print("\nConnection Successful")
            print("-" * 30)
            print("Assets returned:", len(response.get("assets", [])))
            print("Positions returned:", len(response.get("positions", [])))
            return

        if not args.symbol or not args.side or not args.order_type or not args.quantity:
            raise ValueError(
                "For order placement, --symbol, --side, --type, and --quantity are required."
            )

        validated = validate_inputs(
            symbol=args.symbol,
            side=args.side,
            order_type=args.order_type,
            quantity=args.quantity,
            price=args.price,
        )

        print_order_summary(validated)

        payload = build_order_payload(
            symbol=validated["symbol"],
            side=validated["side"],
            order_type=validated["order_type"],
            quantity=validated["quantity"],
            price=validated["price"],
        )

        response = client.place_order(payload)
        print_order_response(response)
        print("\nSuccess: Order placed successfully.")

    except ValueError as e:
        print(f"\nInput Error: {e}")

    except BinanceAPIException as e:
        print(f"\nAPI Error: {e.message}")

    except BinanceRequestException as e:
        print(f"\nNetwork Error: {str(e)}")

    except Exception as e:
        print(f"\nUnexpected Error: {str(e)}")


if __name__ == "__main__":
    main()