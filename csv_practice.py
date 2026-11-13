# Exercise 1: Get the file

import csv

from datetime import datetime


# Exercise 2: Read and print raw rows

with open("data/sales.csv", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# Exercise 3: Skip the header

with open("data/sales.csv", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)


# Exercise 4: Compute totals

total_revenue = 0

with open("data/sales.csv", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        line_total = price * quantity
        total_revenue += line_total

        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

# Exercise 5: Filter and write

total_rows = 0
written_rows = 0

with open("data/sales.csv", newline="") as input_file:
    reader = csv.reader(input_file)
    header = next(reader)

    with open("data/cleaned.csv", "w", newline="") as output_file:
        writer = csv.writer(output_file)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            total_rows += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])

            line_total = price * quantity

            if line_total > 100:
                writer.writerow([product, f"{price:.2f}", quantity, f"{line_total:.2f}"])
                written_rows += 1

print(f"Written {written_rows} rows out of {total_rows} original rows.")

# Exercise 6: csv.DictReader

dict_total_revenue = 0

with open("data/sales.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        line_total = price * quantity
        dict_total_revenue += line_total

        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")

print(f"DictReader total revenue: ${dict_total_revenue:.2f}")

# csv.reader returns lists and accesses values using numbered indexes.
# DictReader uses column names, making the code easier to read and understand.

# Exercise 7: Sales summary by product

product_summary = {}

with open("data/sales.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        line_total = price * quantity

        if product in product_summary:
            product_summary[product] += line_total
        else:
            product_summary[product] = line_total

print("\nSales Summary by Product:")

for product in sorted(product_summary):
    print(f"{product}: ${product_summary[product]:.2f}")


# Exercise 8: Append mode log

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as log_file:
    log_file.write(f"{timestamp} - Total revenue: ${total_revenue:.2f}\n")

print("Run log updated successfully.")

