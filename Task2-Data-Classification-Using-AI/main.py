
"""
DecodeLabs AI Internship - Project 2

Features:
1. Load and explore a dataset
2. Split data into training and testing sets
3. Train a Decision Tree classifier
4. Evaluate model accuracy
5. Display a confusion matrix
6. Predict classes for new input data
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)


def load_dataset():
    """Load and display basic dataset information."""
    print("\n" + "=" * 55)
    print(" DECODELABS - AI DATA CLASSIFICATION")
    print("=" * 55)

    iris = load_iris()

    X = iris.data
    y = iris.target

    print("\n[1] DATASET INFORMATION")
    print("-" * 55)
    print(f"Dataset name: Iris")
    print(f"Total samples: {X.shape[0]}")
    print(f"Number of features: {X.shape[1]}")
    print(f"Number of classes: {len(iris.target_names)}")
    print(f"Features: {', '.join(iris.feature_names)}")
    print(f"Classes: {', '.join(iris.target_names)}")

    print("\nFirst five samples:")
    print(X[:5])

    return iris, X, y


def split_dataset(X, y):
    """Split the dataset into training and testing sets."""
    print("\n[2] SPLITTING THE DATASET")
    print("-" * 55)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")

    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    """Train the Decision Tree classifier."""
    print("\n[3] TRAINING THE MODEL")
    print("-" * 55)

    model = DecisionTreeClassifier(
        random_state=42,
        max_depth=4,
    )

    model.fit(X_train, y_train)

    print("Algorithm: Decision Tree Classifier")
    print("Training completed successfully.")

    return model


def evaluate_model(model, X_test, y_test, iris):
    """Evaluate predictions using unseen test data."""
    print("\n[4] MODEL EVALUATION")
    print("-" * 55)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f"Model accuracy: {accuracy:.2%}")

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions,
            labels=np.arange(len(iris.target_names)),
            target_names=iris.target_names,
            zero_division=0,
        )
    )

    matrix = confusion_matrix(
        y_test,
        predictions,
        labels=np.arange(len(iris.target_names)),
    )

    print("Confusion Matrix:")
    print(matrix)

    return accuracy, matrix


def show_confusion_matrix(matrix, iris):
    """Display a graphical confusion matrix."""
    plt.figure(figsize=(7, 5))

    plt.imshow(matrix, interpolation="nearest")
    plt.title("DecodeLabs - Confusion Matrix")
    plt.colorbar()

    positions = np.arange(len(iris.target_names))

    plt.xticks(positions, iris.target_names, rotation=25)
    plt.yticks(positions, iris.target_names)

    plt.xlabel("Predicted Class")
    plt.ylabel("Actual Class")

    threshold = matrix.max() / 2 if matrix.size else 0

    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            color = (
                "white"
                if matrix[row, col] > threshold
                else "black"
            )

            plt.text(
                col,
                row,
                str(matrix[row, col]),
                ha="center",
                va="center",
                color=color,
            )

    plt.tight_layout()
    plt.show()


def predict_new_sample(model, iris):
    """Take user measurements and predict a flower species."""
    print("\n[5] PREDICT A NEW FLOWER")
    print("-" * 55)

    print("Enter measurements in centimeters.")

    measurements = []

    prompts = [
        "Sepal length",
        "Sepal width",
        "Petal length",
        "Petal width",
    ]

    for prompt in prompts:
        while True:
            try:
                value = float(input(f"{prompt}: "))

                if not np.isfinite(value) or value <= 0:
                    print("Enter a finite number greater than zero.")
                    continue

                measurements.append(value)
                break

            except ValueError:
                print("Invalid input. Please enter a number.")

    sample = np.array(measurements).reshape(1, -1)

    prediction = model.predict(sample)[0]
    species = iris.target_names[prediction]

    print("\nPrediction Result")
    print("-" * 55)
    print(f"Predicted species: {species}")

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(sample)[0]

        print("\nModel probability estimates:")
        for name, probability in zip(
            iris.target_names, probabilities
        ):
            print(f"{name}: {probability:.2%}")

        print(
            "\nNote: These are model estimates, "
            "not guaranteed probabilities of correctness."
        )


def main():
    iris, X, y = load_dataset()

    X_train, X_test, y_train, y_test = split_dataset(X, y)

    model = train_model(X_train, y_train)

    accuracy, matrix = evaluate_model(
        model, X_test, y_test, iris
    )

    show_confusion_matrix(matrix, iris)

    while True:
        answer = input(
            "\nWould you like to predict a new flower? (y/n): "
        ).strip().lower()

        if answer == "y":
            predict_new_sample(model, iris)

        elif answer == "n":
            print("\nThank you for using DecodeLabs AI Project 2!")
            break

        else:
            print("Please enter 'y' or 'n'.")

    print(f"\nFinal test accuracy: {accuracy:.2%}")


if __name__ == "__main__":
    main()
