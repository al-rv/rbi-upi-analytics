from pathlib import Path
import os
import pandas as pd
from sqlalchemy import create_engine, text


csv_file = Path("data/processed/upi_monthly.csv")

mysql_host = os.getenv("MYSQL_HOST", "127.0.0.1")
mysql_port = os.getenv("MYSQL_PORT", "3307")

engine = create_engine(
    f"mysql+pymysql://rbi_user:rbi_password@{mysql_host}:{mysql_port}/rbi_warehouse"
)

data = pd.read_csv(csv_file)

with engine.begin() as connection:
    payment_method_id = connection.execute(
        text("""
            SELECT payment_method_id
            FROM dim_payment_method
            WHERE payment_method_name = 'UPI'
        """)
    ).scalar_one()

    for _, row in data.iterrows():
        connection.execute(
            text("""
                INSERT IGNORE INTO dim_source_file (source_file_name)
                VALUES (:source_file_name)
            """),
            {"source_file_name": row["source_file"]},
        )

        source_file_id = connection.execute(
            text("""
                SELECT source_file_id
                FROM dim_source_file
                WHERE source_file_name = :source_file_name
            """),
            {"source_file_name": row["source_file"]},
        ).scalar_one()

        connection.execute(
            text("""
                INSERT IGNORE INTO fact_payment_indicators
                (
                    report_month,
                    payment_method_id,
                    source_file_id,
                    volume_lakh,
                    value_crore
                )
                VALUES
                (
                    :report_month,
                    :payment_method_id,
                    :source_file_id,
                    :volume_lakh,
                    :value_crore
                )
            """),
            {
                "report_month": row["report_month"],
                "payment_method_id": payment_method_id,
                "source_file_id": source_file_id,
                "volume_lakh": row["volume_lakh"],
                "value_crore": row["value_crore"],
            },
        )

print(f"Loaded {len(data)} records into MySQL.")