# Importing required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import streamlit as st

# Load country-specific housing data
train_data = pd.read_csv('train_country.csv')
test_data = pd.read_csv('test_country.csv')

# Data cleaning
# Drop columns with high missing values
missing_vals = train_data.isnull().sum()
high_missing_cols = missing_vals[missing_vals > train_data.shape[0] * 0.4].index
train_data.drop(columns=high_missing_cols, inplace=True)
test_data.drop(columns=high_missing_cols, inplace=True)

# Fill missing values for numerical columns with median
for col in train_data.select_dtypes(include=['float64', 'int64']).columns:
    fill_value = train_data[col].median()
    train_data[col].fillna(fill_value, inplace=True)
    test_data[col].fillna(fill_value, inplace=True)

# Fill missing values for categorical columns with mode
for col in train_data.select_dtypes(include=['object']).columns:
    fill_value = train_data[col].mode()[0]
    train_data[col].fillna(fill_value, inplace=True)
    test_data[col].fillna(fill_value, inplace=True)

# Exploratory Data Analysis (EDA)
# SalePrice distribution
plt.figure(figsize=(6, 4))
sns.histplot(train_data['SalePrice'], kde=True)
plt.title('Distribution of Sale Prices')
plt.show()

# Correlation heatmap
correlation = train_data.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation, annot=False, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Sale Price vs Overall Quality
sns.boxplot(x='OverallQual', y='SalePrice', data=train_data)
plt.title('Sale Price vs Overall Quality')
plt.show()

# Feature Engineering
train_data['TotalSF'] = train_data['TotalBsmtSF'] + train_data['1stFlrSF']
test_data['TotalSF'] = test_data['TotalBsmtSF'] + test_data['1stFlrSF']

# Selecting significant features
features = ['OverallQual', 'GrLivArea', 'TotalSF', 'GarageCars', 'FullBath', 'YearBuilt']
X_train = train_data[features]
y_train = train_data['SalePrice']
X_test = test_data[features]

# Modeling using Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_train)
rmse = mean_squared_error(y_train, y_pred, squared=False)
print(f'Training RMSE: {rmse}')

# Streamlit Dashboard
def load_streamlit_interface():
    st.title('House Price Prediction')
    overall_qual = st.slider('Overall Quality', 1, 10, 5)
    gr_liv_area = st.number_input('Ground Living Area (sq ft)', value=1500)
    total_sf = st.number_input('Total Square Feet (sq ft)', value=2000)
    garage_cars = st.slider('Size of Garage (Car Capacity)', 0, 5, 2)
    full_bath = st.slider('Number of Full Bathrooms', 0, 4, 2)
    year_built = st.slider('Year Built', 1850, 2020, 1990)

    if st.button('Predict Price'):
        input_data = pd.DataFrame([[overall_qual, gr_liv_area, total_sf, garage_cars, full_bath, year_built]],
                                  columns=features)
        prediction = model.predict(input_data)
        st.success(f'Predicted Sale Price: ${prediction[0]:,.2f}')

    # Display additional insights or visualizations based on user inputs

if __name__ == '__main__':
    load_streamlit_interface()
