PRAGMA foreign_keys = ON;

CREATE TABLE market_segment (
  segment_id   INTEGER PRIMARY KEY AUTOINCREMENT,
  segment_name TEXT NOT NULL UNIQUE
);
CREATE TABLE sector17 (
  sector17_code TEXT PRIMARY KEY,
  sector17_name TEXT NOT NULL
);
CREATE TABLE sector33 (
  sector33_code TEXT PRIMARY KEY,
  sector33_name TEXT NOT NULL,
  sector17_code TEXT NOT NULL REFERENCES sector17(sector17_code)
);
CREATE TABLE index_size (
  index_size_code TEXT PRIMARY KEY,
  index_size_name TEXT NOT NULL
);
CREATE TABLE security (
  securities_code TEXT PRIMARY KEY,
  name            TEXT NOT NULL,
  instrument_type TEXT NOT NULL CHECK (instrument_type IN ('Equity','ETF/ETN','REIT/Fund')),
  section_products TEXT NOT NULL,
  in_universe     INTEGER NOT NULL,
  effective_date  TEXT NOT NULL,
  segment_id      INTEGER NOT NULL REFERENCES market_segment(segment_id),
  sector33_code   TEXT NOT NULL REFERENCES sector33(sector33_code),
  index_size_code TEXT NOT NULL REFERENCES index_size(index_size_code)
);
CREATE TABLE price_snapshot (
  securities_code TEXT NOT NULL REFERENCES security(securities_code),
  trade_date      TEXT NOT NULL,
  close           REAL NOT NULL,
  issued_shares   INTEGER NOT NULL,
  market_cap      INTEGER NOT NULL,
  PRIMARY KEY (securities_code, trade_date)
);
