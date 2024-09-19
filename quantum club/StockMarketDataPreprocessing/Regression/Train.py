#  Use a regression model such as Linear Regression to fit the training data.

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)