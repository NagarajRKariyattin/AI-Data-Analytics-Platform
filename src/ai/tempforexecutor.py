from src.ai.sql_generator import generate_sql
from src.ai.executor import execute_sql

question = "Show total sales by region"

sql = generate_sql(question)

print("Generated SQL:")
print(sql)

print("\nQuery Result:")

df = execute_sql(sql)

print(df)