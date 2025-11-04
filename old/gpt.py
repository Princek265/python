import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Training data (House sizes in square feet and their prices in $1000s)
house_sizes = np.array([500, 700, 900, 1100, 1300, 1500]).reshape(-1, 1)
house_prices = np.array([150, 200, 250, 300, 350, 400])  # Prices in $1000s

# Create the model and train it
model = LinearRegression()
model.fit(house_sizes, house_prices)

# Predict the price of a new house (e.g., 1200 sq ft)
new_house_size = np.array([[1200]])
predicted_price = model.predict(new_house_size)

print(f"Predicted price for a 1200 sq ft house: ${predicted_price[0]}K")

# Visualizing the data
plt.scatter(house_sizes, house_prices, color='blue', label='Actual Prices')
plt.plot(house_sizes, model.predict(house_sizes), color='red', label='Prediction Line')
plt.scatter(new_house_size, predicted_price, color='green', marker='o', label="New House Prediction")
plt.xlabel("House Size (sq ft)")
plt.ylabel("Price ($1000s)")
plt.title("House Price Prediction using Linear Regression")
plt.legend()
plt.show()
