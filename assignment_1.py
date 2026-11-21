# Databricks notebook source
# 1.Read the orders.csv file into a DataFrame.

# 2. Select the following columns only:
# order_id, customer_name, product, amount, status, city

# 3. Remove duplicates:
# Assume an order is duplicated if all fields in a row are identical.

# 4. Filter the data to include only:
# Orders where amount > 100

# 5. Use OR operator to keep:
# Rows where status is "Shipped" OR "Pending"

# 6. Use AND operator to narrow down:
# Rows where amount > 200 AND status = 'Shipped'

# 7. Use IN operator to retain:
# Orders from customers located in New York, Chicago, San Francisco

# 8. Sort the DataFrame in ascending order of amount.


# 9.
# DataFrame actions:
# Show top 5 rows
# Print the total number of final transactions
# Print the schema of the final DataFrame.

# COMMAND ----------

from pyspark.sql.functions import col

# Step 1️⃣: Create the DataFrame
orders_data = [
    (101, 1, "Alice", "Laptop", 1200, "Shipped", "New York"),
    (102, 2, "Bob", "Mouse", 25, "Failed", "Chicago"),
    (103, 3, "Charlie", "Keyboard", 75, "Shipped", "Los Angeles"),
    (104, 1, "Alice", "Monitor", 300, "Shipped", "New York"),
    (105, 2, "Bob", "Laptop", 1200, "Shipped", "Chicago"),
    (106, 1, "Alice", "Monitor", 300, "Shipped", "New York"),
    (107, 4, "David", "Desk", 200, "Cancelled", "Chicago"),
    (108, 5, "Eva", "Chair", 150, "Shipped", "San Francisco"),
    (109, 6, "Frank", "Mouse", 25, "Shipped", "New York"),
    (110, 3, "Charlie", "Laptop", 1200, "Failed", "Los Angeles")
]

columns = ["order_id", "customer_id", "customer_name", "product", "amount", "status", "city"]

orders_df = spark.createDataFrame(orders_data, columns)

# ================================
# 2️⃣ Select specific columns
# ================================
selected_df = orders_df.select("order_id", "customer_name", "product", "amount", "status", "city")

print("Selected columns:")
display(selected_df)

# # ================================
# # 3️⃣ Remove duplicates (if all fields match)
# ================================
deduped_df = selected_df.dropDuplicates()

print("After removing duplicates:")
display(deduped_df)

# # ================================
# # 4️⃣ Filter rows where amount > 100
# # ================================
filtered_df = deduped_df.filter(col("amount") > 100)

print("Orders where amount > 100:")
display(filtered_df)

# # ================================
# # 5️⃣ Keep rows where status is 'Shipped' OR 'Pending'
# # ================================
or_filtered_df = filtered_df.filter(
    (col("status") == "Shipped") | (col("status") == "Pending")
)

print("Orders where status is Shipped or Pending:")
display(or_filtered_df)

# # ================================
# # 6️⃣ Keep rows where amount > 200 AND status = 'Shipped'
# # ================================
and_filtered_df = deduped_df.filter(
    (col("amount") > 200) & (col("status") == "Shipped")
)

print("Orders where amount > 200 and status = 'Shipped':")
display(and_filtered_df)

# # ================================
# # 7️⃣ Keep orders from selected cities (IN operator)
# # ================================
in_filtered_df = deduped_df.filter(
    col("city").isin(["New York", "Chicago", "San Francisco"])
)

print("Orders from New York, Chicago, or San Francisco:")
display(in_filtered_df)

# # ================================
# # 8️⃣ Sort DataFrame by amount ascending
# # ================================
sorted_df = in_filtered_df.orderBy(col("amount").asc())

print("Sorted by amount ascending:")
display(sorted_df)

# # ================================
# # 9️⃣ Actions
# # ================================
print("Show top 5 rows:")
sorted_df.show(5, truncate=False)

print("Total number of transactions:")
print(sorted_df.count())

print("Schema of final DataFrame:")
sorted_df.printSchema()
