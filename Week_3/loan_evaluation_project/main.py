from src.model import evaluate_model

model = evaluate_model()

# Example new applicant
sample = [[60000, 710, 25000, 0]]
prediction = model.predict(sample)

print("\nLoan Approved?" , "YES" if prediction[0] == 1 else "NO")
