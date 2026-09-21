USE rbi_warehouse;

CREATE OR REPLACE VIEW vw_upi_monthly_trends AS
SELECT
    f.report_month,
    p.payment_method_name,
    f.volume_lakh,
    f.value_crore,
    ROUND((f.value_crore * 100) / NULLIF(f.volume_lakh, 0), 2)
        AS average_transaction_value,

    LAG(f.volume_lakh) OVER (
        ORDER BY f.report_month
    ) AS previous_volume_lakh,

    ROUND(
        (
            f.volume_lakh
            - LAG(f.volume_lakh) OVER (ORDER BY f.report_month)
        )
        / NULLIF(
            LAG(f.volume_lakh) OVER (ORDER BY f.report_month),
            0
        ) * 100,
        2
    ) AS volume_growth_percent

FROM fact_payment_indicators f
JOIN dim_payment_method p
    ON f.payment_method_id = p.payment_method_id
WHERE p.payment_method_name = 'UPI';