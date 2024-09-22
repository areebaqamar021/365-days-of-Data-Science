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
