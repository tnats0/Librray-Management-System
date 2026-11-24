# Repository Specific Guidance

## Setup & Dependencies
*   Requires Python 3.10+ and specific libraries: `mysql-connector-python`, `python-dotenv`, `requests`, `opencv-python`, `pyzbar`, `rich`.
*   **Environment:** Must set `API_KEY` in a local `.env` file for API lookups.

## Operational Quirks
*   **API Retry:** The `add` function implements a 503 status code retry loop with a random sleep (1-5 seconds) when searching for books using `find_book`.
*   **Data Check:** Always verify if a book exists in the database using `check_data(code)` before attempting API searches or insertions.
*   **Barcode:** Barcode decoding relies on `opencv-python` and `pyzbar` utilities.

## Entrypoints
*   Primary CLI interaction is through `main.py` functions (`add`, `menu`).
*   Database SQL scripts are located in `database/Queries/` (e.g., `init.sql`, `seed.sql`).