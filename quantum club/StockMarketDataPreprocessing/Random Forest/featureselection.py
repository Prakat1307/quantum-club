# Features for regression (predicting Last Traded Price)
X_regression = df[['Open', 'High', 'Low', 'Previous Close', 'Change', 'Share Volume']]
y_regression = df['Last Traded Price']

# Features for classification (predicting Percentage Change)
X_classification = df.drop(columns=['Target', 'Percentage Change', 'Last Traded Price'])
y_classification = df['Target']