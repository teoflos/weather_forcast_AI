import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RAW_PATH = BASE_DIR / "data/raw_data.csv"
OUT_PATH = BASE_DIR / "data/monthly_timeseries.csv"

MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def main():
    df = pd.read_csv(RAW_PATH)
    
    print("Available years in source:", sorted(df["Year"].unique()))

    df = df[df["Name"] == "Addis Ababa"].copy()

    long_df = df.melt(
        id_vars=["Name", "ELEMENT", "Year", "Time"],
        value_vars=MONTHS,
        var_name="Month",
        value_name="Value",
    )

    monthly = (
        long_df.groupby(["ELEMENT", "Year", "Month"])["Value"]
        .mean()
        .reset_index()
    )

    month_num = {m: i + 1 for i, m in enumerate(MONTHS)}
    monthly["month_num"] = monthly["Month"].map(month_num)
    monthly["date"] = pd.to_datetime(
        dict(year=monthly["Year"], month=monthly["month_num"], day=1)
    )

    wide = monthly.pivot_table(index="date", columns="ELEMENT", values="Value")
    wide = wide.sort_index()


    wide = wide.rename(columns={
        "TMPMAX": "temp_max_C",
        "TMPMIN": "temp_min_C",
        "PRECIP": "precip_mm",
        "RELHUM": "rel_humidity_pct",
        "SUNHRS": "sun_hours",
        "WINDLY": "wind_speed",
    })

    wide.index.name = "date"
    wide.to_csv(OUT_PATH)

    print(f"Saved {len(wide)} monthly rows -> {OUT_PATH}")
    print("\nDate range:", wide.index.min(), "to", wide.index.max())
    print("\nMissing values per column:")
    print(wide.isna().sum())
    print("\nPreview:")
    print(wide.head(12))

if __name__ == "__main__":
    main()
