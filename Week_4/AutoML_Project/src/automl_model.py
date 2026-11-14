from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def run_automl(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y  # <- fix
    )
    
    models = {
        'RandomForest': RandomForestClassifier(random_state=42),
        'SVM': SVC(random_state=42)
    }
    
    best_model = None
    best_score = 0
    
    for name, model in models.items():
        print(f"Training {name}...")
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        print(f"{name} Accuracy: {score:.4f}")
        if score > best_score:
            best_score = score
            best_model = model
    
    print("Best Model Selected:", best_model)
    print(f"Best Accuracy: {best_score:.4f}")
    
    return best_model