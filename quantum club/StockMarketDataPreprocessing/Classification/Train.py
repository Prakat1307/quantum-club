#  Train SVM and LSVM Models:
#  Use SVM and Linear SVM to classify the target variable.

from sklearn.svm import SVC, LinearSVC

# Train SVM model
svm_model = SVC(kernel='rbf')  # Radial basis function kernel
svm_model.fit(X_train, y_train)

# Train Linear SVM model
lsvm_model = LinearSVC()
lsvm_model.fit(X_train, y_train)