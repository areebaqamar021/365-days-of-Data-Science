# Dynamic Pricing Optimization for E-commerce

## Project Overview

This project focuses on building a **dynamic pricing model** for an e-commerce platform that adjusts product prices in real-time based on factors such as demand, competitor pricing, customer behavior, seasonality, and inventory levels. The goal is to optimize prices to maximize sales and profit using **machine learning models**.

### Key Features:
- **Real-time pricing adjustments** based on market conditions
- **Predictive models** to determine optimal prices
- **Simulation of e-commerce data** for training the models
- **Machine Learning Models**: Linear Regression, Random Forest, Neural Networks
- **Profit Maximization Strategy**
- **API Deployment** for real-time pricing using Flask

---

## Table of Contents
1. [Project Setup and Dependencies](#project-setup-and-dependencies)
2. [Dataset](#dataset)
3. [Exploratory Data Analysis](#exploratory-data-analysis)
4. [Feature Engineering](#feature-engineering)
5. [Modeling](#modeling)
    - Linear Regression
    - Random Forest
    - Neural Network
6. [Optimization Strategies](#optimization-strategies)
7. [Model Evaluation](#model-evaluation)
8. [API Deployment](#api-deployment)
9. [How to Use](#how-to-use)
10. [Contributing](#contributing)

---

## Project Setup and Dependencies

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Jupyter Notebook

### Installing Required Libraries

To install the required libraries, run:

```bash
pip install pandas numpy scikit-learn xgboost tensorflow keras matplotlib seaborn flask
```
## Dataset

We have simulated an e-commerce dataset containing product prices, competitor prices, customer interest, sales volume, and more. This dataset is used to train and test our machine learning models.

### Sample Data

| Product_ID | Price | Competitor_Price | Sales_Volume | Customer_Interest | Seasonality | Inventory_Level |
|------------|-------|------------------|--------------|-------------------|-------------|-----------------|
| 1          | 32.45 | 30.10            | 245          | 654               | High        | 150             |
| 2          | 55.78 | 54.30            | 134          | 540               | Medium      | 210             |

## Exploratory Data Analysis

We performed Exploratory Data Analysis (EDA) to visualize relationships between the product price, competitor price, and sales volume. Key insights were obtained from:

- Scatter plots between Price and Sales Volume
- Line plots for Competitor Price vs Sales Volume
- Histogram showing the distribution of sales volumes

## Feature Engineering

We enhanced our dataset with additional features to improve model accuracy:

- **Lag Features**: Historical sales volume (`Sales_Lag1`)
- **Rolling Averages**: Smoothed sales data (`Sales_Rolling_3`)
- **Dummy Variables**: Convert Seasonality to numeric form

## Modeling

Three different models were implemented to predict sales volume based on various features:

### 1. Linear Regression
A basic linear regression model was used as the baseline model.

```python
from sklearn.linear_model import LinearRegression
```
### 2. Random Forest Regressor
A more advanced tree-based model, Random Forest, was used for better prediction accuracy.

```python
from sklearn.ensemble import RandomForestRegressor
```
### 3. Neural Network
We implemented a **Neural Network** using **Keras** with TensorFlow backend to capture complex relationships in the data.

```python
from keras.models import Sequential
from keras.layers import Dense
```

## Optimization Strategies

We employed Profit Maximization as an optimization strategy. The profit is calculated as:
```python
Profit = (Price - Cost) * Sales_Volume
```
## Model Evaluation

The performance of the models is evaluated using Mean Squared Error (MSE) and R² Score:

| Model             | MSE    | R² Score |
|-------------------|--------|----------|
| Linear Regression | 345.12 | 0.78     |
| Random Forest     | 256.34 | 0.85     |
| Neural Network    | 214.45 | 0.89     |

Visualizations such as **Actual vs Predicted Sales Volume** for each model were generated to compare their performances.

## API Deployment

We deployed the optimal pricing model using **Flask**. This API predicts the optimal price for a product in real-time based on the features provided.

### Example Flask API Code

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict_price', methods=['POST'])
def predict_price():
    data = request.get_json()
    features = [data['features']]
    price_pred = rf_model.predict(features)
    return jsonify({'optimal_price': price_pred[0]})

if __name__ == '__main__':
    app.run(debug=True)
```

This **Flask API** can be used to integrate real-time pricing into an e-commerce platform, allowing for dynamic price adjustments based on machine learning models.

## How to Use

### 1. Clone the repository:

```bash
git clone https://github.com/areebaqamar021/dynamic-pricing-optimization.git
cd dynamic-pricing-optimization
```
### 2.Run Jupyter Notebook:
Open the notebook in Jupyter and run each cell step by step.

### 3. Start Flask API:
To deploy the model as an API, run:

```bash
python app.py
```
### Make a POST Request: 
You can use Postman or curl to test the API. Example:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"features": [50, 48, 400, 300, 20, 50, 1, 0]}' \
http://localhost:5000/predict_price
```
## Contributing
Contributions are welcome! If you'd like to collaborate or suggest improvements:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add some feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

