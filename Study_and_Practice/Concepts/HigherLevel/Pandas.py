import pandas as pd
import numpy as np


# File path is given along with delimiter to make it look neat
df = pd.read_csv('/Data/hotel-booking-data.txt', delimiter='\t')
# Removing all the slashes from the file
df = df.replace(r"\\", "", regex=True)

# Prints the first 5 rows to give an idea about the data
print(df.head())
print("\n ****** \n")

# Gives some basic values like count, frequency, etc.
print(df.describe())
print("\n ****** \n")

# Counts the occurrences of each Company
company_booking_count = df['Company'].value_counts()
print(company_booking_count)
print("\n ****** \n")

# Remove the incorrect rows like Hotels NaN
# df.dropna(inplace=True) will replace the file after removal
cln_data = df.dropna()
print(cln_data)
print("\n ****** \n")

# Convert to numeric and set invalid values as NaN
df['Room number'] = pd.to_numeric(df['Room number'], errors='coerce')
print(df)
print("\n ****** \n")

# Creates a new column which is twice the room numbers
df['Room Two'] = df['Room number'] * 2
print(df)
print("\n ****** \n")

# Checks for True or False in the column values
mask = df['Room number'].isna()
df['Booking Site'] = np.where(mask, df['Date'], np.nan)
print(df)
print("\n ****** \n")

# Replace the NaN values by back-filling
df['Booking Site'] = df['Booking Site'].bfill()
print(df)
print("\n ****** \n")

# Now drop the NaN values
final_data = df.dropna()
print(final_data)
print("\n ****** \n")

# Count the bookings made through each booking site
booking_sites = df['Booking Site'].value_counts()
print(booking_sites)
print("\n ****** \n")
