from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
REFERENCE_DIR = DATA_DIR / "reference"

TICKERS = [
    "BTC-USD",
    "ETH-USD",
    "AAPL",
    "MSFT",
    "NVDA",
    "AMZN",
    "GOOGL",
]

START_DATE = "2011-01-01"
END_DATE = None

RAW_FILE_MAP = {
    "BTC-USD": "BTC-USD.csv",
    "ETH-USD": "ETH-USD.csv",
    "AAPL": "AAPL.csv",
    "MSFT": "MSFT.csv",
    "NVDA": "NVDA.csv",
    "AMZN": "AMZN.csv",
    "GOOGL": "GOOGL.csv",
}