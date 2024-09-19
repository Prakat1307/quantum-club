#  valuate both models using accuracy, precision, recall, and F1-score

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Evaluate SVM model
print("SVM Model Evaluation:")
print(f'Accuracy: {accuracy_score(y_test, svm_predictions)}')
print(f'Precision: {precision_score(y_test, svm_predictions)}')
print(f'Recall: {recall_score(y_test, svm_predictions)}')
print(f'F1 Score: {f1_score(y_test, svm_predictions)}')

# Evaluate LSVM model
print("\nLinear SVM Model Evaluation:")
print(f'Accuracy: {accuracy_score(y_test, lsvm_predictions)}')
print(f'Precision: {precision_score(y_test, lsvm_predictions)}')
print(f'Recall: {recall_score(y_test, lsvm_predictions)}')
print(f'F1 Score: {f1_score(y_test, lsvm_predictions)}')