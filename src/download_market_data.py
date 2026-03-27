from pathlib import Path

import pandas as pd
import yfinance as yf

from config import RAW_DIR, TICKERS, START_DATE, END_DATE, RAW_FILE_MAP


def ensure_output_dir(directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)


def download_single_ticker(ticker: str, start_date: str, end_date: str | None) -> pd.DataFrame:
    df = yf.download(
        tickers=ticker,
        start=start_date,
        end=end_date,
        interval="1d",
        auto_adjust=False,
        progress=False,
    )

    if df.empty:
        raise ValueError(f"No data downloaded for ticker: {ticker}")

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df.reset_index()

    expected_columns = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]
    existing_columns = [col for col in expected_columns if col in df.columns]
    df = df[existing_columns].copy()

    df["Ticker"] = ticker
    df["Date"] = pd.to_datetime(df["Date"]).dt.date

    numeric_columns = [col for col in ["Open", "High", "Low", "Close", "Adj Close", "Volume"] if col in df.columns]
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.sort_values("Date").reset_index(drop=True)
    return df


def save_ticker_data(df: pd.DataFrame, output_path: Path) -> None:
    df.to_csv(output_path, index=False)


def main() -> None:
    ensure_output_dir(RAW_DIR)

    for ticker in TICKERS:
        output_file = RAW_DIR / RAW_FILE_MAP[ticker]
        df = download_single_ticker(
            ticker=ticker,
            start_date=START_DATE,
            end_date=END_DATE,
        )
        save_ticker_data(df, output_file)
        print(f"Saved {ticker} -> {output_file}")


if __name__ == "__main__":
    main()