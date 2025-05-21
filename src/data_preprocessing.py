import matplotlib.pyplot as plt

def plot_regression(X, y, model, output_path):
    """Plot the data points and regression line."""
    plt.scatter(X, y, color='blue', label='Data')
    plt.plot(X, model.predict(X), color='red', label='Regression Line')
    plt.xlabel('House Size (sqft)')
    plt.ylabel('Price ($)')
    plt.title('House Price Prediction')
    plt.legend()
    plt.savefig(output_path)
    plt.close()
    print(f"Plot saved to {output_path}")