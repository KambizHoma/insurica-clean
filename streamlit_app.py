import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="Insurica - Life Insurance Underwriting",
    page_icon="nippotica_icon.png",
    layout="wide"
)

# Title and description with modern styling
st.title("Insurica")
st.markdown("### AI-Powered Life Insurance Underwriting")
st.caption("Instant risk assessment and underwriting decisions powered by machine learning")
st.markdown("")  # Add spacing

# Sidebar for demo controls
with st.sidebar:
    # Company logo at the top
    try:
        st.image("nippotica_icon.png", width=100)
    except:
        st.markdown("### NIPPOTICA")
    
    st.markdown("")
    st.markdown("#### Demo Controls")
    demo_mode = st.selectbox(
        "Select Demo Scenario",
        ["Custom Input", "Scenario 1: Low Risk", "Scenario 2: Standard Risk", "Scenario 3: High Risk"]
    )
    
    st.markdown("")
    with st.container():
        st.markdown("##### About Insurica")
        st.caption("Advanced ML for instant underwriting decisions with 94%+ accuracy")
        st.caption("Processing time: < 200ms")
        st.caption("Powered by Nippofin Business Unit")

# Predefined scenarios
scenarios = {
    "Scenario 1: Low Risk": {
        "age": 30,
        "gender": "Male",
        "height": 175,
        "weight": 70,
        "smoker": "No",
        "alcohol": "Occasional",
        "exercise": "Regular (3+ times/week)",
        "occupation": "Software Engineer",
        "diabetes": False,
        "heart_disease": False,
        "cancer": False,
        "hypertension": False,
        "family_heart": False,
        "family_cancer": False,
        "family_diabetes": False
    },
    "Scenario 2: Standard Risk": {
        "age": 45,
        "gender": "Female",
        "height": 162,
        "weight": 68,
        "smoker": "No",
        "alcohol": "Social",
        "exercise": "Moderate (1-2 times/week)",
        "occupation": "Teacher",
        "diabetes": False,
        "heart_disease": False,
        "cancer": False,
        "hypertension": True,
        "family_heart": True,
        "family_cancer": False,
        "family_diabetes": False
    },
    "Scenario 3: High Risk": {
        "age": 55,
        "gender": "Male",
        "height": 170,
        "weight": 95,
        "smoker": "Yes",
        "alcohol": "Regular",
        "exercise": "Rarely",
        "occupation": "Construction Worker",
        "diabetes": True,
        "heart_disease": False,
        "cancer": False,
        "hypertension": True,
        "family_heart": True,
        "family_cancer": True,
        "family_diabetes": True
    }
}

# INPUT SECTION
st.markdown("## 📋 Application Input")
st.caption("Enter applicant information below or select a demo scenario from the sidebar")
st.markdown("")

col1, col2, col3 = st.columns(3)

# Load scenario data if selected
if demo_mode != "Custom Input":
    scenario_data = scenarios[demo_mode]
else:
    scenario_data = None

with col1:
    st.markdown("#### Basic Information")
    age = st.number_input("Age", min_value=18, max_value=80, 
                          value=scenario_data["age"] if scenario_data else 35)
    gender = st.selectbox("Gender", ["Male", "Female"], 
                          index=0 if not scenario_data or scenario_data["gender"]=="Male" else 1)
    height = st.number_input("Height (cm)", min_value=140, max_value=220, 
                             value=scenario_data["height"] if scenario_data else 170)
    weight = st.number_input("Weight (kg)", min_value=40, max_value=150, 
                             value=scenario_data["weight"] if scenario_data else 70)

with col2:
    st.markdown("#### Lifestyle Factors")
    smoker = st.selectbox("Smoking Status", ["No", "Yes", "Former (quit >2 years)"],
                          index=["No", "Yes", "Former (quit >2 years)"].index(scenario_data["smoker"]) if scenario_data else 0)
    alcohol = st.selectbox("Alcohol Consumption", ["None", "Occasional", "Social", "Regular"],
                          index=["None", "Occasional", "Social", "Regular"].index(scenario_data["alcohol"]) if scenario_data else 1)
    exercise = st.selectbox("Exercise Frequency", 
                           ["Rarely", "Moderate (1-2 times/week)", "Regular (3+ times/week)", "Athlete"],
                           index=["Rarely", "Moderate (1-2 times/week)", "Regular (3+ times/week)", "Athlete"].index(scenario_data["exercise"]) if scenario_data else 2)
    occupation = st.selectbox("Occupation Risk Level", 
                             ["Office Worker", "Teacher", "Healthcare", "Software Engineer", "Sales", "Construction Worker", "Driver"],
                             index=["Office Worker", "Teacher", "Healthcare", "Software Engineer", "Sales", "Construction Worker", "Driver"].index(scenario_data["occupation"]) if scenario_data else 0)

