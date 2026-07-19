from src.ai.sql_generator import generate_sql

question = "Show total sales by region"

sql = generate_sql(question)

print(sql)