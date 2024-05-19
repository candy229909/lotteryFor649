from sklearn.neighbors import KNeighborsClassifier

# Train KNN models for each ball number
model1 = KNeighborsClassifier(n_neighbors=5)
model1.fit(X_train1, y_train1)

model2 = KNeighborsClassifier(n_neighbors=5)
model2.fit(X_train2, y_train2)

model3 = KNeighborsClassifier(n_neighbors=5)
model3.fit(X_train3, y_train3)

model4 = KNeighborsClassifier(n_neighbors=5)
model4.fit(X_train4, y_train4)

model5 = KNeighborsClassifier(n_neighbors=5)
model5.fit(X_train5, y_train5)

model6 = KNeighborsClassifier(n_neighbors=5)
model6.fit(X_train6, y_train6)

# Predicting the next set of numbers
predicted_number1 = model1.predict(next_draw_features)
predicted_number2 = model2.predict(next_draw_features)
predicted_number3 = model3.predict(next_draw_features)
predicted_number4 = model4.predict(next_draw_features)
predicted_number5 = model5.predict(next_draw_features)
predicted_number6 = model6.predict(next_draw_features)

predicted_numbers_knn = [predicted_number1[0], predicted_number2[0], predicted_number3[0], predicted_number4[0], predicted_number5[0], predicted_number6[0]]
predicted_numbers_knn
