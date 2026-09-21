# RBI UPI Payment Analytics Platform

An end-to-end data engineering and Power BI project using monthly UPI data from the Reserve Bank of India.

## Architecture

![Figure 1. System architecture of the RBI UPI payment analytics platform.](figures/architecture.svg)

*Figure 1.* System architecture of the RBI UPI payment analytics platform. Monthly RBI PSI Excel files are extracted and validated by a Python ETL pipeline orchestrated with Apache Airflow (Docker), loaded into a MySQL star-schema warehouse, enriched via SQL views, and consumed in Power BI.

## Project Highlights

* Processed 36 monthly RBI files
* Covered August 2023 to July 2026
* Extracted UPI transaction volume and value
* Built a dimensional MySQL warehouse
* Automated the pipeline using Apache Airflow
* Added data-quality checks and Pytest tests
* Created SQL views for analytical reporting
* Built an interactive Power BI dashboard

## Technology Stack

* Python, Pandas, OpenPyXL
* Apache Airflow
* Docker and Docker Compose
* MySQL
* SQLAlchemy and PyMySQL
* Pytest
* Power BI Desktop

## Pipeline Tasks

```text
extract_upi → validate_data → load_mysql
```

The pipeline calculates:

* Monthly transaction volume
* Monthly transaction value
* Average transaction value
* Month-over-month growth


## How to Run

Start the services:

```powershell
docker compose up -d
```

Open Airflow:

```text
http://localhost:8080
```

Trigger the `rbi_upi_pipeline` DAG.

Run tests:

```powershell
pytest
```

Power BI connects to:

```text
Server: 127.0.0.1:3307
Database: rbi_warehouse
```

## Project Outcome

This project demonstrates practical skills in Python ETL, Airflow orchestration, Docker, MySQL warehousing, SQL analytics, data validation, and Power BI reporting.
