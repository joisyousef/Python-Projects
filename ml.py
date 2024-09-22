#machine learning (training and testing)
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
model =KNeighborsClassifier(n_neighbors=3)# "3" can be change in exam
model.fit(X_train,y_train)

#calculate accuracy
import sklearn.metrics import accuracy_score

#accuracy of train
y_pred_train=model.predict(X_train)
accuracy_score(y_train,y_pred_train)

#accuracy of test
y_pred_test=model.predict(X_test)
accuracy_score(y_test,y_pred_test)