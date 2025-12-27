# Insurica - AI-Powered Life Insurance Underwriting Demo

Modern, clean UI demo showcasing AI-powered instant underwriting decisions.

## Files Included

- `streamlit_app.py` - Main application with updated modern styling
- `.streamlit/config.toml` - Theme configuration for clean, professional look
- `nippotica_icon.png` - Company icon
- `requirements.txt` - Python dependencies

## Deployment Instructions

### Local Deployment

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
streamlit run streamlit_app.py
```

### Streamlit Cloud Deployment

1. Push this folder to GitHub
2. Go to share.streamlit.io
3. Select your repository
4. The app will automatically use the `.streamlit/config.toml` for styling

## Styling Features

The app now uses:
- **Clean white background** with subtle gray accents
- **Modern Inter font** throughout
- **Professional blue** primary color (#4F8BF9)
- **Refined typography** with proper heading hierarchy
- **Cleaner spacing** with `st.markdown("")` instead of dividers
- **Centered button layout** for better visual flow
- **Modern dividers** using `st.divider()` instead of markdown separators

## Demo Scenarios

- **Low Risk**: Healthy 30-year-old with no risk factors
- **Standard Risk**: 45-year-old with mild hypertension
- **High Risk**: 55-year-old smoker with multiple conditions

## About Insurica

Insurica demonstrates AI-powered underwriting with:
- Real-time risk assessment (< 200ms)
- 94%+ accuracy on historical data
- Multi-factor ML model
- Instant premium calculation

Powered by Nippotica's Nippofin Business Unit
