# Create binary target variable
df['Target'] = (df['Percentage Change'] > 0).astype(int)