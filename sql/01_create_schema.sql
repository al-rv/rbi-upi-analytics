CREATE DATABASE IF NOT EXISTS rbi_warehouse;

USE rbi_warehouse;

CREATE TABLE IF NOT EXISTS dim_payment_method (
    payment_method_id INT AUTO_INCREMENT PRIMARY KEY,
    payment_method_name VARCHAR(100) NOT NULL UNIQUE
);

INSERT IGNORE INTO dim_payment_method (payment_method_name)
VALUES ('UPI');

CREATE TABLE IF NOT EXISTS dim_source_file (
    source_file_id INT AUTO_INCREMENT PRIMARY KEY,
    source_file_name VARCHAR(255) NOT NULL UNIQUE,
    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS fact_payment_indicators (
    payment_indicator_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    report_month DATE NOT NULL,
    payment_method_id INT NOT NULL,
    source_file_id INT NOT NULL,
    volume_lakh DECIMAL(18, 2),
    value_crore DECIMAL(18, 2),
    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_payment_method
        FOREIGN KEY (payment_method_id)
        REFERENCES dim_payment_method(payment_method_id),

    CONSTRAINT fk_source_file
        FOREIGN KEY (source_file_id)
        REFERENCES dim_source_file(source_file_id),

    CONSTRAINT unique_month_method
        UNIQUE (report_month, payment_method_id)
);