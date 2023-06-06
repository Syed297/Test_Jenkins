from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import pickle

# Load the iris dataset
iris = datasets.load_iris()

# Train a logistic regression model
model = LogisticRegression(max_iter=2000)
model.fit(iris.data, iris.target)

# Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")
