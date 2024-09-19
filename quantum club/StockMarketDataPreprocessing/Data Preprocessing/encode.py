# Encode Categorical Variables:
# Convert categorical variables such as "Industry" and "Series" into numerical format using one-hot encoding.

df = pd.get_dummies(df, columns=['Industry', 'Series'], drop_first=True)
