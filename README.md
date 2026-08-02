# BOM Datasheet Aggregator

A Python/Streamlit utility that consumes distributor REST APIs (Mouser, DigiKey, Nexar) to batch-fetch datasheets, current stock levels, and volume pricing for electronics components.

## Features

* **BOM Batch Processing:** Pass a list of MPNs via `.csv` or raw text to query multiple distributors at once.
* **Datasheet Downloader:** Pulls direct PDF links and packages them into a local `.zip` or directory.
* **Price & Stock Comparison:** Extracts tiered volume pricing to find the cheapest distributor for a build.
* **PostgreSQL Caching:** Caches component metadata locally to reduce external API calls and handle rate limits.
