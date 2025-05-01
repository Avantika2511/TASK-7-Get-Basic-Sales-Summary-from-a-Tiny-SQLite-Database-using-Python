import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to the SQLite database
conn = sqlite3.connect('sales_data.db')

# Step 2: SQL query to get total quantity and revenue
query = '''
SELECT 
    product,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
'''

# Step 3: Load the results of the query into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Step 4: Close the database connection
conn.close()

# Step 5: Print the DataFrame (you should see the data in the console)
print(df)

# Step 6: Plot a simple bar chart
df.plot(kind='bar', x='product', y='revenue', legend=False, color='skyblue')

# Step 7: Add chart labels
plt.title('Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue ($)')
plt.tight_layout()

# Step 8: Show the plot
plt.show()

# Step 9: Save the plot if needed
##plt.savefig("sales_chart.png")
