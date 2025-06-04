import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def generate_dice_data(n):
    rolls = np.random.randint(1, 7, size=n)
    X, y = [], []
    for i in range(6, len(rolls)):
        X.append(rolls[i-6:i])
        y.append(rolls[i])
    return np.array(X), np.array(y)

def train_model():
    X, y = generate_dice_data(10000)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    return model, accuracy