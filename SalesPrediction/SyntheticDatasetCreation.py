# Creating a synthetic dataset for the BigMart Sales Prediction project and providing the Python code for building
# the model:

import pandas as pd
import numpy as np

import random

# Set random seed for reproducibility
np.random.seed(42)

# Number of products and outlets
num_products = 1559
num_outlets = 10

# Generate product attributes
product_ids = [f'P{1000 + i}' for i in range(num_products)]
product_types = ['Food', 'Clothing', 'Household']
product_weights = np.random.uniform(5, 50, num_products)
product_visibility = np.random.uniform(0, 0.2, num_products)
product_prices = np.random.uniform(50, 500, num_products)

# Generate outlet attributes
outlet_ids = [f'O{i + 1}' for i in range(num_outlets)]
outlet_types = ['Supermarket', 'Grocery Store']
outlet_sizes = ['Small', 'Medium', 'Large']
outlet_locations = ['Tier 1', 'Tier 2', 'Tier 3']
outlet_establishment_year = np.random.randint(1980, 2020, num_outlets)

# Create DataFrames for products and outlets
products = pd.DataFrame({
    'Product_ID': product_ids,
    'Product_Type': np.random.choice(product_types, num_products),
    'Product_Weight': product_weights,
    'Product_Visibility': product_visibility,
    'Product_Price': product_prices
})

outlets = pd.DataFrame({
    'Outlet_ID': outlet_ids,
    'Outlet_Type': np.random.choice(outlet_types, num_outlets),
    'Outlet_Size': np.random.choice(outlet_sizes, num_outlets),
    'Outlet_Location': np.random.choice(outlet_locations, num_outlets),
    'Outlet_Establishment_Year': outlet_establishment_year
})

# Create synthetic sales data
sales_data = []

for product_id in products['Product_ID']:
    for outlet_id in outlets['Outlet_ID']:
        sales = np.random.uniform(100, 2000)  # Generate random sales
        sales_data.append([product_id, outlet_id, sales])

# Convert sales data into a DataFrame
sales_df = pd.DataFrame(sales_data, columns=['Product_ID', 'Outlet_ID', 'Sales'])

# Merge the sales data with product and outlet attributes
dataset = sales_df.merge(products, on='Product_ID').merge(outlets, on='Outlet_ID')

# Save the dataset to CSV
dataset.to_csv('bigmart_sales_data.csv', index=False)

print("Synthetic dataset created and saved as 'bigmart_sales_data.csv'.")
