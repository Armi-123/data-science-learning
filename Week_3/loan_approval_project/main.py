from src.model import train_models

model = train_models()

# Test prediction
sample = [[50000, 710, 25000, 0]]
prediction = model.predict(sample)

print("Loan Approved?" , "YES" if prediction[0] == 1 else "NO")