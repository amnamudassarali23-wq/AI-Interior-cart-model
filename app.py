import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_option_menu import option_menu

# --- 1. PREMIUM PRODUCTION INITIALIZATION ---
st.set_page_config(
    page_title="Maison d'Art | Les Collections Haute Ébénisterie",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. ELITE BOUTIQUE UI CSS INJECTION ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&family=Inter:wght@200;300;400;500&display=swap');

    /* Persistent Canvas Overrides */
    .stApp {
        background-color: #05070a !important;
    }
    header, footer {visibility: hidden !important;}
    
    /* Luxury Glassmorphism Container Matrix */
    .luxury-card {
        background: linear-gradient(135deg, rgba(13, 17, 26, 0.7) 0%, rgba(7, 9, 15, 0.9) 100%);
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border: 1px solid rgba(212, 175, 55, 0.06);
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
        transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .luxury-card:hover {
        border: 1px solid rgba(212, 175, 55, 0.3);
        box-shadow: 0 25px 60px rgba(212, 175, 55, 0.05);
        transform: translateY(-2px);
    }
    
    /* Fine-Line Distinct Top Borders */
    .gold-accent-line {
        border-top: 2px solid #D4AF37 !important;
    }
    
    /* Typography Overrides */
    .brand-title {
        font-family: 'Cinzel', serif;
        font-weight: 400;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.6rem;
        margin: 0;
    }
    .brand-sub {
        font-family: 'Inter', sans-serif;
        color: #475569;
        font-size: 0.8rem;
        letter-spacing: 0.15em;
        margin: 10px 0 0 0;
        text-transform: uppercase;
        font-weight: 400;
    }
    
    .item-title {
        font-family: 'Cinzel', serif;
        font-weight: 400;
        font-size: 1.25rem;
        letter-spacing: 0.05em;
        color: #ffffff;
    }
    .item-meta {
        font-family: 'Inter', sans-serif;
        color: #64748b;
        font-size: 0.8rem;
        font-weight: 300;
        margin-top: 4px;
    }
    
    /* Pricing Badge UI Elements */
    .gold-price-tag {
        font-family: 'Inter', sans-serif;
        color: #D4AF37;
        font-weight: 400;
        font-size: 1.4rem;
        letter-spacing: 0.02em;
        text-shadow: 0 0 15px rgba(212, 175, 55, 0.15);
    }
    
    /* Navigation Header Component */
    .nav-header {
        font-family: 'Cinzel', serif;
        font-weight: 400;
        letter-spacing: 0.15em;
        color: #D4AF37;
        text-transform: uppercase;
        margin-bottom: 20px;
        font-size: 1rem;
        text-align: center;
    }

    /* Elegant Custom Overrides for Streamlit Forms and Inputs */
    div[data-baseweb="input"] {
        background-color: rgba(255, 255, 255, 0.01) !important;
        border: 1px solid rgba(255, 255, 255, 0.04) !important;
        border-radius: 4px !important;
    }
    div[data-baseweb="input"] input {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
        font-size: 0.9rem;
    }
    
    /* Custom modifications for Streamlit default metrics */
    div[data-testid="stMetricValue"] {
        font-family: 'Cinzel', serif !important;
        color: #ffffff !important;
        font-size: 1.6rem !important;
    }
    div[data-testid="stMetricLabel"] {
        font-family: 'Inter', sans-serif !important;
        color: #475569 !important;
        letter-spacing: 0.1em !important;
        text-transform: uppercase !important;
        font-size: 0.7rem !important;
    }

    /* Global Luxury Button Styling Overrides */
    .stButton > button {
        background: transparent !important;
        color: #94a3b8 !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        font-family: 'Inter', sans-serif !important;
        letter-spacing: 0.08em !important;
        text-transform: uppercase !important;
        font-size: 0.75rem !important;
        border-radius: 4px !important;
        padding: 8px 16px !important;
        transition: all 0.4s ease !important;
    }
    .stButton > button:hover {
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        background: rgba(212, 175, 55, 0.03) !important;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.1) !important;
    }
    .stButton [data-testid="stBaseButton-primary"] {
        background: rgba(212, 175, 55, 0.05) !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
    }
    .stButton [data-testid="stBaseButton-primary"]:hover {
        background: rgba(212, 175, 55, 0.12) !important;
        box-shadow: 0 4px 20px rgba(212, 175, 55, 0.2) !important;
    }

    /* Fix Tab Item Styling to match Dark Luxury theme */
    button[data-baseweb="tab"] {
        font-family: 'Inter', sans-serif !important;
        font-size: 0.75rem !important;
        letter-spacing: 0.1em !important;
        color: #475569 !important;
    }
    button[aria-selected="true"] {
        color: #D4AF37 !important;
    }
    div[data-絲id="stHorizontalBlock"] {
        align-items: center !important;
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
    st.markdown("<br><div class='nav-header'>Maison Directory</div>", unsafe_allow_html=True)
    selected = option_menu(
        menu_title=None,
        options=["Catalog", "Cart", "Checkout", "Dashboard"],
        icons=["compass", "handbag", "gold", "activity"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#334155", "font-size": "13px"}, 
            "nav-link": {"font-size": "12px", "text-align": "left", "margin":"6px", "color":"#64748b", "font-family": "Inter", "letter-spacing": "0.08em", "text-transform": "uppercase"},
            "nav-link-selected": {"background-color": "rgba(212, 175, 55, 0.08)", "color": "#D4AF37", "font-weight": "400", "border-left": "3px solid #D4AF37"},
        }
    )

# --- 5. REFINED ATELIER HEADER ---
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: flex-end; padding: 20px 0 25px 0; border-bottom: 1px solid rgba(255,255,255,0.03); margin-bottom: 40px;">
        <div>
            <h1 class="brand-title">Maison d'Art</h1>
            <p class="brand-sub">Les Collections Haute Ébénisterie Pour Les Espaces Singuliers</p>
        </div>
        <div style="text-align: right; font-family: 'Inter', sans-serif;">
            <p style="color: #334155; font-size: 0.65rem; letter-spacing: 0.15em; text-transform: uppercase; margin:0;">Atelier Network Status</p>
            <p style="color: #D4AF37; font-size: 0.75rem; margin: 4px 0 0 0; letter-spacing: 0.1em; font-weight: 300;">MILAN • PARIS • GENEVA</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 6. ATELIER PERFORMANCE OVERLAYS ---
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.markdown('<div class="luxury-card gold-accent-line">', unsafe_allow_html=True)
    st.metric("Curated Works", f"{len(PRODUCTS)} Editions")
    st.markdown('</div>', unsafe_allow_html=True)

with metric_col2:
    st.markdown('<div class="luxury-card gold-accent-line">', unsafe_allow_html=True)
    st.metric("Bag Allocations", f"{cart_item_count} Units")
    st.markdown('</div>', unsafe_allow_html=True)

with metric_col3:
    st.markdown('<div class="luxury-card gold-accent-line">', unsafe_allow_html=True)
    st.metric("Statement Value", f"${cart_total_price:,.2f}")
    st.markdown('</div>', unsafe_allow_html=True)

with metric_col4:
    st.markdown('<div class="luxury-card gold-accent-line">', unsafe_allow_html=True)
    st.metric("Available Lot Assets", f"{sum(p['stock'] for p in PRODUCTS)} Units")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 7. ROUTING CORE MODULES ---
if selected == "Catalog":
    
    filter_col1, filter_col2 = st.columns([3, 1])
    with filter_col1:
        search_query = st.text_input("🔍 Search collections by structural keyword...", "").strip().lower()
    with filter_col2:
        price_bounds = st.slider("Price Spectrum Limit ($)", 0, 5000, (0, 5000))

    filtered = [
        p for p in PRODUCTS 
        if (not search_query or search_query in p['name'].lower()) and 
           (price_bounds[0] <= p['price'] <= price_bounds[1])
    ]

    t_sofa, t_table, t_chair, t_light, t_decor = st.tabs(["SEATING SELECTIONS", "CENTRAL RECEPTIONS", "WORKSTUDY CHAIRS", "DESIGNER LUMINAIRES", "COLLECTOR DECOR"])
    categories = {"sofas": t_sofa, "tables": t_table, "chairs": t_chair, "lighting": t_light, "decor": t_decor}

    for cat_slug, tab_obj in categories.items():
        with tab_obj:
            cat_items = [p for p in filtered if p['category'] == cat_slug]
            if not cat_items:
                st.markdown("<p style='color:#334155; font-style:italic; padding: 20px 0; font-size:0.85rem;'>No editions match specified tracking limits inside this salon segment.</p>", unsafe_allow_html=True)
            
            for item in cat_items:
                # We open the card container using HTML layout styling
                st.markdown(f"""
                    <div class="luxury-card">
                        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
                            <div style="display: flex; align-items: center; gap: 25px;">
                                <div style="font-size: 2rem; background: rgba(255,255,255,0.01); padding: 10px 20px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">{item['image']}</div>
                                <div>
                                    <div class="item-title">{item['name']}</div>
                                    <div class="item-meta">Limited Production Release: <span style="color:#94a3b8; font-weight:400;">{item['stock']} units registered</span></div>
                                </div>
                            </div>
                """, unsafe_allow_html=True)
                
                # Create clear grid system layout via native columns for functional buttons and labels
                action_col1, action_col2 = st.columns([2, 1])
                with action_col1:
                    st.markdown(f'<div class="gold-price-tag" style="text-align:right; padding-top:4px;">${item['price']:,.2f}</div>', unsafe_allow_html=True)
                with action_col2:
                    if st.button("Acquire Lot Piece", key=f"acq_{item['id']}", use_container_width=True):
                        st.session_state.cart[item['id']] = st.session_state.cart.get(item['id'], 0) + 1
                        st.toast(f"Allocated {item['name']} to your portfolio allocation.", icon="⚜️")
                        st.rerun()
                
                st.markdown("</div></div>", unsafe_allow_html=True)

elif selected == "Cart":
    st.markdown("<h4 style='font-family:\"Cinzel\"; font-weight:400; letter-spacing:0.08em; color:#ffffff; margin-bottom:25px;'>YOUR RESERVATION PORTFOLIO</h4>", unsafe_allow_html=True)
    if not st.session_state.cart:
        st.markdown("<div class='luxury-card' style='color:#475569; font-style:italic; font-size:0.85rem;'>Your custom portfolio allocation is currently blank.</div>", unsafe_allow_html=True)
    else:
        for pid, qty in list(st.session_state.cart.items()):
            item_details = next(p for p in PRODUCTS if p['id'] == pid)
            
            st.markdown(f"""
                <div class="luxury-card" style="padding: 16px 24px;">
                    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:15px;">
                        <div>
                            <span class="item-title" style="font-size:1.15rem;">{item_details['name']}</span>
                            <span style="color:#475569; font-size:0.8rem; font-family:'Inter'; margin-left:20px; font-weight:400;">ALLOCATED: {qty}</span>
                        </div>
            """, unsafe_allow_html=True)
            
            c_price, c_btn = st.columns([3, 1])
            with c_price:
                st.markdown(f'<div class="gold-price-tag" style="text-align:right; padding-top:4px;">${item_details['price'] * qty:,.2f}</div>', unsafe_allow_html=True)
            with c_btn:
                if st.button("Release Lot Piece", key=f"rel_{pid}", use_container_width=True):
                    del st.session_state.cart[pid]
                    st.rerun()
                
            st.markdown("</div></div>", unsafe_allow_html=True)

elif selected == "Checkout":
    st.markdown("<h4 style='font-family:\"Cinzel\"; font-weight:400; letter-spacing:0.08em; color:#ffffff; margin-bottom:25px;'>SECURE ESCROW LOGISTICS INTERFACE</h4>", unsafe_allow_html=True)
    if not st.session_state.cart:
        st.markdown("<div class='luxury-card' style='border-left: 2px solid #D4AF37; color: #475569; font-family:\"Inter\"; font-size:0.85rem;'>Your acquisition pipeline is dry. Escrow networks cannot process transactions without valid baseline payloads.</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="luxury-card" style="text-align: center; padding: 45px 20px; border-top: 2px solid #D4AF37;">
                <p style="font-family:'Inter'; color:#475569; text-transform:uppercase; letter-spacing:0.12em; margin:0; font-size:0.75rem;">Consolidated Acquisition Gross Statement</p>
                <div style="font-size: 3.2rem; font-weight:400; color:#ffffff; margin: 15px 0; font-family:'Cinzel';">${cart_total_price:,.2f}</div>
                <p style="color:#475569; font-size:0.85rem; max-width:520px; margin:0 auto 30px auto; font-family:'Inter'; font-weight:300; line-height:1.6;">Finalizing the digital validation authorizes white-glove transport routing arrays. Bespoke asset management handling updates will be assigned directly to your primary coordinates.</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Authorize Wire Transfer & Finalize Lot Shipment", type="primary", use_container_width=True):
            st.session_state.cart = {}
            st.balloons()
            st.success("Escrow clearance processing authorized. Manifest profiles have been delivered via registered accounts.")
            st.rerun()

elif selected == "Dashboard":
    st.markdown("<h4 style='font-family:\"Cinzel\"; font-weight:400; letter-spacing:0.08em; color:#ffffff; margin-bottom:25px;'>ATELIER ASSET DEPLOYMENT FORECASTS</h4>", unsafe_allow_html=True)
    df = pd.DataFrame(PRODUCTS)
    
    luxury_colors = ['#D4AF37', '#111726', '#1e293b', '#334155', '#475569']
    
    fig_scatter = px.scatter(
        df, x='price', y='stock', size='price', color='category', hover_name='name',
        title="Asset Valuation Models vs Stock Volatility Layouts",
        color_discrete_sequence=luxury_colors
    )
    fig_scatter.update_layout(
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        font_color="#64748b", font_family="Inter", title_font_family="Cinzel", title_font_color="#ffffff", title_font_size=14
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        fig_pie = px.pie(df, names='category', values='stock', title="Total Volume Capacity Profiles", color_discrete_sequence=luxury_colors)
        fig_pie.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="#64748b", font_family="Inter", title_font_family="Cinzel", title_font_color="#ffffff", title_font_size=14)
        st.plotly_chart(fig_pie, use_container_width=True)
    with col_g2:
        fig_bar = px.bar(df, x='category', y='price', color='category', title="Geometric Category Pricing Baselines", color_discrete_sequence=luxury_colors)
        fig_bar.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="#64748b", font_family="Inter", title_font_family="Cinzel", title_font_color="#ffffff", title_font_size=14)
        st.plotly_chart(fig_bar, use_container_width=True)
