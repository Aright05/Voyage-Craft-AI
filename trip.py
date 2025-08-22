import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load Gemini API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit Page Config
st.set_page_config(page_title="VoyageCraft AI", page_icon="🌍", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    body {
        background-color: #f0f8ff;
        font-family: 'Segoe UI', sans-serif;
    }
    .main-title {
        font-size: 3rem;
        text-align: center;
        color: #2b6777;
        padding-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        color:  #000000 ;
        font-size: 1.2rem;
        margin-bottom: 30px;
    }
    .stButton>button {
        background-color: #fff685;
        color: white;
        font-size: 18px;
        border-radius: 12px;
        padding: 10px 24px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff1d58;
        transform: scale(1.05);
    }
    .block-container {
        max-width: 900px;
        margin: auto;
        padding-top: 20px;
        background-color:  #d0bdf4;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
    }
    textarea, input[type=text], input[type=number] {
        border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Page title and subtitle
st.markdown("<h1 class='main-title'>🌍 VoyageCraft AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Plan your perfect trip with AI – quick, smart & personalized!</p>", unsafe_allow_html=True)

# Input Fields
destination = st.text_input("✈️ Destination")
col1, col2 = st.columns(2)
with col1:
    budget = st.number_input("💰 Budget (in ₹)", min_value=1000, step=500)
with col2:
    days = st.number_input("📅 Number of Days", min_value=1, step=1)
preferences = st.text_area("🎯 Preferences (e.g., food, beaches, culture)")

# Button and AI logic
if st.button("Generate Itinerary"):
    if not destination.strip():
        st.warning("Please enter a destination.")
    else:
        with st.spinner("Planning your trip..."):
            prompt = f"""
            You are a smart travel planner AI. Plan a {days}-day trip to {destination} within ₹{budget}.
            User preferences: {preferences}.
            Include day-wise itinerary, attractions, local food, budget hotels, and experiences.
            Be concise but informative.
            """
            try:
                response = model.generate_content(prompt)
                st.success("Here’s your trip plan!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error generating itinerary: {e}")
