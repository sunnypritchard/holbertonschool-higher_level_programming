#!/usr/bin/python3
"""
Flask application that reads product data from JSON or CSV files
and displays them using Jinja2 templates.
"""
from flask import Flask, render_template, request
import json
import csv


app = Flask(__name__)


def read_json_file():
    """
    Read and parse data from products.json file.

    Returns:
        list: List of product dictionaries, or None if file not found/invalid
    """
    try:
        with open('products.json', 'r') as f:
            data = json.load(f)
            # Handle both formats: direct list or nested under "products" key
            if isinstance(data, list):
                return data
            elif isinstance(data, dict) and 'products' in data:
                return data['products']
            else:
                return None
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def read_csv_file():
    """
    Read and parse data from products.csv file.

    Returns:
        list: List of product dictionaries, or None if file not found/invalid
    """
    try:
        products = []
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert price to float and id to int
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(product)
        return products
    except (FileNotFoundError, ValueError, KeyError):
        return None


@app.route('/products')
def products():
    """
    Route to display products from JSON or CSV file.

    Query Parameters:
        source (str): Data source - 'json' or 'csv' (required)
        id (int): Optional product ID to filter by

    Returns:
        Rendered template with products or error message
    """
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html',
                             error="Wrong source")

    # Read data from the appropriate source
    if source == 'json':
        products_data = read_json_file()
    else:  # source == 'csv'
        products_data = read_csv_file()

    # Handle file reading errors
    if products_data is None:
        return render_template('product_display.html',
                             error=f"Error reading {source.upper()} file")

    # Filter by ID if provided
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products_data if p['id'] == product_id]

            if not filtered_products:
                return render_template('product_display.html',
                                     error="Product not found")

            products_data = filtered_products
        except ValueError:
            return render_template('product_display.html',
                                 error="Invalid product ID")

    # Render template with products
    return render_template('product_display.html', products=products_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
