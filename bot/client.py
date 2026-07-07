import os
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.logging_config import setup_logger

load_dotenv()
logger = setup_logger()


class BinanceFuturesClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY", "").strip()
        self.api_secret = os.getenv("BINANCE_API_SECRET", "").strip()
        self.base_url = os.getenv("BINANCE_BASE_URL", "https://testnet.binancefuture.com").strip()

        if not self.api_key:
            raise ValueError("Missing BINANCE_API_KEY in .env")
        if not self.api_secret:
            raise ValueError("Missing BINANCE_API_SECRET in .env")

        logger.info(f"Using Binance Futures base URL: {self.base_url}")

        self.client = Client(self.api_key, self.api_secret, testnet=True)
        self.client.FUTURES_URL = self.base_url + "/fapi"

    def test_connection(self):
        try:
            logger.info("Testing Binance Futures account connection...")
            response = self.client.futures_account()
            logger.info("Connection test successful.")
            return response
        except BinanceAPIException as e:
            logger.error(f"Binance API connection error: status={e.status_code}, message={e.message}")
            raise
        except BinanceRequestException as e:
            logger.error(f"Network connection error: {str(e)}")
            raise
        except Exception as e:
            logger.exception(f"Unexpected connection error: {str(e)}")
            raise

    def place_order(self, payload: dict):
        try:
            logger.info(f"Order request payload: {payload}")
            response = self.client.futures_create_order(**payload)
            logger.info(f"Order response: {response}")
            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API error: status={e.status_code}, message={e.message}")
            raise

        except BinanceRequestException as e:
            logger.error(f"Binance request error: {str(e)}")
            raise

        except Exception as e:
            logger.exception(f"Unexpected error while placing order: {str(e)}")
            raise