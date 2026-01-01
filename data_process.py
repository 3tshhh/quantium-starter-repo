import csv
from pathlib import Path

data = Path("./data")
with open("filtered_data.csv", "a", newline="") as output_file:
    daily_sales_write = csv.writer(output_file,delimiter=",")
    line_count = 0
    for file in data.glob("*.csv"):
        with open(file) as daily_sales:
            daily_sales_read = csv.reader(daily_sales, delimiter=',')
            for row in daily_sales_read:
                if line_count == 0:
                    daily_sales_write.writerow(["Sales", "Date", "Region"])
                    line_count += 1
                if row[0].lower() == "pink morsel":
                    price = float(row[1].replace("$", "").strip())
                    quantity = float(row[2])
                    pink_sale = price * quantity
                    daily_sales_write.writerow([pink_sale, row[3], row[4]])
                line_count += 1