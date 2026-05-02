from sklearn.metrics import mean_absolute_error

def evaluate(true, pred):
    return mean_absolute_error(true, pred)
