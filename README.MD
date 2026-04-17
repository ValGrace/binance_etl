# Binance ETL Pipeline

A Python ETL (Extract, Transform, Load) pipeline that fetches cryptocurrency data from the Binance API, processes it, and stores it in a PostgreSQL database.

## Project Overview

This pipeline automates the collection of real-time cryptocurrency market data from Binance. It extracts data on prices, trades, order books, and candlestick charts (klines), transforms the data into a structured format, and loads it into PostgreSQL for analysis.

### Data Pipeline Flow
1. **Extract**: Fetches data from Binance REST API endpoints
2. **Transform**: Processes and structures data into pandas DataFrames
3. **Load**: Stores transformed data in PostgreSQL database tables

## Setup

### 1. Activate Virtual Environment
```bash
# Windows
binance_env\Scripts\activate

# macOS/Linux
source binance_env/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Database Connection
Create a `.env` file in the project root with your PostgreSQL credentials:
```
DB_NAME=your_database_name
DB_USER=your_db_user
DB_HOST=localhost
DB_PORT=5432
DB_PASSWORD=your_password
```

## Usage

Run the complete ETL pipeline:
```bash
python main.py
```

This will:
- Extract data from Binance API (prices, trades, order book, klines for BTCUSDT)
- Transform the data into structured DataFrames
- Load into PostgreSQL tables: `prices`, `recent_trades`, `recent_klines`, `latest_orders`

## Binance API Endpoints Used
- `https://api.binance.com/api/v3/ticker/price` - Current cryptocurrency prices
- `https://api.binance.com/api/v3/trades` - Recent trades
- `https://api.binance.com/api/v3/depth` - Order book (market depth)
- `https://api.binance.com/api/v3/klines` - Candlestick chart data 


