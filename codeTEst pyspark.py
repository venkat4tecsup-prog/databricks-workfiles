# Databricks notebook source
#import module here if required


# COMMAND ----------

# MAGIC %md
# MAGIC **ITS NOT MANDATORY TO DO EVERYTHING,IF POSSIBLE DO ALL,EACH QUESTION HAS ITS OWN EVALAUTION CHECKPOINTS**
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # **PYTHON**
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Implement a function** that takes a list of integers and returns the sum of all numbers that are greater than the average of their immediate neighbors (previous and next). The first and last elements are ignored.                   
# MAGIC Example:
# MAGIC Input: [4, 5, 8, 10, 7, 6]                                                                                           
# MAGIC Output: 18 (because 8 and 10 satisfy the condition)

# COMMAND ----------

#TYPE here


def sum_greater_than(arr):
    if len(arr) < 3 :
        return 0
# check
    total = 0
    for i in range (1, len(arr)-1):
        avg = (arr[i-1] + arr[i+1])/2
        if arr[i] >avg :
            total = total + arr[i]
    return total

print(sum_greater_than([4,5,8,10,7,6]))


# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # **PYSPARK**
# MAGIC - > can use pyspark or psql for doing below
# MAGIC - >Try to solve the below questions as far as possible,if not able to please write the logic you have in mind
# MAGIC - > If require can import neccessary modules
# MAGIC - > please avoid overwriting or clearing the output cell which are already shown,do chnages or display in new cells only
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ###Q1:Basic I/o test
# MAGIC > - Read the below mentioned csv  file from specified location
# MAGIC > - file_path:/Volumes/code_test/cr_test/code_test/titanic.csv
# MAGIC > - TSV sep
# MAGIC > - Output 1: Need to give me total count
# MAGIC > - Output 2 :top 10 rows and output should only have these columns[PassengerId,Name,Age,Sex]

# COMMAND ----------

#file path
path='/Volumes/code_test/cr_test/code_test/titanic.csv'

# COMMAND ----------

# DBTITLE 1,891
#code here to get count result as below
path='/Volumes/code_test/cr_test/code_test/titanic.csv'
df = spark.read.option("header", True).option ("inferSchema", True).csv(path)
df.createOrReplaceTempView("titanic")

count = spark.sql("select count(*) From titanic limit 2")

display(count)




# COMMAND ----------

#top 10 rows and only 

Output 2 :top 10 rows and output should only have these columns[PassengerId,Name,Age,Sex]
df=#code here



# COMMAND ----------

# MAGIC %md
# MAGIC ###Q2:Scenario Based
# MAGIC You are working as a data engineer for an e-commerce platform that is launching a customer loyalty program. The marketing team wants to identify the first purchase date and transaction ID for each customer, so they can send a welcome reward.
# MAGIC You have a transactions table with the following schema:
# MAGIC •	customer_id (string)
# MAGIC •	transaction_id (string)
# MAGIC •	timestamp (string, ISO format)
# MAGIC •	amount (double)
# MAGIC
# MAGIC As the senior data engineer, how would you extract the full row corresponding to the first purchase for each customer?
# MAGIC
# MAGIC

# COMMAND ----------

#WRITE THE PYSPARL OR PYSQL CODE

# COMMAND ----------

# MAGIC %md
# MAGIC ###Q3:Dataframe operations
# MAGIC > - Create a df using below data ans schema and get all the outputs like below

# COMMAND ----------

simpleData = (("James", "Sales", 3000), \
("Michael", "Sales", 4600),  \
("Robert", "Sales", 4100),   \
("Maria", "Finance", 3000),  \
("James", "Sales", 3000),    \
("Scott", "Finance", 3300),  \
("Jen", "Finance", 3900),    \
("Jeff", "Marketing", 3000), \
("Kumar", "Marketing", 2000),\
("Saif", "Sales", 4100) \
)

columns= ["employee_name", "department", "salary"]

# COMMAND ----------

df= spark.createDataframe(simpleData,columns)

# COMMAND ----------

#display here

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ###Q3.1:

# COMMAND ----------

sal_df1=#code here

# COMMAND ----------

#display here

# COMMAND ----------

display(sal_df1)

# COMMAND ----------

# MAGIC %md
# MAGIC ###Q3.2:

# COMMAND ----------

sal_df2=#code here

# COMMAND ----------

#display here

# COMMAND ----------

display(sal_df2)

# COMMAND ----------

# MAGIC %md
# MAGIC ###Q3.3:

# COMMAND ----------

sal_df3=

# COMMAND ----------

#display here

# COMMAND ----------

display(sal_df3)

# COMMAND ----------

# MAGIC %md
# MAGIC ###Q4:Dataframe operations
# MAGIC > - Provided my input df and output df
# MAGIC > - Write code to get below out
# MAGIC > - HINT: rotate a DataFrame from a long format (many rows, few columns) to a wide format (fewer rows, many columns)

# COMMAND ----------

data = [("Banana",1000,"USA"), ("Carrots",1500,"USA"), ("Beans",1600,"USA"), \
      ("Orange",2000,"USA"),("Orange",2000,"USA"),("Banana",400,"China"), \
      ("Carrots",1200,"China"),("Beans",1500,"China"),("Orange",4000,"China"), \
      ("Banana",2000,"Canada"),("Carrots",2000,"Canada"),("Beans",2000,"Mexico")]

columns= ["Product","Amount","Country"]
df = spark.createDataFrame(data = data, schema = columns)
display(df)

# COMMAND ----------

#code here

# COMMAND ----------

#display here

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ###Q5:Dataframe operations

# COMMAND ----------

arrayData = [('James',['Java','Scala']),
        ('Michael',['Spark','Java',None]),
        ('Robert',['CSharp','']),
        ('Washington',None),
        ('Jefferson',['1','2'])]

df = spark.createDataFrame(data=arrayData, schema = ['name','knownLanguages'])
display(df)

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC # **CAN WE IMPROVE/FIND MISTAKES IN BELOW CODE FURTHER**
# MAGIC - ![Q1](/Volumes/code_test/cr_test/code_test/pyspark debug 1.png)

# COMMAND ----------

# MAGIC %md
# MAGIC # **ADF**

# COMMAND ----------

# MAGIC %md
# MAGIC 1)Your company wants to run a daily data pipeline in Azure Data Factory to move data from Azure Blob Storage to Azure SQL Database. However, if there are no new files in Blob Storage for a given day, the pipeline should send an email alert instead of executing the data load. How would you design this

# COMMAND ----------

# MAGIC %md
# MAGIC 2)XYZ Ltd. hosts a critical MySQL database inside an on-premises VM running in a private subnet behind a firewall. You’re asked to design an Azure Data Factory (ADF) pipeline to extract data from this VM daily
# MAGIC How would you configure the ADF pipeline to securely access the MySQL database on the on‑premises VM? 