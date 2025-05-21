# House Price Prediction ML Project

## Overview

This project demonstrates a simple linear regression model to predict house prices based on house size (square footage). It serves as a foundational example for setting up a structured machine learning project, adhering to best practices for reproducibility and organization.

## Project Structure
house_price_prediction_ml/
├── src/
│   └── main.py             # Main script to run the prediction
│   └── model.py            # (Optional) For more complex models/functions
│   └── data_preprocessing.py # (Optional) For data cleaning/transformation
├── data/
│   ├── raw/                # Original, immutable datasets
│   └── processed/          # Cleaned and preprocessed data
├── models/
│   └── linear_regression_model.pkl # Trained model saved here
├── notebooks/
│   └── eda.ipynb           # Jupyter notebooks for exploration/experimentation
├── reports/
│   └── figures/            # Generated plots and visualizations
├── venv/                   # Python virtual environment
├── .gitignore              # Files/folders to ignore in version control
├── requirements.txt        # List of project dependencies
└── README.md               # Project description, setup, and usage instructions

## Setup Instructions

To set up and run this project on your local machine, follow these steps:

1.  **Clone the Repository (if applicable):**
    ```bash
    # If this were a Git repository
    # git clone <repository-url>
    # cd house_price_prediction_ml
    ```
    * *For this example, simply create the `house_price_prediction_ml` directory manually.*

2.  **Create a Virtual Environment:**
    It's highly recommended to use a virtual environment to manage project dependencies.
    * **Using PyCharm:** When creating a new project in PyCharm, select "New environment using Virtualenv" and PyCharm will handle this automatically.
    * **Manual (Terminal):**
        ```bash
        python -m venv venv
        # On Windows:
        .\venv\Scripts\activate
        # On macOS/Linux:
        # source venv/bin/activate
        ```

3.  **Install Dependencies:**
    With your virtual environment activated, install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create Project Directories:**
    Ensure the following directories exist within your `house_price_prediction_ml` root:
    * `src/`
    * `data/`
    * `data/raw/`
    * `data/processed/`
    * `models/`
    * `notebooks/`
    * `reports/`
    * `reports/figures/`

5.  **Place `main.py`:**
    Copy the provided `main.py` script into the `src/` directory.

## How to Run

1.  **Activate your virtual environment** (if you're not using PyCharm's integrated terminal, which usually activates it automatically).
2.  **Navigate to the project root directory** in your terminal.
3.  **Execute the main script:**
    ```bash
    python src/main.py
    ```

## Output

Upon successful execution, the script will:
* Print the predicted price for a 1500 sqft house to the console.
* Generate a plot named `house_price_prediction.png` in the `reports/figures/` directory, visualizing the data points and the linear regression line.

## Future Enhancements (Roadmap)

* **Integrate a larger, real-world dataset:** Replace sample data with a CSV file.
* **Data Preprocessing:** Implement functions for handling missing values, feature scaling, and categorical encoding in `src/data_preprocessing.py`.
* **Model Evaluation:** Add metrics like R-squared, MAE, and MSE to assess model performance.
* **Train/Test Split:** Divide the dataset into training and testing sets to evaluate generalization.
* **Feature Engineering:** Explore and add more relevant features (e.g., number of bedrooms, location).
* **Model Persistence:** Save and load the trained model using `joblib` for future use.
* **Advanced Models:** Experiment with other regression algorithms (e.g., Ridge, Lasso, Random Forest).