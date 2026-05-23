import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_option_menu import option_menu

# --- 1. PREMIUM PRODUCTION INITIALIZATION ---
st.set_page_config(
    page_title="Chinar & Co. | Heritage Luxury Atelier",
    page_icon="🇵🇰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session States for Navigation Locking
if 'app_unlocked' not in st.session_state:
    st.session_state.app_unlocked = False

if 'cart' not in st.session_state:
    st.session_state.cart = {}

# --- 2. ELITE MINIMALIST UI CSS INJECTION ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=300;400;500;600&family=Syne:wght=400;500;600&display=swap');

    /* Persistent Canvas Overrides with Bright 3D Luxury Room Background */
    .stApp {
        background-image: linear-gradient(rgba(255, 255, 255, 0.45), rgba(255, 255, 255, 0.45)), 
                          url('https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1920&q=80') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }
    header, footer {visibility: hidden !important;}
    
    /* Modernist Minimal Container Card Matrix */
    .luxury-card {
        background: rgba(28, 25, 23, 0.85);
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border: 1px solid rgba(245, 245, 220, 0.2);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .luxury-card:hover {
        border: 1px solid rgba(245, 245, 220, 0.5);
        box-shadow: 0 30px 60px rgba(0, 0, 0, 0.4);
        transform: translateY(-3px);
    }
    
    /* CHANGED: Beige boxes with Black text */
    .inner-black-box {
        background-color: #f5f5dc !important;
        border: 1px solid #000000;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .inner-black-box p, .inner-black-box span, .inner-black-box div {
        color: #000000 !important;
    }

    /* Sleek Distinct Top Borders */
    .gold-accent-line {
        border-top: 2px solid #000000 !important;
    }
    
    /* Typography Overrides */
    .brand-title {
        font-family: 'Syne', sans-serif;
        font-weight: 600;
        letter-spacing: -0.02em;
        text-transform: none;
        color: #000000 !important;
        font-size: 2.8rem;
        margin: 0;
    }
    .brand-sub {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #000000 !important;
        font-size: 0.85rem;
        letter-spacing: 0.05em;
        margin: 8px 0 0 0;
        font-weight: 400;
    }
    
    .item-title {
        font-family: 'Syne', sans-serif;
        font-weight: 500;
        font-size: 1.3rem;
        letter-spacing: 0em;
        color: #000000 !important;
    }
    .item-meta {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #111111 !important;
        font-size: 0.8rem;
        font-weight: 400;
        margin-top: 4px;
    }
    
    /* Pricing Badge UI Elements */
    .gold-price-tag {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #000000 !important;
        font-weight: 500;
        font-size: 1.4rem;
        letter-spacing: -0.01em;
    }
    
    /* Navigation Header Component */
    .nav-header {
        font-family: 'Syne', sans-serif;
        font-weight: 500;
        letter-spacing: 0.05em;
        color: #f5f5dc !important;
        margin-bottom: 20px;
        font-size: 1.1rem;
        text-align: center;
    }

    /* Elegant Custom Overrides for Streamlit Forms and Inputs */
    div[data-baseweb="input"] {
        background-color: rgba(0, 0, 0, 0.05) !important;
        border: 1px solid rgba(0, 0, 0, 0.2) !important;
        border-radius: 8px !important;
    }
    div[data-baseweb="input"] input {
        color: #000000 !important;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 0.9rem;
    }
    
    /* CHANGED: Metrics inside beige boxes become black */
    div[data-testid="stMetricValue"] {
        font-family: 'Syne', sans-serif !important;
        color: #000000 !important;
        font-size: 1.8rem !important;
        font-weight: 500 !important;
    }
    div[data-testid="stMetricLabel"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #000000 !important;
        letter-spacing: 0.05em !important;
        font-size: 0.75rem !important;
    }

    /* Global Square Welcome Button Layout */
    .stButton > button {
        background: #000000 !important;
        color: #f5f5dc !important;
        border: 2px solid #f5f5dc !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        letter-spacing: 0.02em !important;
        font-weight: bold !important;
        font-size: 0.95rem !important;
        border-radius: 0px !important;
        padding: 12px 24px !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:hover {
        color: #000000 !important;
        border: 2px solid #000000 !important;
        background: #f5f5dc !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4) !important;
    }

    /* Fix Tab Item Styling */
    button[data-baseweb="tab"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 0.8rem !important;
        color: #222222 !important;
    }
    button[aria-selected="true"] {
        color: #000000 !important;
        font-weight: bold !important;
    }
    
    /* Global Text Elements */
    p, span, label, h1, h2, h3, h4, h5, h6 {
        color: #000000 !important;
    }
    
    /* Sidebar Structure */
    section[data-testid="stSidebar"] {
        background-color: #f5f5dc !important;
        border-right: 1px solid #000000;
    }
    section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] span {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)
