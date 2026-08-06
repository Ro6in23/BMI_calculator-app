
import google.genai as genai
import streamlit as st

GOOGLE_API_KEY = st.secrets["google"]["api_key"]

client = genai.Client(api_key= GOOGLE_API_KEY)

st.title("BMI Calculator with AI Nutritionist")

#Input fields for height and weight

wt = st.number_input("Enter your weight in kilograms: ", min_value=0.0, value=70.0)
ht = st.number_input("Enter your height in meters: ", min_value=0.1, value=1.0)

# Calculate BMI
bmi = wt / (ht**2)
st.write(f"Your bmi is: {bmi:.2f}")

prompt = f"Act like an expert nutritionist, comment on BMI with following data: height as {ht}, weight as {wt}, BMI as {bmi}"

if st.button("Analyze your BMI using AI:"):
    st.write("Analyzing your BMI with AI..........")
    response = client.models.generate_content(
        model = "gemini-3.5-flash-lite",
        contents = prompt
    )
    st.write(response.text)
