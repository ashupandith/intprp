# Data Architecture (Databricks, Synapse, Fabric, Databases)

## Interview Positioning

Show that you can connect data architecture to business outcomes:
- trusted data products
- faster decision cycles
- AI readiness
- governance at scale

## Platform Positioning Cheat Sheet

- Databricks:
  - Strong for advanced engineering + data science + lakehouse flexibility
  - Excellent for mixed batch/stream processing and ML platform needs
- Synapse:
  - Integrated analytics in Azure ecosystem, SQL-heavy enterprise patterns
  - Good fit when data warehouse and BI integration are central
- Fabric:
  - Unified SaaS-style analytics experience, strong Microsoft integration
  - Useful for simplified operations and broad business analytics adoption

## Lakehouse Patterns

- Bronze: raw ingestion, immutable where possible
- Silver: cleansed and standardized datasets
- Gold: business-ready aggregates and data products

Key points:
- enforce schema evolution strategy
- define data quality contracts and SLAs
- include lineage and metadata from day 1

## Streaming and CDC Patterns

- CDC pipelines for operational data synchronization
- Event streaming for near-real-time analytics
- Exactly-once semantics where required by business rules
- Replay and backfill strategy for reliability

## Governance and Security

- Data classification and access policies
- Row/column-level security for sensitive domains
- Catalog + lineage (Purview or equivalent)
- Tokenized access and secretless runtime patterns

