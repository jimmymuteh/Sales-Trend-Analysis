# Multi-Month Sales Performance & Revenue Trend Analysis

Automated data pipeline built in Python and Pandas to ingest, combine, and analyze monthly distributor sales records, evaluating regional revenue contribution, customer concentration, and seasonal drop-offs.

## Executive Findings & Business Insights

* **Month-over-Month Revenue Drop:** Total revenue fell **12.7%** from August to September, contracting from **KES 892K to KES 778K**.
* **Regional Dominance:** Nairobi remains the strongest region, contributing **61% of total revenue** despite accounting for only **38% of total orders**.
* **Concentrated Growth:** Three core accounts—**Kamau Stores, Otieno Wholesale, and Hassan Traders**—account for **47% of all revenue** and grew **30–41%** in September. This confirms that the overall portfolio decline came entirely from smaller, volatile retail accounts.
* **Dormant Revenue Opportunity:** **8 customers** who actively ordered in August failed to reorder in September, representing **KES 145K in dormant revenue** that requires immediate sales outreach before the end of the quarter.

## Technical Stack

* **Language:** Python 3.x
* **Core Libraries:** `pandas` (aggregation, pivot tables, filtering), `matplotlib` (multi-panel data visualization), `os` (file automation and directory management).

## Outputs Generated

* **`charts/project_analysis.png`**: A 3-panel professional dashboard displaying regional revenue distribution, month-over-month comparison bars, and customer tier breakdowns.

