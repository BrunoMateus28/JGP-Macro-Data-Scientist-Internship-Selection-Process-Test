import pandas as pd

# Load the CSV file
df = pd.read_csv('cpi_data.csv')

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')

# Filter data for "All items" and "Gasoline"
df['series 2'] = pd.to_numeric(df['series 2'], errors='coerce')  # All items
df['series 3'] = pd.to_numeric(df['series 3'], errors='coerce')  # Gasoline

# Merge the data on 'date'
df_filtered = df[['date', 'series 2', 'series 3']].dropna()

# Calculate the correlation
correlation = df_filtered['series 2'].corr(df_filtered['series 3'])

print(f'Correlation between All items and Gasoline prices: {correlation}')
