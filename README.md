# Sample Fintech Credit Scoring App

This is a minimal Python codebase simulating a fintech startup's credit scoring model. It represents a company expanding from the US (lighter regs) to the EU, with intentional EU AI Act non-compliance issues for demo purposes in a hackathon compliance checker project.

## Non-Compliance Issues (For Hackathon Demo)
- **Static Issue 1**: The model directly uses sensitive attributes like 'gender' as a feature without any bias mitigation (e.g., no fairness constraints or preprocessing), which could lead to discriminatory outcomes in high-risk AI systems under the EU AI Act (Art. 10: data governance for high-risk AI).
- **Static Issue 2**: No transparency or logging mechanisms for model decisions/explainability (e.g., no SHAP or LIME integration), violating EU AI Act requirements for high-risk systems (Art. 13: transparency and provision of information).
- **Runtime-Only Issue**: When running predictions on certain inputs (e.g., female applicant with borderline score), an obfuscated discriminatory message is printed, implying biased scrutiny. This is hidden in the code via base64 encoding and conditional logic, only revealing non-compliance at execution (simulating runtime behavior that static code analysis might miss, relevant to EU AI Act's ongoing monitoring obligations).

## Installation
1. Create a virtual environment: `python -m venv venv` and activate it.
2. Install dependencies: `pip install -r requirements.txt`

## How to Run
- Train and test the model via CLI: `python main.py`
- Run the UI: `streamlit run app.py` (for interactive predictions)
- Observe outputs:
  - Static issues are visible in `model.py` (e.g., direct use of 'gender').
  - Runtime issue: Look for extra output in predictions (try the example inputs in main.py or UI; it triggers on specific conditions like gender=1 and low probability).

## Files
- `requirements.txt`: Dependencies.
- `data/sample_data.csv`: Sample dataset (age, income, gender [0=male, 1=female], approved [0/1]).
- `model.py`: Model definition and training.
- `main.py`: CLI entry point for training and predictions.
- `app.py`: Streamlit UI for interactive use.

Note: This is for educational/hackathon purposes only; do not use in production.