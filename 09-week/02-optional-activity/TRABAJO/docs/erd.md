# ERD — Tokyo Stock Exchange listing

```mermaid
erDiagram
    SECTOR17 ||--|{ SECTOR33 : "groups"
    SECTOR33 ||--o{ SECURITY : "classifies"
    MARKET_SEGMENT ||--o{ SECURITY : "lists"
    INDEX_SIZE ||--o{ SECURITY : "sizes"
    SECURITY ||--o{ PRICE_SNAPSHOT : "has"

    SECTOR17 {
        text sector17_code PK
        text sector17_name
    }
    SECTOR33 {
        text sector33_code PK
        text sector33_name
        text sector17_code FK
    }
    MARKET_SEGMENT {
        int segment_id PK
        text segment_name UK
    }
    INDEX_SIZE {
        text index_size_code PK
        text index_size_name
    }
    SECURITY {
        text securities_code PK
        text name
        text instrument_type "Equity | ETF/ETN | REIT/Fund"
        text section_products
        bool in_universe
        date effective_date
        int segment_id FK
        text sector33_code FK
        text index_size_code FK
    }
    PRICE_SNAPSHOT {
        text securities_code PK, FK
        date trade_date PK
        float close
        int issued_shares
        int market_cap
    }
```

## Cardinalities

| Relationship | Cardinality | Meaning |
|---|---|---|
| SECTOR17 → SECTOR33 | 1 : N (mandatory both sides) | each of the 33 sectors belongs to exactly one of the 17 macro-sectors; a macro-sector has one or more sectors |
| SECTOR33 → SECURITY | 1 : N (a sector may have 0 securities) | a security has exactly one sector (placeholder `NA` / `UNC` for funds / unclassified) |
| MARKET_SEGMENT → SECURITY | 1 : N | a security belongs to exactly one segment (Prime, Standard, Growth, ...) |
| INDEX_SIZE → SECURITY | 1 : N | a security has one TOPIX size class (or `NA`) |
| SECURITY → PRICE_SNAPSHOT | 1 : N | one snapshot per trade date; this file has one date per security, but the key allows a time series |

**Design notes.** The flat CSV mixes four reference attributes (segment, 33-sector, 17-sector, size) with the security itself, repeating their names thousands of times. Normalizing them into lookup tables removes that redundancy (3NF). `sector17` is *not* stored in `SECURITY` because it is functionally dependent on `sector33` (verified in the notebook: each 33-sector maps to exactly one 17-sector). Prices live in their own table because they change with time while the security's descriptive data does not. DDL: `sql/schema.sql`.
