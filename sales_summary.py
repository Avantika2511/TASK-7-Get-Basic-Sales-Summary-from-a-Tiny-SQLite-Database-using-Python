import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('sales_data.db')

# Write SQL to get total quantity and revenue
query = '''
SELECT 
    product,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
'''

# Load results into a DataFrame
df = pd.read_sql_query(query, conn)
conn.close()

# Show the summary in the console
print(df)
