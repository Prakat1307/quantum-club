#  Select relevant features for predicting the Last Traded Price. 
# You might choose features like Open, High, Low, Previous Close, Change, Percentage Change, and Volume.

# Define features and target variable
X = df[['Open', 'High', 'Low', 'Previous Close', 'Change', 'Percentage Change', 'Share Volume']]
y = df['Last Traded Price']