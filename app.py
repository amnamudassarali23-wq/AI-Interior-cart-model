# app.py

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

# Initialize Session States
if 'app_unlocked' not in st.session_state:
    st.session_state.app_unlocked = False

if 'cart' not in st.session_state:
    st.session_state.cart = {}

# --- 2. CSS INJECTION ---
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=300;400;500;600&family=Syne:wght=400;500;600&display=swap');

/* Background */
.stApp {
    background-image:
    linear-gradient(rgba(255,255,255,0.45), rgba(255,255,255,0.45)),
    url('https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1920&q=80') !important;

    background-size: cover !important;
    background-position: center !important;
    background-attachment: fixed !important;
}

header, footer {
    visibility: hidden !important;
}

/* Main Black Boxes */
.inner-black-box {
    background-color: #000000 !important;
    border: 2px solid #f5f5dc !important;
    padding: 18px;
    border-radius: 10px;
    margin-bottom: 12px;
}

/* Beige text inside black boxes */
.inner-black-box p,
.inner-black-box span,
.inner-black-box div,
.inner-black-box label,
.inner-black-box h1,
.inner-black-box h2,
.inner-black-box h3,
.inner-black-box h4,
.inner-black-box h5,
.inner-black-box h6 {
    color: #f5f5dc !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #000000 !important;
    border-right: 2px solid #f5f5dc !important;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] div,
section[data-testid="stSidebar"] label {
    color: #f5f5dc !important;
}

/* Brand */
.brand-title {
    font-family: 'Syne', sans-serif;
    font-weight: 600;
    color: #000000 !important;
    font-size: 2.8rem;
    margin: 0;
}

.brand-sub {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #000000 !important;
    font-size: 0.9rem;
    margin-top: 8px;
}

/* Buttons */
.stButton > button {
    background: #f5f5dc !important;
    color: #000000 !important;
    border: 2px solid #000000 !important;
    border-radius: 0px !important;
    font-weight: bold !important;
    font-size: 0.95rem !important;
    padding: 12px 24px !important;
    transition: 0.3s ease !important;
}

.stButton > button:hover {
    background: #000000 !important;
    color: #f5f5dc !important;
    border: 2px solid #f5f5dc !important;
}

/* Inputs */
div[data-baseweb="input"] {
    background-color: rgba(245,245,220,0.9) !important;
    border: 1px solid #000000 !important;
    border-radius: 8px !important;
}

div[data-baseweb="input"] input {
    color: #000000 !important;
}

/* Metrics */
div[data-testid="stMetricValue"] {
    color: #f5f5dc !important;
    font-size: 1.8rem !important;
    font-weight: bold !important;
}

div[data-testid="stMetricLabel"] {
    color: #f5f5dc !important;
}

/* Tabs */
button[data-baseweb="tab"] {
    color: #000000 !important;
    font-weight: 500 !important;
}

button[aria-selected="true"] {
    background-color: #000000 !important;
    color: #f5f5dc !important;
}

/* General Text */
p, span, label, h1, h2, h3, h4, h5, h6 {
    color: #000000 !important;
}

</style>
""", unsafe_allow_html=True)

# PRODUCTS
PRODUCTS = [
    {"id": 1, "name": "Velvet Chesterfield Sofa", "price": 2999, "category": "sofas", "image": "🛋️", "stock": 12},
    {"id": 2, "name": "Modern L-Shape Sofa", "price": 2499, "category": "sofas", "image": "🛋️", "stock": 8},
    {"id": 3, "name": "Luxury Leather Sectional", "price": 4999, "category": "sofas", "image": "🛋️", "stock": 5},
    {"id": 4, "name": "Marble Coffee Table", "price": 899, "category": "tables", "image": "☕", "stock": 15},
    {"id": 5, "name": "Oak Dining Table", "price": 1799, "category": "tables", "image": "🍽️", "stock": 10},
]

# HEADER
st.markdown("""
<div style="display:flex; justify-content:space-between; align-items:flex-end;
padding:20px 0 25px 0; border-bottom:2px solid #000000; margin-bottom:40px;">

<div>
<h1 class="brand-title">Chinar & Co.</h1>
<p class="brand-sub">Premium Heritage Craftsmanship for Architectural Interiors</p>
</div>

<div style="text-align:right;">
<p style="font-size:0.8rem; color:#000000;">LAHORE • KARACHI • ISLAMABAD</p>
</div>

</div>
""", unsafe_allow_html=True)

# LANDING PAGE
if not st.session_state.app_unlocked:

    st.markdown("""
    <div class="inner-black-box">
        <h2>Amna Mudassar Ali</h2>
        <p>Lead System Architect & Developer</p>

        <hr style="border:1px solid #f5f5dc;">

        <p><b>Academic Status:</b> First Semester Student</p>
        <p><b>Institution:</b> IIUI Islamabad</p>
        <p><b>Classification:</b> FIRST YEAR PROJECT (FYP)</p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "🌐 LinkedIn Profile",
        "https://www.linkedin.com/in/amna-mudassar-ali-64aa763ab",
        use_container_width=True
    )

    if st.button("Welcome", use_container_width=True):
        st.session_state.app_unlocked = True
        st.rerun()

