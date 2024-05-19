from xgboost import XGBClassifier

# Reducing the number of estimators further to limit training time
n_estimators = 20

# Train XGBoost models for each ball number with reduced estimators
model1 = XGBClassifier(n_estimators=n_estimators, random_state=42)
model1.fit(X_train1, y_train1)

model2 = XGBClassifier(n_estimators=n_estimators, random_state=42)
model2.fit(X_train2, y_train2)

model3 = XGBClassifier(n_estimators=n_estimators, random_state=42)
model3.fit(X_train3, y_train3)

model4 = XGBClassifier(n_estimators=n_estimators, random_state=42)
model4.fit(X_train4, y_train4)

model5 = XGBClassifier(n_estimators=n_estimators, random_state=42)
model5.fit(X_train5, y_train5)

model6 = XGBClassifier(n_estimators=n_estimators, random_state=42)
model6.fit(X_train6, y_train6)

# Predicting the next set of numbers
predicted_number1 = model1.predict(next_draw_features)
predicted_number2 = model2.predict(next_draw_features)
predicted_number3 = model3.predict(next_draw_features)
predicted_number4 = model4.predict(next_draw_features)
predicted_number5 = model5.predict(next_draw_features)
predicted_number6 = model6.predict(next_draw_features)

predicted_numbers = [predicted_number1[0], predicted_number2[0], predicted_number3[0], predicted_number4[0], predicted_number5[0], predicted_number6[0]]
predicted_numbers
