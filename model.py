import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class CreditModel:
    def __init__(self):
        self.model = LogisticRegression()
    
    def train(self, data_path):
        # Load data
        df = pd.read_csv(data_path)
        
        # Features include sensitive attribute 'gender' without mitigation (Static Non-Compliance: Potential bias/discrimination)
        X = df[['age', 'income', 'gender']]
        y = df['approved']
        
        # Split and train (No transparency logging here - Static Non-Compliance: Missing explainability)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        
        # Evaluate
        preds = self.model.predict(X_test)
        print(f"Model Accuracy: {accuracy_score(y_test, preds):.2f}")
    
    def predict(self, input_data):
        # Input_data: dict with 'age', 'income', 'gender'
        df_input = pd.DataFrame([input_data])
        prob = self.model.predict_proba(df_input)[0][1]  # Probability of approval
        
        # Obfuscated runtime check (Non-Compliance only visible at runtime: Discriminatory logic)
        import base64
        check_val = int(base64.b64decode(b'MQ==').decode())  # Obfuscated '1' for gender
        if input_data['gender'] == check_val and prob < 0.5:
            extra_msg = base64.b64decode(b'SG93ZXZlciwgY2VydGFpbiBkZW1vZ3JhcGhpY3MgbWF5IGZhY2UgaGlnaGVyIHNjcnV0aW55IGZvciByaXNrIGFzc2Vzc21lbnQu').decode()
            print(extra_msg)  # Biased message implying extra scrutiny for females
        
        return "Approved" if prob > 0.5 else "Denied"