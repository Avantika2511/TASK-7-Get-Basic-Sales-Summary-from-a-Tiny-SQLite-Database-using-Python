## Task 7: Basic Sales Summary from SQLite Database

### **Objective:**
Create a Python script that connects to a small SQLite database, runs SQL queries to pull simple sales information (e.g., total quantity sold, total revenue), and displays the results using basic print statements and a bar chart.

### **Tools Used:**
- **Python** (with `sqlite3`, `pandas`, and `matplotlib`)
- **SQLite** (built into Python, no additional setup required)
- **Jupyter Notebook** or a `.py` script

### **Steps:**

1. **Create an SQLite Database (`sales_data.db`):**
   - The SQLite database contains a single `sales` table with columns:
     - `id` (INTEGER, primary key)
     - `product` (TEXT)
     - `quantity` (INTEGER)
     - `price` (REAL)
   - Sample sales data is inserted into the table.

2. **SQL Query:**
   - Write an SQL query to calculate the total quantity sold and total revenue by product:
     ```sql
     SELECT product, SUM(quantity) AS total_quantity, SUM(quantity * price) AS revenue
     FROM sales
     GROUP BY product;
     ```

3. **Load Data into Pandas DataFrame:**
   - Use the `pandas` library to load the results of the SQL query into a DataFrame for easier data manipulation and visualization.

4. **Display Results:**
   - Print the summary results (total quantity and revenue by product) to the console.

5. **Plot Bar Chart:**
   - Use `matplotlib` to create a simple bar chart showing revenue by product.
   - Customize the chart with labels for the title, x-axis, and y-axis.

6. **Save Chart (Optional):**
   - Optionally, save the generated bar chart as a `.png` file using `plt.savefig("sales_chart.png")`.

### **Outcome:**
- **Learned:**
  - Writing basic SQL queries to aggregate sales data.
  - Loading SQL query results into Python using `pandas`.
  - Creating simple data visualizations with `matplotlib`.

- **Delivered:**
  - Python script (or notebook) that:
    - Connects to an SQLite database (`sales_data.db`).
    - Runs SQL queries to summarize sales data.
    - Displays results via print statements and a bar chart.

### **Files:**
- `sales_data.db` – SQLite database containing sales data.
- `sales_summary.py` – Python script that performs the SQL query, processes the data, and visualizes it.
