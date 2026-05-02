from src.utils import load_data
from src.model import build_cnn

def train_model():
    x_train, y_train, x_test, y_test = load_data()
    model = build_cnn()

    history = model.fit(
        x_train, y_train,
        epochs=10,
        batch_size=32,
        validation_split=0.2
    )

    model.save("cnn_model.h5")

    test_loss, test_acc = model.evaluate(x_test, y_test)
    print("Test Accuracy:", test_acc)
