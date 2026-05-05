# Corporate Finance Engine

A Python pipeline that fetches real financial data from Yahoo Finance,
maps it to standard corporate finance variables, and calculates key
financial metrics automatically.

Built to automate what analysts do manually: pulling data, cleaning it,
and running the calculations.

---

## What it does

Given a ticker symbol and a year, the pipeline:

1. Fetches income statement, balance sheet and cash flow data from Yahoo Finance
2. Maps raw Yahoo columns to standard financial variables (ric_op_mon, cost_op_mon, ammort, etc.)
3. Resolves and validates inputs — required fields raise errors, optional fields default to zero
4. Calculates financial metrics via pure Python functions

**Currently calculated:**
- MOL (Margine Operativo Lordo / EBITDA proxy)
- ROL (Risultato Operativo Lordo / EBIT proxy)
- FCCNOGC (Flusso di Cassa del Capitale Circolante Netto Operativo della Gestione Caratteristica)

**Verified on:** Ferrari N.V. (RACE) 2023, 2024, 2025 — figures cross-checked
against official annual reports from Ferrari investor relations.

---

## Verification

Outputs verified against Ferrari N.V. (RACE) official Annual Report 2025.
Differences are rounding artifacts from Yahoo Finance reporting in millions.

Source: Ferrari N.V. Annual Report 2025 — Consolidated Income Statement.

---

## Usage

```bash
python executioner.py
```

To change ticker or year, edit the last line of `executioner.py`:

```python
main("RACE", year=2025)
```

---

## Project structure

| File | Role |
|---|---|
| `yahoo_fetcher.py` | Downloads data from Yahoo Finance and maps columns to calculator keys |
| `resolver.py` | Validates and cleans fetcher output before passing to formulas |
| `formulas.py` | Pure Python financial functions, no external dependencies |
| `executioner.py` | Entry point — orchestrates the pipeline |

---
## Architecture
Yahoo Finance
↓
yahoo_fetcher.py   (fetch + map columns)
↓
resolver.py        (validate + clean)
↓
formulas.py        (calculate)
↓
output

`formulas.py` has no dependencies on Yahoo, the resolver, or any
interface — every function can be called and tested independently.

---

## Requirements
yahooquery
pandas

Install:

```bash
pip install yahooquery pandas
```

---

## Status

| Feature | Status |
|---|---|
| Yahoo Finance fetcher | Complete |
| Semantic mapping (RACE verified) | Complete |
| MOL, ROL, FCCNOGC | Complete |
| Full cash flow pipeline (FCGC, FCID, FCU, FCE) | In progress |
| Ratio analysis (ROS, ROI, ROE) | In progress |
| Multi-year loop | Planned |
| UI layer | Planned |
| Report output (PDF/Excel) | Planned |

---

## License

