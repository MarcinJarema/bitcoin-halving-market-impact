# bitcoin-halving-market-impact

Event-based analysis of BTC, ETH and selected US large-cap stocks around Bitcoin halving dates using Python, Power Query and Power BI.

## Project status

This repository is currently **work in progress**.

At the current MVP stage, the project already includes:
- an initial Power BI dashboard page focused on BTC price behavior around Bitcoin halving windows,
- a working analytical layout with KPI cards, filters, a cycle summary table and a price path chart,
- an initial Power BI data model based on fact and dimension tables.

The remaining parts of the project, including additional report pages, final data preparation flow and broader cross-asset comparison, are still being completed.

## Project goal

The goal of this project is to analyze how selected market assets behaved in time windows around Bitcoin halving events.

The project is focused on **descriptive analysis**, not causal claims.  
It aims to show how prices, local lows, post-halving highs and selected event-window metrics behaved around known Bitcoin halving dates.

## Current scope

The current scope includes:
- Bitcoin (`BTC-USD`)
- Ethereum (`ETH-USD`)
- selected US large-cap stocks
- event windows aligned to Bitcoin halving dates

At this stage, the most advanced and already visible part of the project is the BTC-focused dashboard page.

## Current MVP

### 1. Power BI report page: BTC Halving Thesis

The first completed report page focuses on BTC and answers a simple question:

**How did Bitcoin behave around halving windows across historical cycles?**

The page currently includes:
- KPI cards for:
  - pre-halving minimum day,
  - post-halving maximum day,
  - number of analyzed cycles,
- a cycle filter,
- a days-from-halving window filter,
- a summary table for halving cycles,
- a line chart showing BTC price paths around halving dates.

### 2. Data model

The report is built on a simple analytical model using:
- fact tables for market prices and halving-window observations,
- dimension tables for assets, calendar dates and halving metadata.

This model is intended to keep the Power BI layer readable and easier to extend with additional pages.

## Tech stack

- Python
- Pandas
- yfinance
- Power Query
- Power BI
- Git / GitHub

## Analysis approach

The workflow used in this project is:

1. Download daily market data for crypto and selected equities.
2. Prepare reference data for Bitcoin halving dates and asset metadata.
3. Align observations into event windows around halving dates.
4. Transform and model data for reporting.
5. Build Power BI pages for exploratory and descriptive analysis.

## Limitations

This project has several important limitations:

- It does **not** attempt to prove that halving events directly caused price movements.
- The number of historical halving cycles is small.
- Cross-asset comparisons around halving dates should be treated as descriptive context, not hard evidence of market dependency.
- Data sourcing and transformation are still being finalized, so the repository should be treated as an evolving portfolio project rather than a finished production system.

## Screenshots

### Dashboard preview

![BTC Halving Thesis dashboard](powerbi/screenshots/btc-halving-thesis-dashboard-page.png)

### Data model

![Power BI data model](powerbi/screenshots/btc-halving-thesis-data-model.png)

## Next steps

Planned next steps:
- finalize data ingestion and cleaned datasets,
- complete additional Power BI pages for cross-asset comparison and correlations,
- document transformation logic more clearly,
- add a notebook with supporting exploratory analysis,
- finalize repository structure and setup instructions.

## Why this project

I built this project as a portfolio piece to demonstrate practical skills in:
- event-based analysis,
- financial data preparation,
- dimensional modeling for reporting,
- Power BI dashboard design,
- combining Python, Power Query and BI reporting in one workflow.

## Repository note

This repository is being developed incrementally.  
The current version is intended to show a realistic MVP and visible progress rather than a fake “finished” project with empty structure.