from sklearn.metrics import mean_squared_error, accuracy_score, precision_score, recall_score, f1_score
import numpy as np

# Evaluate Regression Model using RMSE and MAE
rmse_rf = np.sqrt(mean_squared_error(y_test_reg, y_pred_reg))
mae_rf = np.mean(np.abs(y_test_reg - y_pred_reg))

print("Random Forest Regression Model Evaluation:")
print(f'RMSE: {rmse_rf}')
print(f'MAE: {mae_rf}')

# Evaluate Classification Model using accuracy, precision, recall, and F1-score
accuracy_rf = accuracy_score(y_test_clf, y_pred_clf)
precision_rf = precision_score(y_test_clf, y_pred_clf)
recall_rf = recall_score(y_test_clf, y_pred_clf)
f1_rf = f1_score(y_test_clf, y_pred_clf)

print("\nRandom Forest Classification Model Evaluation:")
print(f'Accuracy: {accuracy_rf}')
print(f'Precision: {precision_rf}')
print(f'Recall: {recall_rf}')
print(f'F1 Score: {f1_rf}')