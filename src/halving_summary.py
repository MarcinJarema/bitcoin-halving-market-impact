"""Reproduce the halving-cycle summary table from the raw BTC data.

Usage:
    python src/halving_summary.py            # default window: +-550 days
    python src/halving_summary.py --window 365

The numbers match the "Podsumowanie cykli" table in the Power BI report
(PreMin / PostMax and the min -> max return).
"""
import argparse

import pandas as pd

from config import RAW_DIR, REFERENCE_DIR


def summarize(window_days: int = 550) -> pd.DataFrame:
    close = (
        pd.read_csv(RAW_DIR / "BTC-USD.csv", parse_dates=["Date"])
        .set_index("Date")["Close"]
        .sort_index()
    )
    halvings = pd.read_csv(REFERENCE_DIR / "halving_dates.csv", parse_dates=["halving_date"])

    rows = []
    for _, h in halvings.iterrows():
        d = h["halving_date"]
        if d < close.index.min() or d + pd.Timedelta(days=window_days) > close.index.max():
            rows.append({"halving": h["label"], "note": "window not fully covered by data"})
            continue
        pre = close[(close.index >= d - pd.Timedelta(days=window_days)) & (close.index <= d)]
        post = close[(close.index >= d) & (close.index <= d + pd.Timedelta(days=window_days))]
        p0 = close.asof(d)

        def change_after(days: int) -> float:
            return (close.asof(d + pd.Timedelta(days=days)) / p0 - 1) * 100

        rows.append(
            {
                "halving": h["label"],
                "pre_min_price": round(pre.min(), 2),
                "pre_min_day": (pre.idxmin() - d).days,
                "post_max_price": round(post.max(), 2),
                "post_max_day": (post.idxmax() - d).days,
                "min_to_max_return_pct": round((post.max() / pre.min() - 1) * 100, 2),
                "close_on_halving": round(p0, 2),
                "after_180d_pct": round(change_after(180), 1),
                "after_365d_pct": round(change_after(365), 1),
                f"after_{window_days}d_pct": round(change_after(window_days), 1),
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--window", type=int, default=550, help="window in days around each halving")
    args = parser.parse_args()
    print(summarize(args.window).to_string(index=False))


if __name__ == "__main__":
    main()
