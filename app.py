import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_option_menu import option_menu

# --- 1. PREMIUM PRODUCTION INITIALIZATION ---
st.set_page_config(
    page_title="Maison d'Art | Elite Luxury Atelier",
    page_icon="⚜️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. ELITE BOUTIQUE UI CSS INJECTION ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&family=Inter:wght@200;300;400;500&display=swap');

    /* Persistent Canvas Overrides */
    .stApp {
        background-color: #07090e !important;
    }
    header {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    
    /* Luxury Glassmorphism Container Matrix */
    .luxury-card {
        background: linear-gradient(145deg, rgba(15, 20, 32, 0.8) 0%, rgba(10, 12, 18, 0.9) 100%);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(212, 175, 55, 0.08);
        border-radius: 16px;
        padding: 28px;
        margin-bottom: 24px;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
        transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .luxury-card:hover {
        border: 1px solid rgba(212, 175, 55, 0.35);
        box-shadow: 0 20px 50px rgba(212, 175, 55, 0.08);
        transform: translateY(-4px);
    }
    
    /* Fine-Line Distinct Top Borders */
    .gold-accent-line {
        border-top: 3px solid #D4AF37 !important;
    }
    
    /* Typography Overrides */
    .brand-title {
        font-family: 'Cinzel', serif;
        font-weight: 400;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        background: linear-gradient(135deg, #ffffff 0%, #a3b1cc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.8rem;
        margin: 0;
    }
    .brand-sub {
        font-family: 'Inter', sans-serif;
        color: #64748b;
        font-size: 0.85rem;
        letter-spacing: 0.12em;
        margin: 8px 0 0 0;
        text-transform: uppercase;
        font-weight: 300;
    }
    
    .item-title {
        font-family: 'Cinzel', serif;
        font-weight: 500;
        font-size: 1.3rem;
        letter-spacing: 0.05em;
        color: #ffffff;
        margin-bottom: 6px;
    }
    .item-meta {
        font-family: 'Inter', sans-serif;
        color: #64748b;
        font-size: 0.85rem;
        font-weight: 300;
    }
    
    /* Pricing Badge UI Elements */
    .gold-price-tag {
        font-family: 'Inter', sans-serif;
        color: #D4AF37;
        font-weight: 400;
        font-size: 1.5rem;
        letter-spacing: 0.04em;
        text-align: right;
        margin-bottom: 12px;
        text-shadow: 0 0 10px rgba(212, 175, 55, 0.2);
    }
    
    /* Sidebar Layout Modifications */
    .nav-header {
        font-family: 'Cinzel', serif;
        font-weight: 400;
        letter-spacing: 0.12em;
        color: #D4AF37;
        text-transform: uppercase;
        margin-bottom: 25px;
        font-size: 1.1rem;
        text-align: center;
    }

    /* Override default input elements to match dark luxury look */
    div[data-baseweb="input"] {
        background-color: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-radius: 8px !important;
    }
    div[data-baseweb="input"] input {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
    }
    
    /* Custom modifications for Streamlit default metrics */
    div[data-testid="stMetricValue"] {
        font-family: 'Cinzel', serif !important;
        color: #ffffff !important;
        font-size: 1.8rem !important;
        font-weight: 400 !important;
    }
    div[data-testid="stMetricLabel"] {
        font-family: 'Inter', sans-serif !important;
        color: #64748b !important;
        letter-spacing: 0.08em !important;
        text-transform: uppercase !important;
        font-size: 0.75rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. PERSISTENT SYSTEM STATE STORAGE ---
if 'cart' not in st.session_state:
    st.session_state.cart = {}

# Curated Product Dataset
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
    st.markdown("<br><div class='nav-header'>Maison Directory</div>", unsafe_allow_html=True)
    selected = option_menu(
        menu_title=None,
        options=["Catalog", "Cart", "Checkout", "Dashboard"],
        icons=["house", "bag", "credit-card", "activity"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#475569", "font-size": "14px"}, 
            "nav-link": {"font-size": "13px", "text-align": "left", "margin":"6px", "color":"#94a3b8", "font-family": "Inter", "letter-spacing": "0.05em", "text-transform": "uppercase"},
            "nav-link-selected": {"background-color": "rgba(212, 175, 55, 0.12)", "color": "#D4AF37", "font-weight": "400", "border-left": "4px solid #D4AF37"},
        }
    )

# --- 5. REFINED ATELIER HEADER ---
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: flex-end; padding: 30px 0 30px 0; border-bottom: 1px solid rgba(255,255,255,0.04); margin-bottom: 45px;">
        <div>
            <h1 class="brand-title">Maison d'Art</h1>
            <p class="brand-sub">Curated Atelier Collections for Discerning Architectural Spaces</p>
        </div>
        <div style="text-align: right; font-family: 'Inter', sans-serif;">
            <p style="color: #64748b; font-size: 0.7rem; letter-spacing: 0.12em; text-transform: uppercase; margin:0;">Global Distribution Pipeline</p>
            <p style="color: #D4AF37; font-size: 0.8rem; margin: 6px 0 0 0; letter-spacing: 0.08em; font-weight: 300;">● MILAN • PARIS • LONDON</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 6. ATELIER PERFORMANCE OVERLAYS ---
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.markdown('<div class="luxury-card gold-accent-line">', unsafe_allow_html=True)
    st.metric("Curated Editions", f"{len(PRODUCTS)} Items")
    st.markdown('</div>', unsafe_allow_html=True)

with metric_col2:
    st.markdown('<div class="luxury-card gold-accent-line">', unsafe_allow_html=True)
    st.metric("Bag Allocations", f"{cart_item_count} Units")
    st.markdown('</div>', unsafe_allow_html=True)

with metric_col3:
    st.markdown('<div class="luxury-card gold-accent-line">', unsafe_allow_html=True)
    st.metric("Portfolio Valuation", f"${cart_total_price:,.2f}")
    st.markdown('</div>', unsafe_allow_html=True)

with metric_col4:
    st.markdown('<div class="luxury-card gold-accent-line">', unsafe_allow_html=True)
    st.metric("Warehouse Capacity", f"{sum(p['stock'] for p in PRODUCTS)} Units")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 7. ROUTING CORE MODULES ---
if selected == "Catalog":
    
    # Clean Filter Interfaces
    filter_col1, filter_col2 = st.columns([2, 1])
    with filter_col1:
        search_query = st.text_input("🔍 Filter items by name keyword...", "").strip().lower()
    with filter_col2:
        price_bounds = st.slider("Atelier Price Limit Window ($)", 0, 5000, (0, 5000))

    # Filtration Layer
    filtered = [
        p for p in PRODUCTS 
        if (not search_query or search_query in p['name'].lower()) and 
           (price_bounds[0] <= p['price'] <= price_bounds[1])
    ]

    # Salon Navigation Tabs
    t_sofa, t_table, t_chair, t_light, t_decor = st.tabs(["🛋️ SEATING SELECTIONS", "☕ CENTRAL RECEPTIONS", "🪑 OFFICE CHAIRS", "💡 DESIGNER LUMINAIRES", "🎨 COLLECTOR DECOR"])
    categories = {"sofas": t_sofa, "tables": t_table, "chairs": t_chair, "lighting": t_light, "decor": t_decor}

    for cat_slug, tab_obj in categories.items():
        with tab_obj:
            cat_items = [p for p in filtered if p['category'] == cat_slug]
            if not cat_items:
                st.markdown("<p style='color:#475569; font-style:italic; padding: 20px 0;'>No editions match your parameters inside this category salon.</p>", unsafe_allow_html=True)
            
            for item in cat_items:
                st.markdown(f"""
                    <div class="luxury-card">
                        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
                            <div style="display: flex; align-items: center; gap: 30px;">
                                <div style="font-size: 2.4rem; background: rgba(255,255,255,0.01); padding: 12px 24px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.03);">{item['image']}</div>
                                <div>
                                    <div class="item-title">{item['name']}</div>
                                    <div class="item-meta">Limited Manufacturing Run: <span style="color:#e2e8f0; font-weight:400;">{item['stock']} items verified in stock</span></div>
                                </div>
                            </div>
                            <div style="text-align: right; min-width: 160px;">
                                <div class="gold-price-tag">${item['price']:,.2f}</div>
                """, unsafe_allow_html=True)
                
                # Render Acquisition Button safely
                if st.button("Acquire Premium Edition", key=f"acq_{item['id']}", use_container_width=True):
                    st.session_state.cart[item['id']] = st.session_state.cart.get(item['id'], 0) + 1
                    st.toast(f"Allocated {item['name']} to your custom collection.", icon="⚜️")
                    st.rerun()
                    
                st.markdown("</div></div></div>", unsafe_allow_html=True)

elif selected == "Cart":
    st.markdown("<h3 style='font-family:\"Cinzel\"; font-weight:400; letter-spacing:0.06em; color:#ffffff; margin-bottom:30px;'>🛒 YOUR SELECTION RUN</h3>", unsafe_allow_html=True)
    if not st.session_state.cart:
        st.markdown("<div class='luxury-card' style='color:#64748b; font-style:italic;'>Your custom portfolio allocation is currently blank.</div>", unsafe_allow_html=True)
    else:
        for pid, qty in list(st.session_state.cart.items()):
            item_details = next(p for p in PRODUCTS if p['id'] == pid)
            
            st.markdown(f"""
                <div class="luxury-card" style="margin-bottom:14px; padding:20px 28px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <span class="item-title" style="font-size:1.15rem;">{item_details['name']}</span>
                            <span style="color:#64748b; font-size:0.85rem; font-family:'Inter'; margin-left:25px; font-weight:300;">Allocated Yield: {qty}</span>
                        </div>
                        <div style="display:flex; align-items:center; gap:35px;">
                            <span style="font-family:'Inter'; color:#D4AF37; font-size:1.2rem; font-weight:400;">${item_details['price'] * qty:,.2f}</span>
            """, unsafe_allow_html=True)
            
            if st.button("Release Allocation", key=f"rel_{pid}"):
                del st.session_state.cart[pid]
                st.rerun()
                
            st.markdown("</div></div></div>", unsafe_allow_html=True)

elif selected == "Checkout":
    st.markdown("<h3 style='font-family:\"Cinzel\"; font-weight:400; letter-spacing:0.06em; color:#ffffff; margin-bottom:30px;'>💳 ESCROW & ROUTING ARRAY</h3>", unsafe_allow_html=True)
    if not st.session_state.cart:
        st.markdown("<div class='luxury-card' style='border-left: 3px solid #f59e0b; color: #94a3b8; font-family:\"Inter\"; font-weight:300;'>Your cart configuration pipeline is dry. Transaction operations cannot complete without valid baseline items.</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="luxury-card" style="text-align: center; padding: 50px 20px; border-top: 2px solid #D4AF37;">
                <p style="font-family:'Inter'; color:#64748b; text-transform:uppercase; letter-spacing:0.12em; margin:0; font-size:0.8rem; font-weight:300;">Consolidated Statement Gross Total</p>
                <div style="font-size: 3.6rem; font-weight:400; color:#ffffff; margin: 20px 0; font-family:'Cinzel'; text-shadow: 0 4px 20px rgba(0,0,0,0.5);">${cart_total_price:,.2f}</div>
                <p style="color:#64748b; font-size:0.9rem; max-width:550px; margin:0 auto 35px auto; font-family:'Inter'; font-weight:300; line-height:1.6;">Authorizing the transmission initializes customized logistics routing arrays. Priority shipping schedules will be arranged for your estate coordinates.</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Authorize Transfer and Secure Shipment Portfolio", type="primary", use_container_width=True):
            st.session_state.cart = {}
            st.balloons()
            st.success("Escrow cleared. Invoices and tracking profiles have been forwarded to your registered contact channel.")
            st.rerun()

elif selected == "Dashboard":
    st.markdown("<h3 style='font-family:\"Cinzel\"; font-weight:400; letter-spacing:0.06em; color:#ffffff; margin-bottom:30px;'>📊 ATELIER STOCK DISTRIBUTION METRICS</h3>", unsafe_allow_html=True)
    df = pd.DataFrame(PRODUCTS)
    
    # Custom Dark High-Contrast Color Palette for Plotly Charts
    luxury_colors = ['#D4AF37', '#1e293b', '#334155', '#475569', '#64748b']
    
    fig_scatter = px.scatter(
        df, x='price', y='stock', size='price', color='category', hover_name='name',
        title="Asset Valuation Models vs Stock Volatility Layouts",
        color_discrete_sequence=luxury_colors
    )
    fig_scatter.update_layout(
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        font_color="#94a3b8", font_family="Inter", title_font_family="Cinzel", title_font_color="#ffffff", title_font_size=16
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        fig_pie = px.pie(df, names='category', values='stock', title="Total Volume Capacity Profiles", color_discrete_sequence=luxury_colors)
        fig_pie.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="#94a3b8", font_family="Inter", title_font_family="Cinzel", title_font_color="#ffffff", title_font_size=15)
        st.plotly_chart(fig_pie, use_container_width=True)
    with col_g2:
        fig_bar = px.bar(df, x='category', y='price', color='category', title="Geometric Category Pricing Baselines", color_discrete_sequence=luxury_colors)
        fig_bar.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="#94a3b8", font_family="Inter", title_font_family="Cinzel", title_font_color="#ffffff", title_font_size=15)
        st.plotly_chart(fig_bar, use_container_width=True)
