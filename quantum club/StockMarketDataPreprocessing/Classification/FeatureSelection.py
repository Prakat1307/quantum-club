# Define features and target variable
X = df.drop(columns=['Target', 'Percentage Change', 'Last Traded Price'])  
y = df['Target']