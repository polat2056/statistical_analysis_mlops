from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(df):
    X = df.drop('target', axis=1)
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    joblib.dump(model, 'models/random_forest_model.pkl')
    return model
import mlflow
import mlflow.sklearn

def train_model(df):
    mlflow.start_run()

    X = df.drop('target', axis=1)
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    mlflow.sklearn.log_model(model, "random_forest_model")
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", model.score(X_test, y_test))

    mlflow.end_run()
    joblib.dump(model, 'models/random_forest_model.pkl')
    return model
