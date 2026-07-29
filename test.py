import joblib
import numpy as np

# LOAD FILES
model = joblib.load("model/ids_model.pkl")
scaler = joblib.load("model/scaler.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")

# CREATE DUMMY SAMPLE
sample = np.zeros((1, model.n_features_in_))

# SCALE SAMPLE
sample_scaled = scaler.transform(sample)

# PREDICT
pred = model.predict(sample_scaled)

# CONVERT LABEL
prediction = label_encoder.inverse_transform(pred)

print("Prediction:", prediction)