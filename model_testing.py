import numpy as np
import pickle

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# New sample
sample = np.array([5.1, 3.5, 1.4, 0.2]).reshape(1, -1)

# Make a prediction
prediction = model.predict(sample)

print(f"Prediction for the sample is: {prediction}")
