from pathlib import Path
import csv


data_file = Path("data/rainfall.csv")

with data_file.open(newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rainfall_values = [
        float(row["rainfall_mm"])
        for row in reader
    ]

average_rainfall = sum(rainfall_values) / len(rainfall_values)

print(f"Average monthly rainfall: {average_rainfall:.1f} mm")

average_rainfall = sum(rainfall_values) / len(rainfall_values)
minimum_rainfall = min(rainfall_values)
maximum_rainfall = max(rainfall_values)

print(f"Minimum monthly rainfall: {minimum_rainfall:.1f} mm")
print(f"Maximum monthly rainfall: {maximum_rainfall:.1f} mm")