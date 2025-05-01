import sqlite3

# Connect (or create) the database
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Create a simple sales table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
''')

# Insert some sales data
sample_data = [
    ('Apple', 10, 0.5),
    ('Banana', 5, 0.3),
    ('Apple', 15, 0.5),
    ('Orange', 7, 0.7),
    ('Banana', 10, 0.3)
]
cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sample_data)
conn.commit()
conn.close()
