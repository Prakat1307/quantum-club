#  Create a new binary target variable based on the "Percentage Change" column.
# Create binary target variable
df['Target'] = (df['Percentage Change'] > 0).astype(int)  # 1 for positive, 0 for negative