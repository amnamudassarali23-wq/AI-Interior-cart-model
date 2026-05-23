import streamlit as st
import pandas as pd
import numpy as np

# Page Layout configuration
st.set_page_config(
    page_title="Nala Lai | Premium Operations Command",
    page_icon="⚜️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Executive Luxury CSS Injection ---
st.markdown("""
    <style>
    /* Dark Obsidian Background */
    .main { 
        background-color: #07090e; 
    }
    
    /* Clean up default Streamlit padding & clutter */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Luxury Glassmorphism Panel Cards */
    .luxury-card {
        background: rgba(15, 20, 30, 0.65);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .luxury-card:hover {
        border: 1px solid rgba(212, 175, 55, 0.3);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }
    
    /* Dynamic Threat Glow-borders */
    .border-gold { border-top: 3px solid #D4AF37; }
    .border-emerald { border-left: 4px solid #10b981; }
    .border-amber { border-left: 4px solid #f59e0b; }
    .border-crimson { border-left: 4px solid #ef4444; }
    
    /* Elegant Typography */
    .luxury-title {
        font-family: 'Helvetica Neue', Inter, sans-serif;
        font-weight: 300;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #94a3b8;
        font-size: 0.75rem;
    }
    .luxury-value {
        font-family: 'Helvetica Neue', Inter, sans-serif;
        font-weight: 400;
        letter-spacing: -0.03em;
        font-size: 2.2rem;
        color: #ffffff;
        margin: 5px 0;
    }
    
    /* Custom Metric Tweaks */
    div[data-testid="stMetricValue"] {
        font-weight: 300 !important;
        letter-spacing: -0.02em;
    }
    </style>
""", unsafe_transform=True)

# --- Sidebar Controls ---
st.sidebar.markdown("<h2 style='font-weight: 300; letter-spacing: 0.05em; color: #D4AF37;'>⚜️ SIMULATOR</h2>", unsafe_transform=True)
st.sidebar.markdown("Fine-tune parameters to preview state-changes across the custom UI layer.")
sim_rain = st.sidebar.slider("Simulated 6h Rain (mm)", 0.0, 45.0, 12.0)
sim_water = st.sidebar.slider("Current Gauge Level (ft)", 2.0, 22.0, 8.5)

# Strategic Status Matrix
if sim_rain > 20 or sim_water > 15:
    risk_class, risk_label, risk_color = "border-crimson", "CRITICAL THREAT EVENT", "#ef4444"
    risk_msg = "Disaster vectors active. Evacuation metrics achieved for Rawalpindi Sectors."
elif sim_rain > 8 or sim_water > 9:
    risk_class, risk_label, risk_color = "border-amber", "ELEVATED ALERT LEVEL", "#f59e0b"
    risk_msg = "Hydrological capacity narrowing near Katarian Bridge. Continuous monitoring."
else:
    risk_class, risk_label, risk_color = "border-emerald", "OPERATIONAL STATUS: NOMINAL", "#10b981"
    risk_msg = "Channels operating inside safe variances. No immediate hydrological distress."

# --- Elegant Header Architecture ---
st.markdown(f"""
    <div style="display: flex; justify-content: space-between; align-items: flex-end; padding: 20px 0 40px 0; border-bottom: 1px solid rgba(255,255,255,0.05); margin-bottom: 35px;">
        <div>
            <h1 style="font-weight: 200; font-size: 2.2rem; letter-spacing: 0.1em; color: #ffffff; margin: 0; text-transform: uppercase;">Nala Lai Intelligence</h1>
            <p style="color: #64748b; font-size: 0.9rem; letter-spacing: 0.05em; margin: 5px 0 0 0;">RAWALPINDI, PAKISTAN — COGNITIVE RISK ENGINE</p>
        </div>
        <div style="text-align: right;">
            <span class="luxury-title">System Pulse</span>
            <p style="color: #D4AF37; font-size: 0.9rem; font-weight: 400; margin: 5px 0 0 0; letter-spacing: 0.05em;">● LIVE ENGINES SYNCHRONIZED</p>
        </div>
    </div>
""", unsafe_transform=True)

# --- Top Level Alert Banner (Executive Interface) ---
st.markdown(f"""
    <div class="luxury-card {risk_class}">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
            <div style="flex: 1; min-width: 300px;">
                <span class="luxury-title" style="color: {risk_color}; font-weight: 600;">System Assessment Matrix</span>
                <div style="font-size: 1.6rem; font-weight: 300; color: #ffffff; margin: 5px 0; letter-spacing: 0.02em;">{risk_label}</div>
                <p style="margin: 0; color: #94a3b8; font-size: 0.95rem; font-weight: 300;">{risk_msg}</p>
            </div>
            <div style="padding-left: 30px; border-left: 1px solid rgba(255,255,255,0.05); text-align: left; min-width: 200px;">
                <span class="luxury-title">6H Probability</span>
                <div class="luxury-value" style="color: #D4AF37; font-weight: 300;">{min(100, int((sim_rain/45)*100))}%</div>
            </div>
        </div>
    </div>
""", unsafe_transform=True)

# --- Performance Indicators Matrix ---
m_col1, m_col2, m_col3, m_col4 = st.columns(4)

with m_col1:
    st.markdown("""<div class="luxury-card border-gold">""", unsafe_transform=True)
    st.metric(label="🌧️ 6H PRECIPITATION INTENSITY", value=f"{sim_rain} mm", delta="-1.4 mm / hr")
    st.markdown("""</div>""", unsafe_transform=True)

with m_col2:
    st.markdown("""<div class="luxury-card border-gold">""", unsafe_transform=True)
    st.metric(label="📏 CHANNEL GAUGE DEPTH", value=f"{sim_water} ft", delta="+0.8 ft (Surging)", delta_color="inverse")
    st.markdown("""</div>""", unsafe_transform=True)

with m_col3:
    st.markdown("""<div class="luxury-card border-gold">""", unsafe_transform=True)
    st.metric(label="⚡ DISCHARGE VELOCITY", value="4.1 m/s", delta="Averaged")
    st.markdown("""</div>""", unsafe_transform=True)

with m_col4:
    st.markdown("""<div class="luxury-card border-gold">""", unsafe_transform=True)
    st.metric(label="🛰️ LOGISTICS NETWORK", value="100%", delta="14 Nodes Operational")
    st.markdown("""</div>""", unsafe_transform=True)

# --- Visual Infrastructure Segment ---
layout_col1, layout_col2 = st.columns([1.3, 1])

with layout_col1:
    st.markdown("<p class='luxury-title' style='margin-bottom: 15px;'>📍 Spatial Telemetry Mapping</p>", unsafe_transform=True)
    # Generate balanced point clusters surrounding Nala Lai channels
    map_data = pd.DataFrame(
        np.random.randn(6, 2) / [190, 190] + [33.5973, 73.0479],
        columns=['lat', 'lon']
    )
    st.map(map_data, use_container_width=True)

with layout_col2:
    st.markdown("<p class='luxury-title' style='margin-bottom: 15px;'>📹 Deep-Neural Surveillance Feeds</p>", unsafe_transform=True)
    
    feed_tab1, feed_tab2 = st.tabs(["🔒 STATION 01: KATARIAN", "🔒 STATION 02: GANJMANDI"])
    
    with feed_tab1:
        st.markdown(f"""
            <div style="background-color: #0b0f17; border-radius: 8px; height: 260px; display: flex; flex-direction: column; justify-content: center; align-items: center; border: 1px solid rgba(212, 175, 55, 0.15); position: relative; overflow: hidden;">
                <div style="position: absolute; top: 15px; left: 15px; display: flex; align-items: center; gap: 8px;">
                    <span style="height: 8px; width: 8px; background-color: {risk_color}; border-radius: 50%; display: inline-block;"></span>
                    <span style="color: #64748b; font-size: 0.7rem; font-weight: 600; letter-spacing: 0.05em;">CV CORE ENGAGED</span>
                </div>
                <span style="font-size: 2.5rem; opacity: 0.35;">🌊</span>
                <p style="color: #64748b; font-size: 0.85rem; letter-spacing: 0.03em; margin-top: 15px; font-weight: 300;">Raw Video Processing Matrix</p>
                <p style="color: {risk_color}; font-size: 0.9rem; font-weight: 400; letter-spacing: 0.02em; margin: 3px 0 0 0;">
                    {"⚠️ ALERT: ANOMALOUS RADIAL PATTERNS / HUMAN DISCOVERED" if sim_water > 14 else "✓ NO CRITICAL INFRASTRUCTURE DEFECTS"}
                </p>
            </div>
        """, unsafe_transform=True)
        
    with feed_tab2:
        st.markdown("""
            <div style="background-color: #0b0f17; border-radius: 8px; height: 260px; display: flex; flex-direction: column; justify-content: center; align-items: center; border: 1px solid rgba(255, 255, 255, 0.05); position: relative; overflow: hidden;">
                <div style="position: absolute; top: 15px; left: 15px; display: flex; align-items: center; gap: 8px;">
                    <span style="height: 8px; width: 8px; background-color: #10b981; border-radius: 50%; display: inline-block;"></span>
                    <span style="color: #64748b; font-size: 0.7rem; font-weight: 600; letter-spacing: 0.05em;">CV CORE ENGAGED</span>
                </div>
                <span style="font-size: 2.5rem; opacity: 0.35;">🌉</span>
                <p style="color: #64748b; font-size: 0.85rem; letter-spacing: 0.03em; margin-top: 15px; font-weight: 300;">Structural Baseline Processing</p>
                <p style="color: #10b981; font-size: 0.9rem; font-weight: 400; letter-spacing: 0.02em; margin: 3px 0 0 0;">✓ FLOW CAPACITY WITHIN TOLERANCE LIMITS</p>
            </div>
        """, unsafe_transform=True)

# --- Clean Analytical Base ---
st.markdown("<br><br>", unsafe_transform=True)
st.markdown("<p class='luxury-title'>📈 Predictive Regression Matrix (24-Hour Delta)</p>", unsafe_transform=True)
chart_data = pd.DataFrame(
    np.random.randn(24, 2) + [10, 12],
    columns=['Hydric Volume Forecast', 'Empirical Measurement']
)
st.line_chart(chart_data, use_container_width=True)