# MAIN APP
else:

    cart_item_count = sum(st.session_state.cart.values())
    cart_total_price = sum(
        next(p['price'] for p in PRODUCTS if p['id'] == pid) * qty
        for pid, qty in st.session_state.cart.items()
    )

    # SIDEBAR
    with st.sidebar:

        selected = option_menu(
            menu_title=None,
            options=["Catalog", "Cart", "Dashboard", "Developer Info"],
            icons=["grid", "bag", "bar-chart", "person"],
            default_index=0,

            styles={
                "container": {
                    "padding": "5px",
                    "background-color": "#000000"
                },

                "icon": {
                    "color": "#f5f5dc",
                    "font-size": "14px"
                },

                "nav-link": {
                    "font-size": "13px",
                    "text-align": "left",
                    "margin": "6px",
                    "color": "#f5f5dc",
                    "background-color": "#000000",
                    "border": "1px solid #f5f5dc"
                },

                "nav-link-selected": {
                    "background-color": "#f5f5dc",
                    "color": "#000000",
                    "font-weight": "bold"
                }
            }
        )

    # METRICS
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown('<div class="inner-black-box">', unsafe_allow_html=True)
        st.metric("Products", len(PRODUCTS))
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="inner-black-box">', unsafe_allow_html=True)
        st.metric("Cart Items", cart_item_count)
        st.markdown('</div>', unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="inner-black-box">', unsafe_allow_html=True)
        st.metric("Total Price", f"${cart_total_price}")
        st.markdown('</div>', unsafe_allow_html=True)

    # CATALOG
    if selected == "Catalog":

        for item in PRODUCTS:

            st.markdown(f"""
            <div class="inner-black-box">

                <div style="display:flex; justify-content:space-between; align-items:center;">

                    <div>
                        <h3>{item['image']} {item['name']}</h3>
                        <p>Stock Available: {item['stock']}</p>
                    </div>

                    <div style="font-size:1.5rem; font-weight:bold;">
                        ${item['price']}
                    </div>

                </div>

            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Add {item['name']}", key=item['id']):
                st.session_state.cart[item['id']] = st.session_state.cart.get(item['id'], 0) + 1
                st.success(f"{item['name']} added to cart")
                st.rerun()

    # CART
    elif selected == "Cart":

        st.markdown("## Your Cart")

        if not st.session_state.cart:
            st.warning("Cart is empty")

        else:

            for pid, qty in st.session_state.cart.items():

                item = next(p for p in PRODUCTS if p['id'] == pid)

                st.markdown(f"""
                <div class="inner-black-box">
                    <h3>{item['name']}</h3>
                    <p>Quantity: {qty}</p>
                    <p>Total: ${item['price'] * qty}</p>
                </div>
                """, unsafe_allow_html=True)

    # DASHBOARD
    elif selected == "Dashboard":

        df = pd.DataFrame(PRODUCTS)

        fig = px.bar(
            df,
            x="name",
            y="price",
            color="category",
            title="Product Pricing Dashboard"
        )

        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color="#000000"
        )

        st.plotly_chart(fig, use_container_width=True)

    # DEVELOPER INFO
    elif selected == "Developer Info":

        st.markdown("""
        <div class="inner-black-box">
            <h2>Developer Information</h2>
            <p>Name: Amna Mudassar Ali</p>
            <p>University: IIUI Islamabad</p>
            <p>Program: First Semester</p>
        </div>
        """, unsafe_allow_html=True)
