# ⚡ BOM Datasheet & Telemetry Aggregator

> Stop searching for component datasheets one by one. Drop in your Bill of Materials (BOM), and get every datasheet PDF, real-time stock status, and volume price break in seconds.

## 🚀 Key Features
* **Batch Processing:** Pass a list of 50+ MPNs (Manufacturer Part Numbers) via `.csv` or text input.
* **Multi-Distributor API Ingestion:** Automatically fetches and normalizes raw JSON payloads from Mouser, DigiKey, and Nexar APIs.
* **Instant PDF Archiving:** Downloads and packages all project datasheets into a single structured directory or `.zip` file.
* **Price & Stock Optimization:** Aggregates live stock availability and tiered volume pricing across suppliers to optimize procurement costs.
* **Local Caching:** Stores fetched component specs in a PostgreSQL database to bypass rate limits and deliver lightning-fast responses.
