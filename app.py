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
    
    /* Sleek Distinct Top Borders */
    .gold-accent-line {
        border-top: 2px solid #e6dfd3 !important;
    }
    
    /* Typography Overrides altered to Beige colors */
    .brand-title {
        font-family: 'Syne', sans-serif;
        font-weight: 600;
        letter-spacing: -0.02em;
        text-transform: none;
        background: linear-gradient(135deg, #ffffff 0%, #f5f5dc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.8rem;
        margin: 0;
    }
    .brand-sub {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #e6dfd3;
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
        color: #f5f5dc;
    }
    .item-meta {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #d4cbbe;
        font-size: 0.8rem;
        font-weight: 400;
        margin-top: 4px;
    }
    
    /* Pricing Badge UI Elements */
    .gold-price-tag {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #f5f5dc;
        font-weight: 500;
        font-size: 1.4rem;
        letter-spacing: -0.01em;
        text-shadow: 0 0 20px rgba(245, 245, 220, 0.2);
    }
    
    /* Navigation Header Component */
    .nav-header {
        font-family: 'Syne', sans-serif;
        font-weight: 500;
        letter-spacing: 0.05em;
        color: #f5f5dc;
        margin-bottom: 20px;
        font-size: 1.1rem;
        text-align: center;
    }

    /* Elegant Custom Overrides for Streamlit Forms and Inputs */
    div[data-baseweb="input"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(245, 245, 220, 0.2) !important;
        border-radius: 8px !important;
    }
    div[data-baseweb="input"] input {
        color: #f5f5dc !important;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 0.9rem;
    }
    
    /* Custom modifications for Streamlit default metrics */
    div[data-testid="stMetricValue"] {
        font-family: 'Syne', sans-serif !important;
        color: #f5f5dc !important;
        font-size: 1.8rem !important;
        font-weight: 500 !important;
    }
    div[data-testid="stMetricLabel"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #d4cbbe !important;
        letter-spacing: 0.05em !important;
        font-size: 0.75rem !important;
    }

    /* Global Modernist Button Styling Overrides */
    .stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: #e6dfd3 !important;
        border: 1px solid rgba(245, 245, 220, 0.3) !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        letter-spacing: 0.02em !important;
        font-weight: 500 !important;
        font-size: 0.8rem !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    .stButton > button:hover {
        color: #f5f5dc !important;
        border: 1px solid #f5f5dc !important;
        background: rgba(245, 245, 220, 0.1) !important;
        box-shadow: 0 4px 20px rgba(245, 245, 220, 0.2) !important;
    }
    .stButton [data-testid="stBaseButton-primary"] {
        background: #f5f5dc !important;
        color: #0b0d12 !important;
        border: 1px solid #f5f5dc !important;
        font-weight: 600 !important;
    }
    .stButton [data-testid="stBaseButton-primary"]:hover {
        background: #ffffff !important;
        color: #0b0d12 !important;
        border: 1px solid #ffffff !important;
        box-shadow: 0 6px 25px rgba(255, 255, 255, 0.25) !important;
    }

    /* Fix Tab Item Styling to match Minimalist Modern theme */
    button[data-baseweb="tab"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 0.8rem !important;
        color: #d4cbbe !important;
    }
    button[aria-selected="true"] {
        color: #f5f5dc !important;
    }
    p, span, label {
        color: #e6dfd3 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. PERSISTENT SYSTEM STATE STORAGE ---
if 'cart' not in st.session_state:
    st.session_state.cart = {}

PRODUCTS = [
    {"id": 1, "name": "Velvet Chesterfield Sofa", "price": 2999, "category": "sofas", "image": "🛋️", "stock": 12},
    {"id": 2, "name": "Modern L-Shape Sofa", "price": 2499, "category": "sofas", "image": "🛋️", "stock": 8},
    {"id": 3, "name": "Luxury Leather Sectional", "price": 4999, "category": "sofas", "image": "🛋️", "stock": 5},
    {"id": 4, "name": "Marble Coffee Table", "price": 899, "category": "tables", "image": "☕", "stock": 15},
    {"id": 5, "name": "Oak Dining Table", "price": 1799, "category": "tables", "image": "🍽️", "stock": 10},
    {"id": 6, "name": "Glass Side Table", "price": 299, "category": "tables", "image": "☕", "stock": 20},
    {"id": 7, "name": "Eames Lounge Chair", "price": 1299, "category": "chairs", "image": "🪑", "stock": 18},
    {"id": 8, "name": "Velvet Armchair", "price": 799, "category": "chairs", "image": "🪑", "stock": 25},
    {"id": 9, "name": "Bar Stool Set", "price": 599, "category": "chairs", "image": "🪑", "stock": 30},
    {"id": 10, "name": "Crystal Chandelier", "price": 2499, "category": "lighting", "image": "💡", "stock": 6},
    {"id": 11, "name": "Modern Floor Lamp", "price": 399, "category": "lighting", "image": "💡", "stock": 22},
    {"id": 12, "name": "Wall Sconces (Pair)", "price": 299, "category": "lighting", "image": "💡", "stock": 15},
    {"id": 13, "name": "Persian Rug 8x10", "price": 2999, "category": "decor", "image": "🧳", "stock": 4},
    {"id": 14, "name": "Wall Art Set", "price": 599, "category": "decor", "image": "🎨", "stock": 12},
    {"id": 15, "name": "Marble Vase", "price": 199, "category": "decor", "image": "🪴", "stock": 35}
]

# Metrics Computations
cart_item_count = sum(st.session_state.cart.values())
cart_total_price = sum(next(p['price'] for p in PRODUCTS if p['id'] == pid) * qty for pid, qty in st.session_state.cart.items())

# --- 4. NAVIGATION ARCHITECTURE ---
with st.sidebar:
    st.markdown("<br><div class='nav-header'>Chinar Directory</div>", unsafe_allow_html=True)
    selected = option_menu(
        menu_title=None,
        options=["Main Page", "Catalog", "Cart", "Checkout", "Dashboard"],
        icons=["info-circle", "grid", "bag", "credit-card", "pie-chart"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#d4cbbe", "font-size": "14px"}, 
            "nav-link": {"font-size": "13px", "text-align": "left", "margin":"6px", "color":"#e6dfd3", "font-family": "Plus Jakarta Sans", "font-weight": "400"},
            "nav-link-selected": {"background-color": "rgba(245, 245, 220, 0.2)", "color": "#f5f5dc", "border-left": "3px solid #f5f5dc"},
        }
    )

# --- 5. REFINED ATELIER HEADER ---
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: flex-end; padding: 20px 0 25px 0; border-bottom: 1px solid rgba(245,245,220,0.2); margin-bottom: 40px;">
        <div>
            <h1 class="brand-title">Chinar & Co.</h1>
            <p class="brand-sub">Premium Heritage Craftsmanship for Architectural Interiors</p>
        </div>
        <div style="text-align: right; font-family: 'Plus Jakarta Sans', sans-serif;">
            <p style="color: #d4cbbe; font-size: 0.7rem; letter-spacing: 0.05em; text-transform: uppercase; margin:0;">Atelier Flagship Network</p>
            <p style="color: #f5f5dc; font-size: 0.8rem; margin: 4px 0 0 0; font-weight: 500;">LAHORE • KARACHI • ISLAMABAD</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 6. ATELIER PERFORMANCE OVERLAYS ---
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.markdown('<div class="luxury-card gold-accent-line">', unsafe_allow_html=True)
    st.metric("Curated Designs", f"{len(PRODUCTS)} Items")
    st.markdown('</div>', unsafe_allow_html=True)

with metric_col2:
    st.markdown('<div class="luxury-card gold-accent-line">', unsafe_allow_html=True)
    st.metric("Cart Reservations", f"{cart_item_count} Units")
    st.markdown('</div>', unsafe_allow_html=True)

with metric_col3:
    st.markdown('<div class="luxury-card gold-accent-line">', unsafe_allow_html=True)
    st.metric("Total Portfolio Value", f"${cart_total_price:,.2f}")
    st.markdown('</div>', unsafe_allow_html=True)

with metric_col4:
    st.markdown('<div class="luxury-card gold-accent-line">', unsafe_allow_html=True)
    st.metric("Available Vault Stock", f"{sum(p['stock'] for p in PRODUCTS)} Units")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 7. ROUTING CORE MODULES ---
if selected == "Main Page":
    st.markdown("<h4 style='font-family:\"Syne\"; font-weight:500; color:#f5f5dc; margin-bottom:25px;'>PROJECT DEPLOYMENT INFORMATION</h4>", unsafe_allow_html=True)
    st.markdown("""
        <div class="luxury-card" style="border-top: 2px solid #f5f5dc; padding: 40px 30px;">
            <h2 style="font-family:'Syne'; color:#f5f5dc; font-weight:500; margin-bottom:5px;">Amna Mudassar Ali</h2>
            <p style="font-family:'Plus Jakarta Sans'; color:#e6dfd3; font-size:1.05rem; letter-spacing:0.02em; font-weight:300; margin-bottom:25px;">
                Lead System Architect & Developer
            </p>
            <hr style="border: 0; border-top: 1px solid rgba(245,245,220,0.2); margin-bottom:25px;">
            <div style="display: grid; grid-template-columns: 140px 1fr; row-gap: 15px; font-family:'Plus Jakarta Sans'; font-size:0.95rem; line-height:1.6;">
                <div style="color:#d4cbbe; font-weight:500;">Academic Status:</div>
                <div style="color:#e6dfd3;">Student of First Semester</div>
                <div style="color:#d4cbbe; font-weight:500;">Institution:</div>
                <div style="color:#e6dfd3;">International Islamic University, Islamabad (IIUI)</div>
                <div style="color:#d4cbbe; font-weight:500;">Classification:</div>
                <div style="color:#f5f5dc; font-weight:600; letter-spacing:0.05em;">FIRST YEAR PROJECT (FYP)</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.link_button("🌐 Connect on LinkedIn Profile", "https://www.linkedin.com/in/amna-mudassar-ali-64aa763ab?utm_source=share_via&utm_content=profile&utm_medium=member_android", use_container_width=True)

elif selected == "Catalog":
    
    filter_col1, filter_col2 = st.columns([3, 1])
    with filter_col1:
        search_query = st.text_input("🔍 Filter collections by keyword...", "").strip().lower()
    with filter_col2:
        price_bounds = st.slider("Price Window Range ($)", 0, 5000, (0, 5000))

    filtered = [
        p for p in PRODUCTS 
        if (not search_query or search_query in p['name'].lower()) and 
           (price_bounds[0] <= p['price'] <= price_bounds[1])
    ]

    t_sofa, t_table, t_chair, t_light, t_decor = st.tabs(["LIVING SEATING", "CENTRAL CONSOLES", "ATELIER DESK CHAIRS", "ARCHITECTURAL FIXTURES", "COLLECTOR PIECES"])
    categories = {"sofas": t_sofa, "tables": t_table, "chairs": t_chair, "lighting": t_light, "decor": t_decor}

    for cat_slug, tab_obj in categories.items():
        with tab_obj:
            cat_items = [p for p in filtered if p['category'] == cat_slug]
            if not cat_items:
                st.markdown("<p style='color:#e6dfd3; font-style:italic; padding: 20px 0; font-size:0.85rem;'>No editions match specified tracking limits inside this salon segment.</p>", unsafe_allow_html=True)
            
            for item in cat_items:
                st.markdown(f"""
                    <div class="luxury-card">
                        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
                            <div style="display: flex; align-items: center; gap: 25px;">
                                <div style="font-size: 2rem; background: rgba(255,255,255,0.01); padding: 10px 20px; border-radius: 12px; border: 1px solid rgba(245,245,220,0.2);">{item['image']}</div>
                                <div>
                                    <div class="item-title">{item['name']}</div>
                                    <div class="item-meta">Limited Production Manifest: <span style="color:#e6dfd3; font-weight:500;">{item['stock']} units remain</span></div>
                                </div>
                            </div>
                """, unsafe_allow_html=True)
                
                action_col1, action_col2 = st.columns([2, 1])
                with action_col1:
                    st.markdown(f'<div class="gold-price-tag" style="text-align:right; padding-top:4px;">${item['price']:,.2f}</div>', unsafe_allow_html=True)
                with action_col2:
                    if st.button("Acquire Lot Assignment", key=f"acq_{item['id']}", use_container_width=True):
                        st.session_state.cart[item['id']] = st.session_state.cart.get(item['id'], 0) + 1
                        st.toast(f"Allocated {item['name']} to your reservation catalog.", icon="⚡")
                        st.rerun()
                
                st.markdown("</div></div>", unsafe_allow_html=True)

elif selected == "Cart":
    st.markdown("<h4 style='font-family:\"Syne\"; font-weight:500; color:#ffffff; margin-bottom:25px;'>YOUR SELECTION PORTFOLIO</h4>", unsafe_allow_html=True)
    if not st.session_state.cart:
        st.markdown("<div class='luxury-card' style='color:#e6dfd3; font-style:italic; font-size:0.85rem;'>Your structural portfolio selection layout is currently empty.</div>", unsafe_allow_html=True)
    else:
        for pid, qty in list(st.session_state.cart.items()):
            item_details = next(p for p in PRODUCTS if p['id'] == pid)
            
            st.markdown(f"""
                <div class="luxury-card" style="padding: 16px 24px;">
                    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:15px;">
                        <div>
                            <span class="item-title" style="font-size:1.15rem;">{item_details['name']}</span>
                            <span style="color:#e6dfd3; font-size:0.85rem; font-family:'Plus Jakarta Sans'; margin-left:20px;">LOT YIELD: {qty}</span>
                        </div>
            """, unsafe_allow_html=True)
            
            c_price, c_btn = st.columns([3, 1])
            with c_price:
                st.markdown(f'<div class="gold-price-tag" style="text-align:right; padding-top:4px;">${item_details['price'] * qty:,.2f}</div>', unsafe_allow_html=True)
            with c_btn:
                if st.button("Release Unit Allocation", key=f"rel_{pid}", use_container_width=True):
                    del st.session_state.cart[pid]
                    st.rerun()
                
            st.markdown("</div></div>", unsafe_allow_html=True)

elif selected == "Checkout":
    st.markdown("<h4 style='font-family:\"Syne\"; font-weight:500; color:#ffffff; margin-bottom:25px;'>SECURE ESCROW TRANSFERS</h4>", unsafe_allow_html=True)
    if not st.session_state.cart:
        st.markdown("<div class='luxury-card' style='border-left: 2px solid #f5f5dc; color: #e6dfd3; font-family:\"Plus Jakarta Sans\"; font-size:0.85rem;'>Your current portfolio allocation is dry. Transaction engines cannot initialize without asset parameters.</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="luxury-card" style="text-align: center; padding: 45px 20px; border-top: 2px solid #f5f5dc;">
                <p style="font-family:'Plus Jakarta Sans'; color:#e6dfd3; text-transform:uppercase; letter-spacing:0.05em; margin:0; font-size:0.75rem;">Consolidated Bill Gross Balance</p>
                <div style="font-size: 3.2rem; font-weight:600; color:#ffffff; margin: 15px 0; font-family:'Syne';">${cart_total_price:,.2f}</div>
                <p style="color:#e6dfd3; font-size:0.85rem; max-width:520px; margin:0 auto 30px auto; font-family:'Plus Jakarta Sans'; line-height:1.6;">Confirming this data stream sets customized logistics chains in motion. Premium white-glove line deliveries will be routed immediately to your designated estate parameters.</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Approve Wire Clearing & Secure Transit Profile", type="primary", use_container_width=True):
            st.session_state.cart = {}
            st.balloons()
            st.success("Escrow clearance pipeline verified. Manifest arrays and custom shipment schedules have been forwarded.")
            st.rerun()

elif selected == "Dashboard":
    st.markdown("<h4 style='font-family:\"Syne\"; font-weight:500; color:#ffffff; margin-bottom:25px;'>ATELIER MARKET DEPLOYMENT LOGS</h4>", unsafe_allow_html=True)
    df = pd.DataFrame(PRODUCTS)
    
    beige_luxury_colors = ['#f5f5dc', '#ecdcb9', '#dfcaa3', '#cbb38a', '#ab946f']
    
    fig_scatter = px.scatter(
        df, x='price', y='stock', size='price', color='category', hover_name='name',
        title="Asset Valuation Distributions vs Stock Balance Matrix",
        color_discrete_sequence=beige_luxury_colors
    )
    fig_scatter.update_layout(
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        font_color="#e6dfd3", font_family="Plus Jakarta Sans", title_font_family="Syne", title_font_color="#ffffff", title_font_size=14
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        fig_pie = px.pie(df, names='category', values='stock', title="Lot Volume Storage Distributions", color_discrete_sequence=beige_luxury_colors)
        fig_pie.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="#e6dfd3", font_family="Plus Jakarta Sans", title_font_family="Syne", title_font_color="#ffffff", title_font_size=14)
        st.plotly_chart(fig_pie, use_container_width=True)
    with col_g2:
        fig_bar = px.bar(df, x='category', y='price', color='category', title="Geometric Structural Baseline Costs", color_discrete_sequence=beige_luxury_colors)
        fig_bar.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="#e6dfd3", font_family="Plus Jakarta Sans", title_font_family="Syne", title_font_color="#ffffff", title_font_size=14)
        st.plotly_chart(fig_bar, use_container_width=True)
