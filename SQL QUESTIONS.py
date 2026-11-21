# Databricks notebook source
# MAGIC %md
# MAGIC # 1)For Sql use online sql compiler  if needed for Q1 and Q4
# MAGIC - LINK:[SQL LITE](https://sqliteonline.com/)
# MAGIC - ![STEP 1](/Volumes/code_test/cr_test/code_test/sql lite Cr.png)
# MAGIC - Below cells will contains Questions,sample input,reqyired output and table DDLs
# MAGIC - Once you get required output in Sql complier copy your qury here

# COMMAND ----------

# MAGIC %md
# MAGIC # Q1 Write the query to write the logic/approach
# MAGIC - ![Q1](/Volumes/code_test/cr_test/code_test/Q1 sql.png)
# MAGIC
# MAGIC ### - TABLE DDL
# MAGIC
# MAGIC `
# MAGIC CREATE TABLE BaseTable
# MAGIC (
# MAGIC      [ID] INT
# MAGIC     ,[Name] VARCHAR(10)
# MAGIC );
# MAGIC
# MAGIC  
# MAGIC INSERT INTO BaseTable VALUES
# MAGIC (1,'Ram'),
# MAGIC (2,'Sai'),
# MAGIC (3,'Ali'),
# MAGIC (4,'Venkat'),
# MAGIC (5,'Reinhard')
# MAGIC
# MAGIC SELECT * FROM BaseTable
# MAGIC `

# COMMAND ----------

# MAGIC %sql
# MAGIC Insert into BaseTable_new select * from BaseTable

# COMMAND ----------

# MAGIC %md
# MAGIC # Q2 Write the query to write the logic/approach
# MAGIC Given a employees table, write a query to find the employees who have been with the company for more than 10 years. employees:employee_id ,name ,hire_date ,salary

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from employees

# COMMAND ----------

# MAGIC %md
# MAGIC # Q3 Write the query to write the logic/approach
# MAGIC You're working with an e-commerce platform's orders table. The data engineering team wants to analyze repeat customers and their purchasing patterns — but with some constraints to evaluate your SQL skills.           
# MAGIC
# MAGIC
# MAGIC **Table: orders**
# MAGIC
# MAGIC ![2.1](/Volumes/code_test/cr_test/code_test/orders.png)
# MAGIC
# MAGIC
# MAGIC
# MAGIC **Question**                                                                                                            
# MAGIC Write a SQL query that returns the top 5 customers who have placed more than one order, along with:       - - -  
# MAGIC
# MAGIC
# MAGIC - customer_id
# MAGIC - customer_name
# MAGIC - total_orders
# MAGIC - total_spent
# MAGIC - first_order_date
# MAGIC - last_order_date
# MAGIC
# MAGIC
# MAGIC
# MAGIC **Rules:**
# MAGIC
# MAGIC
# MAGIC - Do NOT use any JOINs (only one table is involved).
# MAGIC - Do NOT use traditional scalar or correlated subqueries in SELECT or WHERE clauses.
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Q4 Write the query to write the logic/approach
# MAGIC ![2.1](/Volumes/code_test/cr_test/code_test/Q2.1.png)
# MAGIC ![2.2](/Volumes/code_test/cr_test/code_test/Q2.2.png)
# MAGIC
# MAGIC ## - Table DDL
# MAGIC `--Create Table
# MAGIC
# MAGIC
# MAGIC CREATE TABLE PhoneNumbers
# MAGIC (
# MAGIC      Id INT
# MAGIC     ,Name VARCHAR(10)
# MAGIC     ,MobileNum VARCHAR(100)
# MAGIC     ,ResidenceNum VARCHAR(100)
# MAGIC )
# MAGIC
# MAGIC --Insert Data
# MAGIC
# MAGIC
# MAGIC INSERT INTO PhoneNumbers VALUES
# MAGIC (1,'Joey','9762575422',NULL),
# MAGIC (2,'Ross', '9987796244','8762575402'),
# MAGIC (3,'Chandler',NULL,'7645764689'),
# MAGIC (4,'Monica','8902567839','7825367901'),
# MAGIC (5,'Rachel',NULL,'7845637289'),
# MAGIC (6,'Pheobe','9872435789','9838653469'),
# MAGIC (7,'Gunther',NULL,NULL),
# MAGIC (8,'Mike',NULL,'9700103678');
# MAGIC
# MAGIC --Verify Data
# MAGIC
# MAGIC
# MAGIC SELECT * FROM PhoneNumbers
# MAGIC
# MAGIC `

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # Q5 Write the query to write the logic/approach
# MAGIC Write a SQL query to calculate the running total of sales amounts for each product, partitioned by product_id and ordered by sale
# MAGIC
# MAGIC Table
# MAGIC sales :sale_id ,product_id ,sale_ amount
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select *,sum(sale_amount) as "running_total" over(partition by product_id order by sale_id) from sales