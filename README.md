# bitcoin-halving-market-impact

Event-based analysis of BTC, ETH and selected US large-cap stocks around Bitcoin halving dates using Python, Power Query and Power BI.

## Project goal

This project analyzes how selected market assets behaved in time windows around Bitcoin halving events.

The scope is intentionally limited to:
- Bitcoin (BTC-USD)
- Ethereum (ETH-USD)
- Selected large-cap US stocks
- Event windows around Bitcoin halving dates

The project does not attempt to prove causation. It focuses on descriptive analysis of price behavior, returns and selected correlations around known halving dates.

## Planned stack

- Python
- Pandas
- yfinance
- Power Query
- Power BI
- Git / GitHub

## Planned repository structure

```text
data/
  reference/
notebooks/
powerbi/
  screenshots/
src/
```

## Planned workflow

1. Download daily market data for crypto and selected stocks.
2. Store raw datasets as CSV files.
3. Prepare reference tables for halving dates and asset metadata.
4. Transform and combine data in Power Query.
5. Build a Power BI dashboard with 3 pages:
   - Overview
   - Halving windows
   - Correlations
6. Document limitations and findings in a notebook and README.

## Current status

Repository initialized. Data ingestion, reference tables and dashboard are work in progress.-