with col3:
    st.markdown("#### Medical History")
    diabetes = st.checkbox("Diabetes", value=scenario_data["diabetes"] if scenario_data else False)
    heart_disease = st.checkbox("Heart Disease", value=scenario_data["heart_disease"] if scenario_data else False)
    cancer = st.checkbox("Cancer History", value=scenario_data["cancer"] if scenario_data else False)
    hypertension = st.checkbox("Hypertension", value=scenario_data["hypertension"] if scenario_data else False)
    
    st.markdown("#### Family History")
    family_heart = st.checkbox("Family Heart Disease", value=scenario_data["family_heart"] if scenario_data else False)
    family_cancer = st.checkbox("Family Cancer", value=scenario_data["family_cancer"] if scenario_data else False)
    family_diabetes = st.checkbox("Family Diabetes", value=scenario_data["family_diabetes"] if scenario_data else False)

st.markdown("")

# Calculate BMI
bmi = weight / ((height/100) ** 2)

# ANALYZE BUTTON - centered
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    analyze_clicked = st.button("🔍 Analyze Application with AI", type="primary", use_container_width=True)

if analyze_clicked:
    
    # Processing animation
    with st.spinner("Insurica AI is analyzing application data..."):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        steps = [
            "Loading applicant data...",
            "Calculating health metrics...",
            "Analyzing medical history...",
            "Evaluating lifestyle risk factors...",
            "Processing family history...",
            "Running ML risk model...",
            "Generating underwriting decision..."
        ]
        
        for i, step in enumerate(steps):
            status_text.text(step)
            progress_bar.progress((i + 1) / len(steps))
            time.sleep(0.3)
        
        status_text.empty()
        progress_bar.empty()
    
    # Calculate risk score (simplified ML simulation)
    risk_score = 50  # Base score
    
    # Age factor
    if age < 30:
        risk_score -= 10
    elif age > 50:
        risk_score += 15
    elif age > 40:
        risk_score += 8
    
    # BMI factor
    if bmi < 18.5:
        risk_score += 8
    elif bmi > 30:
        risk_score += 15
    elif bmi > 25:
        risk_score += 8
    
    # Smoking
    if smoker == "Yes":
        risk_score += 20
    elif smoker == "Former (quit >2 years)":
        risk_score += 5
    
    # Medical conditions
    if diabetes:
        risk_score += 12
    if heart_disease:
        risk_score += 18
    if cancer:
        risk_score += 15
    if hypertension:
        risk_score += 10
    
    # Family history
    if family_heart:
        risk_score += 8
    if family_cancer:
        risk_score += 6
    if family_diabetes:
        risk_score += 5
    
    # Lifestyle adjustments
    if exercise == "Regular (3+ times/week)" or exercise == "Athlete":
        risk_score -= 8
    elif exercise == "Rarely":
        risk_score += 5
    
    if alcohol == "Regular":
        risk_score += 8
    elif alcohol == "None":
        risk_score -= 3
    
    # Occupation risk
    if occupation in ["Construction Worker", "Driver"]:
        risk_score += 10
    elif occupation in ["Office Worker", "Software Engineer"]:
        risk_score -= 3
    
    # Ensure score is within bounds
    risk_score = max(0, min(100, risk_score))
    
    # Determine classification
    if risk_score < 30:
        classification = "Preferred"
        color = "green"
        decision = "✅ APPROVED"
        premium_multiplier = 0.85
    elif risk_score < 55:
        classification = "Standard"
        color = "blue"
        decision = "✅ APPROVED"
        premium_multiplier = 1.0
    elif risk_score < 75:
        classification = "Substandard"
        color = "orange"
        decision = "⚠️ APPROVED with CONDITIONS"
        premium_multiplier = 1.4
    else:
        classification = "High Risk"
        color = "red"
        decision = "❌ DECLINED - Refer to Manual Review"
        premium_multiplier = 2.0
    
    # Calculate base premium (simplified)
    base_annual_premium = 5000  # Base premium for 1M coverage
    age_factor = 1 + (age - 30) * 0.02
    final_premium = base_annual_premium * age_factor * premium_multiplier
    
    # OUTPUT SECTION
    st.markdown("")
    st.markdown("## AI Analysis Results")
    
    # Decision banner
    if "APPROVED" in decision and "CONDITIONS" not in decision:
        st.success(f"### {decision}")
    elif "CONDITIONS" in decision:
        st.warning(f"### {decision}")
    else:
        st.error(f"### {decision}")
    
    # Results in columns
    result_col1, result_col2, result_col3 = st.columns(3)
    
    with result_col1:
        st.metric("Risk Classification", classification)
        st.metric("BMI", f"{bmi:.1f}")
    
    with result_col2:
        st.metric("Risk Score", f"{risk_score}/100")
        if "APPROVED" in decision:
            st.metric("Coverage Amount", "¥10,000,000")
    
    with result_col3:
        if "APPROVED" in decision:
            st.metric("Annual Premium", f"¥{final_premium:,.0f}")
            st.caption(f"Premium multiplier: {premium_multiplier}x")
        else:
            st.metric("Recommended Action", "Manual Review")
    
    # Risk score visualization
    st.markdown("")
    st.markdown("#### Risk Score Breakdown")
    
    # Create a visual risk meter
    if risk_score < 30:
        meter_color = "🟢"
    elif risk_score < 55:
        meter_color = "🔵"
    elif risk_score < 75:
        meter_color = "🟠"
    else:
        meter_color = "🔴"
    
    meter = meter_color * int(risk_score / 5) + "⚪" * (20 - int(risk_score / 5))
    st.text(meter)
    st.caption(f"Risk Score: {risk_score}/100 - {classification}")
    
    # Key factors
    st.markdown("")
    st.markdown("#### Key Risk Factors Identified")
    factors = []
    
    if age > 50:
        factors.append(f"• Age: {age} years (increased risk)")
    if bmi > 25:
        factors.append(f"• BMI: {bmi:.1f} (overweight/obese)")
    if smoker == "Yes":
        factors.append("• Current smoker (significant risk factor)")
    if diabetes:
        factors.append("• Diabetes diagnosis")
    if heart_disease:
        factors.append("• Heart disease history")
    if cancer:
        factors.append("• Cancer history")
    if hypertension:
        factors.append("• Hypertension")
    if family_heart or family_cancer:
        factors.append("• Significant family medical history")
    if exercise == "Rarely":
        factors.append("• Sedentary lifestyle")
    if alcohol == "Regular":
        factors.append("• Regular alcohol consumption")
    
    if factors:
        for factor in factors:
            st.markdown(factor)
    else:
        st.markdown("• Excellent health profile")
        st.markdown("• No significant risk factors identified")
    
    # UNDER THE HOOD SECTION
    st.markdown("")
    st.divider()
    st.markdown("## 🔧 Under the Hood")
    
    tech_col1, tech_col2 = st.columns(2)
    
    with tech_col1:
        st.markdown("#### Machine Learning Model")
        st.markdown("""
        **Insurica uses a multi-layer neural network trained on:**
        - 500,000+ historical underwriting cases
        - Medical research databases
        - Actuarial mortality tables
        - Claims history data
        
        **Key Technologies:**
        - Deep Learning (TensorFlow)
        - Gradient Boosting (XGBoost)
        - Ensemble prediction methods
        - Real-time cloud processing
        """)
    
    with tech_col2:
        st.markdown("#### Data Processing Pipeline")
        st.markdown("""
        **Input Processing:**
        1. Data validation & normalization
        2. Feature engineering (BMI, age groups, risk categories)
        3. Medical history encoding
        4. Lifestyle factor weighting
        
        **Risk Assessment:**
        5. ML model inference (< 200ms)
        6. Multi-factor risk scoring
        7. Actuarial table comparison
        8. Final decision & premium calculation
        """)
    
    st.markdown("")
    st.markdown("#### Model Performance Metrics")
    perf_col1, perf_col2, perf_col3, perf_col4 = st.columns(4)
    
    with perf_col1:
        st.metric("Accuracy", "94.2%")
    with perf_col2:
        st.metric("Processing Time", "< 200ms")
    with perf_col3:
        st.metric("False Positive Rate", "2.1%")
    with perf_col4:
        st.metric("AUC-ROC Score", "0.96")
    
    st.info("💡 **Business Value:** Insurica reduces manual underwriting time from 3-5 days to under 1 second, while maintaining high accuracy and regulatory compliance.")

# Footer
st.markdown("")
st.divider()
col_footer1, col_footer2, col_footer3 = st.columns([2, 1, 2])
with col_footer2:
    st.caption("**Insurica by Nippofin**")
    st.caption("Demo Version 1.0")