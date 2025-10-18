from model import CreditModel  # Fixed import (was model.py, but Python imports without .py)

if __name__ == "__main__":
    model = CreditModel()
    model.train('data/sample_data.csv')
    
    # Example predictions
    print("\nPrediction 1 (Male, high income):")
    print(model.predict({'age': 35, 'income': 50000, 'gender': 0}))
    
    print("\nPrediction 2 (Female, borderline income - triggers runtime issue):")
    print(model.predict({'age': 30, 'income': 35000, 'gender': 1}))
    
    print("\nPrediction 3 (Male, low income):")
    print(model.predict({'age': 25, 'income': 30000, 'gender': 0}))