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

    .stApp {
        background-image: linear-gradient(rgba(255, 255, 255, 0.45), rgba(255, 255, 255, 0.45)), 
                          url('https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1920&q=80') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }
    header, footer {visibility: hidden !important;}
    
    /* Beige background with black text */
    .luxury-card {
        background: rgba(245, 245, 220, 0.85);
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border: 1px solid rgba(245, 245, 220, 0.2);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        color: #000000 !important;
    }
    .luxury-card:hover {
        border: 1px solid rgba(245, 245, 220, 0.5);
        box-shadow: 0 30px 60px rgba(0, 0, 0, 0.4);
        transform: translateY(-3px);
    }

    /* Black background with beige text */
    .stButton > button {
        background: #000000 !important;
        color: #f5f5dc !important;
        border: 2px solid #f5f5dc !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
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

    /* Sidebar beige background with black text */
    section[data-testid="stSidebar"] {
        background-color: #f5f5dc !important;
        border-right: 1px solid #000000;
        color: #000000 !important;
    }
    section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] span {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Rest of your code remains unchanged ---
