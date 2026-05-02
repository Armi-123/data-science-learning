from src.model import train_model

model = train_model()

# Test prediction
example = [[3, 1450, 8]]
predicted_price = model.predict(example)

print("Predicted Price:", predicted_price)
