#!/usr/bin/python3
"""
Script to create and populate the SQLite database for products.
"""
import sqlite3


def create_database():
    """
    Create products.db database and populate it with sample data.
    """
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Create Products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Clear existing data to avoid duplicates
    cursor.execute('DELETE FROM Products')

    # Insert sample data
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')

    conn.commit()
    conn.close()

    print("Database 'products.db' created and populated successfully!")


if __name__ == '__main__':
    create_database()
