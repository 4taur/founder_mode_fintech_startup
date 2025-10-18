import streamlit as st
from model import CreditModel  # Import the model class

st.title("Fintech Credit Scoring Demo App")
st.markdown("""
This UI simulates a fintech credit scoring tool. Enter applicant details to get a prediction.
(Note: For hackathon demo, this reveals runtime non-compliance when triggered.)
""")

# Train model on load (or load pre-trained if desired)
@st.cache_resource
def load_model():
    model = CreditModel()
    model.train('data/sample_data.csv')
    return model

model = load_model()

# Input form
age = st.number_input("Age", min_value=18, max_value=100, value=30)
income = st.number_input("Annual Income ($)", min_value=0, value=40000)
gender = st.selectbox("Gender (0: Male, 1: Female)", [0, 1])

if st.button("Predict Credit Approval"):
    input_data = {'age': age, 'income': income, 'gender': gender}
    result = model.predict(input_data)
    st.subheader("Prediction")
    st.write(result)
    
    # Note: Runtime issue prints to console if triggered; check terminal for biased message.