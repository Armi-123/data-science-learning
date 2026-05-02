import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def build_and_train_model():
    # Load dataset
    df = pd.read_csv(r"d:\Unlox\Week_5\NeuralNetwork_Project\diabetes.csv")

    # Split features and labels
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Feature scaling (important for NN)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Build ANN
    model = Sequential([
        Dense(16, activation='relu', input_dim=X_train.shape[1]),
        Dense(8, activation='relu'),
        Dense(1, activation='sigmoid')     # binary output
    ])

    # Compile ANN
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Train ANN
    model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2)

    # Evaluate
    loss, accuracy = model.evaluate(X_test, y_test)
    print("Model Accuracy:", accuracy)
