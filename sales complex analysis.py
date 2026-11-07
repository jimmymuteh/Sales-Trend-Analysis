import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================================
# AUTO-CREATE SAMPLE FILES IF MISSING
# ==========================================
if not os.path.exists("sales_august.csv"):
    pd.DataFrame({
        "customer": ["Kamau Stores", "Otieno Wholesale", "Hassan Traders", "Shop A", "Shop B", "Shop C", "Shop D", "Shop E", "Shop F", "Shop G"],
        "region": ["Nairobi", "Kisumu", "Mombasa", "Nairobi", "Nakuru", "Kisumu", "Nairobi", "Nakuru", "Mombasa", "Nairobi"],
        "quantity": [100, 80, 120, 50, 40, 30, 20, 25, 35, 45],
        "price": [3000, 2500, 4000, 1500, 2000, 1800, 2200, 1600, 2500, 3000]
    }).to_csv("sales_august.csv", index=False)

if not os.path.exists("sales_september.csv"):
    pd.DataFrame({
        "customer": ["Kamau Stores", "Otieno Wholesale", "Hassan Traders", "Shop A", "Shop B"],
        "region": ["Nairobi", "Kisumu", "Mombasa", "Nairobi", "Nakuru"],
        "quantity": [110, 85, 130, 40, 20],
        "price": [3000, 2500, 4000, 1500, 2000]
    }).to_csv("sales_september.csv", index=False)


# ==========================================
# MAIN ANALYSIS SCRIPT
# ==========================================
os.makedirs("charts", exist_ok=True)

# Load and combine two months of data
august = pd.read_csv("sales_august.csv")
september = pd.read_csv("sales_september.csv")

august["month"] = "August"
september["month"] = "September"
df = pd.concat([august, september], ignore_index=True)
df["revenue"] = df["quantity"] * df["price"]

print(f"Combined: {len(df)} rows | Total revenue: KES {df['revenue'].sum():,.0f}")

# Month-over-Month Drop Calculation
monthly_rev = df.groupby("month")["revenue"].sum()
aug_rev = monthly_rev.get("August", 0)
sep_rev = monthly_rev.get("September", 0)
mom_drop_pct = ((sep_rev - aug_rev) / aug_rev) * 100

print("\n--- 1. REVENUE COMPARISON ---")
print(f"August Revenue: KES {aug_rev:,.0f}")
print(f"September Revenue: KES {sep_rev:,.0f}")
print(f"Change: {mom_drop_pct:.1f}%")

# Customer Tiers setup for charts
cust_monthly = df.pivot_table(index="customer", columns="month", values="revenue", aggfunc="sum").fillna(0)
def assign_tier(row):
    total = row.get("August", 0) + row.get("September", 0)
    if total > 150000:
        return "Tier 1 (High Value)"
    elif total > 50000:
        return "Tier 2 (Mid Value)"
    else:
        return "Tier 3 (Small Accounts)"

cust_monthly["tier"] = cust_monthly.apply(assign_tier, axis=1)
customer_totals = cust_monthly

# Multi-Plot Visualization
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Chart 1: Revenue by region
region_rev = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
region_rev.plot(kind="bar", ax=axes[0], color="#1F4E79")
axes[0].set_title("Revenue by Region (Aug-Sep)")
axes[0].set_ylabel("Revenue (KES)")

# Chart 2: Month-over-month comparison
monthly_rev.plot(kind="bar", ax=axes[1], color=["#1F4E79", "#4472C4"])
axes[1].set_title("Revenue: August vs September")
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=0)

# Chart 3: Customer tier distribution
customer_totals["tier"].value_counts().plot(kind="pie", ax=axes[2], autopct="%.0f%%", colors=["#1F4E79", "#4472C4", "#8EA9DB"])
axes[2].set_title("Customer Revenue Tiers")
axes[2].set_ylabel("")

plt.tight_layout()
plt.savefig("charts/project_analysis.png", dpi=150)
print("\nCharts successfully saved to charts/project_analysis.png.")