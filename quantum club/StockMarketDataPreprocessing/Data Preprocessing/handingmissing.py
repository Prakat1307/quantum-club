missing_values = df.isnull().sum()
print(missing_values)

# Fill missing values
for column in df.columns:
    if df[column].dtype == 'object':  
        df[column].fillna(df[column].mode()[0], inplace=True)
    else:  # Numerical columns
        df[column].fillna(df[column].mean(), inplace=True)