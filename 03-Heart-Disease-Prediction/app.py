import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(
    page_title="Heart Disease Risk Assessment",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Dark Theme & High Contrast Labels
st.markdown("""
    <style>
    /* Global App Background */
    .stApp {
        background-color: #0b132b;
        color: #ffffff;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #1c2541;
        border-right: 1px solid #3a506b;
    }
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    /* Titles & Subheadings */
    h1, h2, h3 {
        color: #6fffe9 !important;
        font-weight: 700 !important;
    }
    
    /* Input Field Labels (Age, BP, Height, etc.) */
    label, p, div[data-testid="stMarkdownContainer"] > p {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 15px !important;
    }

    /* Form Container Card */
    div[data-testid="stForm"] {
        background-color: #1c2541;
        border: 1px solid #3a506b;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.4);
    }

    /* Text Inputs, Selectboxes, and Number Controls */
    input, div[data-baseweb="select"] > div {
        background-color: #0b132b !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        border: 1px solid #486581 !important;
    }

    /* Dropdown Options List */
    div[role="listbox"] ul li {
        color: #ffffff !important;
        background-color: #1c2541 !important;
    }

    /* High Contrast Submit Button */
    .stButton > button {
        width: 100%;
        background-color: #e63946 !important;
        color: #ffffff !important;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 700 !important;
        font-size: 16px !important;
        border: none !important;
        box-shadow: 0px 4px 10px rgba(230, 57, 70, 0.3);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #d62828 !important;
        color: #ffffff !important;
    }

    /* Information Box in Sidebar */
    .stAlert {
        background-color: #0b132b !important;
        border: 1px solid #3a506b !important;
        color: #6fffe9 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Load Saved Model Pipeline
@st.cache_resource
def load_model():
    try:
        return joblib.load('Heart_Disease_Model.pkl')
    except Exception:
        return None

model = load_model()

# Sidebar Configuration
with st.sidebar:
    st.image("https://img.icons8.com/color/96/heart-health.png", width=70)
    st.title("CardioPredict")
    st.write("Heart Disease Risk Predictor")
    st.divider()
    st.info("ℹ️ Enter patient clinical details in the form to evaluate heart disease risk.")

# Header
st.title("❤️ Heart Disease Assessment Portal")
st.caption("Enter patient details below to perform an automated risk assessment.")
st.divider()

if model is None:
    st.warning("⚠️ Model file `Heart_Disease_Model.pkl` was not found. Please save your trained pipeline first.")

# Main Input Form
with st.form("patient_form"):
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.subheader("🩺 Clinical Vitals")
        
        age = st.number_input("Age (Years)", min_value=1, max_value=120, value=45)
        
        v_col1, v_col2 = st.columns(2)
        with v_col1:
            ap_hi = st.number_input("Systolic BP (ap_hi)", min_value=50, max_value=250, value=120)
        with v_col2:
            ap_lo = st.number_input("Diastolic BP (ap_lo)", min_value=30, max_value=150, value=80)
            
        cholesterol = st.selectbox("Cholesterol Level", options=[1, 2, 3], 
                                  format_func=lambda x: {1: "1: Normal", 2: "2: Above Normal", 3: "3: High"}[x])
        
        gluc = st.selectbox("Glucose Level", options=[1, 2, 3], 
                           format_func=lambda x: {1: "1: Normal", 2: "2: Above Normal", 3: "3: High"}[x])

    with col2:
        st.subheader("👤 Biometrics & Demographics")
        
        b_col1, b_col2 = st.columns(2)
        with b_col1:
            height = st.number_input("Height (cm)", min_value=50, max_value=250, value=165)
        with b_col2:
            weight = st.number_input("Weight (kg)", min_value=20, max_value=200, value=70)
            
        country = st.selectbox("Country", ["India", "Indonesia", "Singapore", "USA", "Other"])
        occupation = st.selectbox("Occupation", ["Accountant", "Engineer", "Doctor", "Nurse", "Teacher", "Chef", "Lawyer", "Other"])

    st.write("")
    submit = st.form_submit_button("Run Risk Assessment")

# Output Section
if submit and model is not None:
    st.divider()
    st.subheader("📊 Assessment Result")
    
    input_data = pd.DataFrame([{
        'age': age,
        'ap_hi': ap_hi,
        'ap_lo': ap_lo,
        'cholesterol': cholesterol,
        'gluc': gluc,
        'height': height,
        'weight': weight,
        'country': country,
        'occupation': occupation
    }])

    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0][1] if hasattr(model, "predict_proba") else (0.85 if prediction == 1 else 0.15)

    res_col1, res_col2 = st.columns([1, 1], gap="medium")

    with res_col1:
        # Gauge Chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=prediction_proba * 100,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Cardiovascular Risk Level", 'font': {'color': "#6fffe9", 'size': 18}},
            number={'suffix': "%", 'font': {'color': "#ffffff"}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#ffffff"},
                'bar': {'color': "#e63946" if prediction == 1 else "#2a9d8f"},
                'bgcolor': "#0b132b",
                'borderwidth': 2,
                'bordercolor': "#3a506b",
                'steps': [
                    {'range': [0, 40], 'color': 'rgba(42, 157, 143, 0.3)'},
                    {'range': [40, 70], 'color': 'rgba(233, 196, 106, 0.3)'},
                    {'range': [70, 100], 'color': 'rgba(230, 57, 70, 0.3)'}
                ],
            }
        ))
        fig.update_layout(paper_bgcolor="#1c2541", font={'color': "#ffffff"}, height=260, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig, use_container_width=True)

    with res_col2:
        st.write("")
        if prediction == 1:
            st.error("🚨 **High Risk Detected**")
            st.markdown("""
            * Further cardiovascular screening (ECG / Lipid panel) is recommended.
            * Monitor daily blood pressure levels (`ap_hi` / `ap_lo`).
            * Consult a healthcare professional for clinical advice.
            """)
        else:
            st.success("✅ **Low Risk Detected**")
            st.markdown("""
            * Patient clinical metrics fall within typical target baseline ranges.
            * Continue routine health monitoring and balanced lifestyle practices.
            """)