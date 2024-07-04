# Wine Quality Prediction

This project aims to predict the quality of wine based on its chemical properties using various machine learning models. The dataset used is the Wine Quality dataset, which contains features such as acidity, chlorides, sulfur dioxide levels, etc., along with a quality rating.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Preprocessing](#preprocessing)
- [Modeling](#modeling)
- [Evaluation](#evaluation)
- [Results](#results)
- [Conclusion](#conclusion)
- [Installation](#installation)

## Introduction

Wine quality is determined by various factors that can be measured chemically. This project aims to leverage machine learning techniques to predict the quality of wine based on these measurable factors.
The project includes data preprocessing, model training, and evaluation.

## Dataset

The dataset used in this project is the Wine Quality dataset. It contains the following columns:

- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Free Sulfur Dioxide
- Total Sulfur Dioxide
- Density
- pH
- Sulphates
- Alcohol
- Quality (target variable)

## Preprocessing

1. **Handling Missing Values**: The dataset is checked for missing values and handled appropriately.
2. **Handling Duplicate Values**: The dataset is checked for duplicate values and handled appropriately.
3. **Standardization**: Features are standardized using `StandardScaler`.
4. **Class Imbalance**: Synthetic Minority Over-sampling Technique (SMOTE) is used to handle class imbalance.

## Modeling

The following models were used for prediction:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Classifier
- K-Nearest Neighbors
- Extra Tree Classifier
- XGB Classifier
- Artificial Neural Network (ANN)

## Evaluation

The models are evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1 Score

## Results

The performance of the models is stored in a pandas DataFrame and printed as follows:

| Classifier                | Accuracy | Precision | Recall | F1 Score |
|---------------------------|----------|-----------|--------|----------|
| Logistic Regression       | 0.532362 | 0.542011  | 0.532362 | 0.521114 |
| Decision Tree             | 0.522654 | 0.521329  | 0.522654 | 0.521787 |
| Random Forest             | 0.600324 | 0.612666  | 0.600324 | 0.590215 |
| Support Vector Classifier | 0.579288 | 0.596981  | 0.579288 | 0.560440 |
| K-Nearest Neighbors       | 0.556634 | 0.558658  | 0.556634 | 0.556183 |
| Extra Tree Classifier     | 0.610032 | 0.621627  | 0.610032 | 0.600254 |
| XGB classifier            | 0.601942 | 0.605508  | 0.601942 | 0.597072 |
| Artificial Neural Network | 0.730831 | 0.715200  | 0.730831 | 0.718137 |





## Dependencies

- pandas
- numpy
- scikit-learn 1.3.2
- xgboost 1.6.2
- streamlit
- pickle
- tensorflow 2.15.0
## Installation

Install all project requirements 

```bash
  pip install -r requirements.txt
```
    
Run the command to see the demo

```bash
  streamlit run app.py
```
## Authors

- [@Debopam-Pritam2014](https://www.github.com/Debopam-Pritam2014)


## Acknowledgements

 - [Dataset link kaggle](https://www.kaggle.com/datasets/debopamdey/combined-wine-dataset-red-and-white-wines)
 - [imblearn Docs](https://imbalanced-learn.org/stable/user_guide.html)


## Conclusion

The project demonstrates the use of various machine learning algorithms to predict wine quality. The Artificial Neural Network model showed promising results with further potential improvements through hyperparameter tuning and more sophisticated feature engineering.

## Feedback

If you have any feedback, please reach out to me at debopamdeycse19@gmail.com

