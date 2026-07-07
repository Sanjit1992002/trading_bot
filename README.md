# Binance Futures Testnet Trading Bot

A lightweight Python command-line trading bot for the **Binance USDT-M Futures Testnet**. It lets you place both **Market** and **Limit** orders while keeping the code clean, modular, and easy to extend.

## 🚀 Features

- Place **Market** and **Limit** orders
- Supports both **Buy** and **Sell** trades
- Simple command-line interface using `argparse`
- Input validation before sending orders
- Modular project structure for easy maintenance
- Detailed logging of API requests, responses, and errors
- Graceful handling of API, network, and validation errors

---

## 📁 Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
├── cli.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone <your-github-repo-url>
cd trading_bot
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API credentials

Create a `.env` file in the project root and add your Binance Futures Testnet credentials:

```env
BINANCE_API_KEY=YOUR_TESTNET_API_KEY
BINANCE_API_SECRET=YOUR_TESTNET_API_SECRET
BINANCE_BASE_URL=https://testnet.binancefuture.com
LOG_FILE=logs/trading_bot.log
```

> **Note:** These must be **Binance Futures Testnet** API keys, not production Binance credentials.

---

## ▶️ Usage

### Test the API connection

```bash
python cli.py --test-connection
```

### Place a Market order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a Limit order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

---

## 📋 Sample Output

After placing an order, the CLI displays a summary like this:

```text
Order Response
------------------------------
Order ID     : 19899469686
Status       : FILLED
Executed Qty : 0.0010
Avg Price    : N/A
Symbol       : BTCUSDT
Side         : BUY
Type         : MARKET

Success: Order placed successfully.
```

---

## 📝 Logging

All activity is automatically logged to:

```text
logs/trading_bot.log
```

Logs include:

- Timestamp
- Log level
- API requests
- API responses
- Error details (if any)

---

## 💡 Assumptions

- Designed for **Binance USDT-M Futures Testnet** only.
- Limit orders use `GTC (Good Till Cancelled)` by default.
- Users provide valid trading symbols and quantities supported by Binance.
- API credentials are generated from the Futures Testnet.

---

## ⚠️ Troubleshooting

**Invalid API-key, IP, or permissions**

- Double-check that you're using **Futures Testnet** API keys.
- Make sure there are no extra spaces or quotes in your `.env` file.

**Limit order remains `NEW`**

- This is normal. The order will remain open until the market reaches your specified price.

**Market order is immediately `FILLED`**

- This is expected behavior on the Futures Testnet.

---

## 📦 Requirements

- Python 3.9+
- python-binance
- python-dotenv
- urllib3 < 2.0 (recommended for macOS with LibreSSL)

---

## 📄 License

This project is licensed under the **MIT License**.