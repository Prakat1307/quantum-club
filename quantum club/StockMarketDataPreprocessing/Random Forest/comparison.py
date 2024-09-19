 #To compare the results of Random Forest with SVM and regression models you previously implemented

# Evaluate SVM model (for classification)
svm_accuracy = accuracy_score(y_test_clf, svm_predictions)
svm_precision = precision_score(y_test_clf, svm_predictions)
svm_recall = recall_score(y_test_clf, svm_predictions)
svm_f1 = f1_score(y_test_clf, svm_predictions)

print("\nSVM Model Evaluation:")
print(f'Accuracy: {svm_accuracy}')
print(f'Precision: {svm_precision}')
print(f'Recall: {svm_recall}')
print(f'F1 Score: {svm_f1}')

# Evaluate Linear Regression model (for regression)
y_pred_lr = linear_model.predict(X_test_reg)  

lr_rmse = np.sqrt(mean_squared_error(y_test_reg, y_pred_lr))
lr_mae = np.mean(np.abs(y_test_reg - y_pred_lr))

print("\nLinear Regression Model Evaluation:")
print(f'RMSE: {lr_rmse}')
print(f'MAE: {lr_mae}')