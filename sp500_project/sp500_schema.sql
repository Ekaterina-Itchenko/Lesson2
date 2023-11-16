CREATE TABLE companies (
    symbol TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    sector TEXT NOT NULL,
    price REAL NOT NULL,
    price_earnings REAL DEFAULT NULL,
    dividend_yield REAL DEFAULT NULL,
    earnings_share REAL DEFAULT NULL,
    week_low REAL DEFAULT NULL,
    week_high REAL DEFAULT NULL,
    market_cap INTEGER DEFAULT NULL,
    ebitda INTEGER DEFAULT NULL,
    price_sales REAL DEFAULT NULL,
    price_book REAL DEFAULT NULL,
    sec_filings TEXT DEFAULT NULL
);
