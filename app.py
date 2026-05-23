import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_option_menu import option_menu

# --- 1. PREMIUM PRODUCTION INITIALIZATION ---
st.set_page_config(
    page_title="Maison d'Art | Premium Luxury Interiors",
    page_icon="⚜️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. LUXURY ATELIER CSS INJECTION ---
st.markdown("""
    <style>
    /* Obsidian Dark Mode Canvas Background */
    .main { 
        background-color: #07090e; 
    }
    
    /* Clean up default Streamlit padding clutter */
    header {visibility: hidden;}
    
    /* Glassmorphism Luxury Product Panels */
    .luxury-card {
        background: rgba(18, 24, 38, 0.7);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.04);
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .luxury-card:hover {
        border: 1px solid rgba(212, 175, 55, 0.4);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
        transform: translateY(-2px);
    }
    
    /* Elegant Clean Font Hierarchy */
    .brand-title {
        font-family: 'Playfair Display', 'Didot', serif;
        font-weight: 200;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: #ffffff;
        font-size: 2.6rem;
        margin: 0;
    }
    .brand-sub {
        font-family: 'Inter', sans-serif;
        color: #64748b;
        font-size: 0.95rem;
        letter-spacing: 0.08em;
        margin: 6px 0 0 0;
        text-transform: uppercase;
    }
    
    .item-title {
        font-family: 'Inter', sans-serif;
        font-weight: 400;
        font-size: 1.25rem;
        letter-spacing: 0.02em;
        color: #ffffff;
        margin-bottom: 4px;
    }
    .item-meta {
        font-family: 'Inter', sans-serif;
        color: #94a3b8;
        font-size: 0.85rem;
    }
    
    /* Clean Luxury Currency Tagging */
    .gold-price-tag {
        font-family: 'Inter', sans-serif;
        color: #D4AF37;
        font-weight: 400;
        font-size: 1.4rem;
        letter-spacing: 0.02em;
        text-align: right;
        margin-bottom: 10px;
    }
    
    /* Accent Top Micro-bordering */
    .gold-accent-line {
        border-top: 2px solid #D4AF37;
    }
    
    /* Navigation Adjustments */
    .nav-header {
        font-family: 'Inter', sans-serif;
        font-weight: 300;
        letter-spacing: 0.06em;
        color: #D4AF37;
        text-transform: uppercase;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. PERSISTENT SYSTEM STATE STORAGE ---
if 'cart' not in st.session_state:
    st.session_state.cart = {}

# Premium Curated Architectural Data Catalog
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
    st.markdown("<div class='nav-header'>Maison Directory</div>", unsafe_allow_html=True)
    selected = option_menu(
        menu_title=None,
        options=["Catalog", "Cart", "Checkout", "Dashboard"],
        icons=["house-door", "bag-check", "credit-card", "graph-up"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#64748b", "font-size": "14px"}, 
            "nav-link": {"font-size": "14px", "text-align": "left", "margin":"5px", "color":"#f8fafc", "font-family": "Inter"},
            "nav-link-selected": {"background-color": "rgba(212, 175, 55, 0.15)", "color": "#D4AF37", "font-weight": "400", "border-left": "3px solid #D4AF37"},
        }
    )

# --- 5. REFINED ATELIER HEADER ---
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: flex-end; padding: 25px 0 35px 0; border-bottom: 1px solid rgba(255,255,255,0.05); margin-bottom: 40px;">
        <div>
            <h1 class="brand-title">Maison d'Art</h1>
            <p class="brand-sub">Curated Atelier Inventory for Discerning Spaces</p>
        </div>
        <div style="text-align: right;">
            <p style="font-family: 'Inter', sans-serif; color: #64748b; font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase; margin:0;">Operational Pulse</p>
            <p style="color: #D4AF37; font-size: 0.85rem; margin: 4px 0 0 0; letter-spacing: 0.05em;">● PARIS • MILAN • RAWALPINDI</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 6. HIGH-FIDELITY BUSINESS METRICS CONTAINER ---
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.markdown('<div class="luxury-card gold-accent-line">', unsafe_allow_html=True)
    st.metric("AVAILABLE EDITIONS", len(PRODUCTS))
    st.markdown('</div>', unsafe_allow_html=True)

with metric_col2:
    st.markdown('<div class="luxury-card gold-accent-line">', unsafe_allow_html=True)
    st.metric("BAG ALLOCATIONS", cart_item_count)
    st.markdown('</div>', unsafe_allow_html=True)

with metric_col3:
    st.markdown('<div class="luxury-card gold-accent-line">', unsafe_allow_html=True)
    st.metric("RUNNING STATEMENT", f"${cart_total_price:,.2f}")
    st.markdown('</div>', unsafe_allow_html=True)

with metric_col4:
    st.markdown('<div class="luxury-card gold-accent-line">', unsafe_allow_html=True)
    st.metric("ATELIER CAPACITY", f"{sum(p['stock'] for p in PRODUCTS)} Units")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 7. APPLICATIVE ROUTING ENGINE ---
if selected == "Catalog":
    
    # Refined Search & Filter Rails
    filter_col1, filter_col2 = st.columns([2, 1])
    with filter_col1:
        search_query = st.text_input("🔍 Search Atelier Collections...", "").strip().lower()
    with filter_col2:
        price_bounds = st.slider("Price Spectrum Limit ($)", 0, 5000, (0, 5000))

    # In-Memory Filtration
    filtered = [
        p for p in PRODUCTS 
        if (not search_query or search_query in p['name'].lower()) and 
           (price_bounds[0] <= p['price'] <= price_bounds[1])
    ]

    # Custom Curated Sub-Category Tabs
    t_sofa, t_table, t_chair, t_light, t_decor = st.tabs(["🛋️ SEATING", "☕ RECEPTIONS", "🪑 STUDY CHAIRS", "💡 LUMINAIRES", "🎨 SCULPTURAL DECOR"])
    categories = {"sofas": t_sofa, "tables": t_table, "chairs": t_chair, "lighting": t_light, "decor": t_decor}

    for cat_slug, tab_obj in categories.items():
        with tab_obj:
            cat_items = [p for p in filtered if p['category'] == cat_slug]
            if not cat_items:
                st.markdown("<p style='color:#64748b; font-style:italic;'>No standard releases verify your specified parameters in this salon.</p>", unsafe_allow_html=True)
            
            for item in cat_items:
                st.markdown(f"""
                    <div class="luxury-card">
                        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px;">
                            <div style="display: flex; align-items: center; gap: 25px;">
                                <div style="font-size: 2.5rem; background: rgba(255,255,255,0.02); padding: 10px 20px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.05);">{item['image']}</div>
                                <div>
                                    <div class="item-title">{item['name']}</div>
                                    <div class="item-meta">Limited Stock Production Block: <span style="color:#ffffff; font-weight:500;">{item['stock']} items available</span></div>
                                </div>
                            </div>
                            <div style="text-align: right; min-width: 150px;">
                                <div class="gold-price-tag">${item['price']:,.2f}</div>
                """, unsafe_allow_html=True)
                
                # Render Streamlit button inline safely outside HTML template block
                if st.button("Acquire Edition", key=f"acq_{item['id']}", use_container_width=True):
                    st.session_state.cart[item['id']] = st.session_state.cart.get(item['id'], 0) + 1
                    st.toast(f"Allocated {item['name']} to your Maison collection.", icon="⚜️")
                    st.rerun()
                    
                st.markdown("</div></div></div>", unsafe_allow_html=True)

elif selected == "Cart":
    st.markdown("<h2 style='font-weight:200; letter-spacing:0.04em; color:#ffffff; margin-bottom:25px;'>🛒 YOUR COLLECTION RETRIEVAL</h2>", unsafe_allow_html=True)
    if not st.session_state.cart:
        st.markdown("<p style='color:#64748b; font-style:italic;'>Your acquisition collection portfolio is currently empty.</p>", unsafe_allow_html=True)
    else:
        for pid, qty in list(st.session_state.cart.items()):
            item_details = next(p for p in PRODUCTS if p['id'] == pid)
            
            st.markdown(f"""
                <div class="luxury-card" style="margin-bottom:12px; padding:18px 24px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <span class="item-title" style="font-size:1.1rem;">{item_details['name']}</span>
                            <span style="color:#64748b; font-size:0.9rem; margin-left:20px;">Allocation Yield: {qty}</span>
                        </div>
                        <div style="display:flex; align-items:center; gap:30px;">
                            <span style="font-family:'Inter'; color:#D4AF37; font-size:1.1rem;">${item_details['price'] * qty:,.2f}</span>
            """, unsafe_allow_html=True)
            
            if st.button("Release Unit", key=f"rel_{pid}"):
                del st.session_state.cart[pid]
                st.rerun()
                
            st.markdown("</div></div></div>", unsafe_allow_html=True)

elif selected == "Checkout":
    st.markdown("<h2 style='font-weight:200; letter-spacing:0.04em; color:#ffffff; margin-bottom:25px;'>💳 SECURE TRANSFERS PROTOCOL</h2>", unsafe_allow_html=True)
    if not st.session_state.cart:
        st.markdown("<div class='luxury-card' style='border-left: 3px solid #f59e0b; color: #94a3b8;'>Your allocation cache is empty. Transaction processing cannot verify baseline inventory payloads.</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="luxury-card" style="text-align: center; padding: 40px 20px;">
                <p style="font-family:'Inter'; color:#64748b; text-transform:uppercase; letter-spacing:0.1em; margin:0;">Consolidated Invoice Balance</p>
                <div style="font-size: 3.2rem; font-weight:200; color:#ffffff; margin: 15px 0; font-family:'Playfair Display';">${cart_total_price:,.2f}</div>
                <p style="color:#94a3b8; font-size:0.9rem; max-width:500px; margin:0 auto 30px auto; font-weight:300;">Confirming authorization initializes global priority logistical routing arrays to secure residential destinations.</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Authorize Transfer and Secure Shipment", type="primary", use_container_width=True):
            st.session_state.cart = {}
            st.balloons()
            st.success("Transaction verified. Documentation files forwarded to your encrypted registrar.")
            st.rerun()

elif selected == "Dashboard":
    st.markdown("<h2 style='font-weight:200; letter-spacing:0.04em; color:#ffffff; margin-bottom:25px;'>📊 ATELIER LOGISTICS METRICS</h2>", unsafe_allow_html=True)
    df = pd.DataFrame(PRODUCTS)
    
    # Custom Dark High-Contrast Color Sequencing for Graphs
    luxury_colors = ['#D4AF37', '#1e293b', '#334155', '#475569', '#64748b']
    
    fig_scatter = px.scatter(
        df, x='price', y='stock', size='price', color='category', hover_name='name',
        title="Asset Valuation Profiles vs Stock Volatility Matrix",
        color_discrete_sequence=luxury_colors
    )
    fig_scatter.update_layout(
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        font_color="#94a3b8", title_font_family="Playfair Display", title_font_color="#ffffff"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        fig_pie = px.pie(df, names='category', values='stock', title="Total Volume Capacity Allocation Profiles", color_discrete_sequence=luxury_colors)
        fig_pie.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="#94a3b8", title_font_color="#ffffff")
        st.plotly_chart(fig_pie, use_container_width=True)
    with col_g2:
        fig_bar = px.bar(df, x='category', y='price', color='category', title="Geometric Asset Valuation Layouts", color_discrete_sequence=luxury_colors)
        fig_bar.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="#94a3b8", title_font_color="#ffffff")
        st.plotly_chart(fig_bar, use_container_width=True)
