from model import HousePriceModel
from data_preprocessing import plot_regression
import os


def main():
    # Initialize model
    model = HousePriceModel()

    # Load data with a robust path
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'house_data.csv')
    X, y = model.load_data(file_path)

    # Train model
    model.train(X, y)

    # Predict price for a 1500 sqft house
    size_to_predict = 1500
    predicted_price = model.predict(size_to_predict)
    print(f"Predicted price for {size_to_predict} sqft house: ${predicted_price:.2f}")

    # Create outputs directory if it doesn't exist
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs')
    os.makedirs(output_dir, exist_ok=True)

    # Visualize results
    output_path = os.path.join(output_dir, 'house_price_prediction.png')
    plot_regression(X, y, model.model, output_path)


if __name__ == "__main__":
    main()