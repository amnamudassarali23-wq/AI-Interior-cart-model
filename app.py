"""
AI Interior Designing - Transform Your Space With Artificial Intelligence
Developer: Amna Mudassar Ali (amnamudassarali23@gmail.com)
A SaaS-grade Streamlit web application utilizing AI for interior design visualization.
"""

import os
import io
import time
import urllib.parse
import requests
from typing import Tuple, Optional

import streamlit as st
from PIL import Image

# -----------------------------------------------------------------------------
# Streamlit Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="AI Interior Designing | Amna Mudassar Ali",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# -----------------------------------------------------------------------------
# Styling & Custom CSS (NavBlue & Cream Interior Design Theme)
# -----------------------------------------------------------------------------
def apply_custom_css():
    """Injects NavBlue (#0B2545) & Cream (#FDFBF7) theme styling with custom design graphics."""
    custom_css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #0B2545;
    }

    .stApp {
        background-color: #FDFBF7;
    }

    .design-hero-bg {
        position: relative;
        background: linear-gradient(135deg, rgba(11, 37, 69, 0.95) 0%, rgba(19, 49, 92, 0.92) 100%),
                    radial-gradient(circle at 50% 50%, rgba(197, 160, 89, 0.15) 0%, transparent 60%);
        border-radius: 24px;
        padding: 70px 30px;
        text-align: center;
        color: #FDFBF7;
        box-shadow: 0 20px 40px rgba(11, 37, 69, 0.15);
        border: 1px solid rgba(197, 160, 89, 0.3);
        margin-bottom: 30px;
        overflow: hidden;
    }

    .brand-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 700;
        letter-spacing: -0.02em;
        color: #FDFBF7;
        margin-bottom: 10px;
    }

    .developer-card {
        display: inline-block;
        background: rgba(253, 251, 247, 0.12);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(197, 160, 89, 0.4);
        padding: 14px 28px;
        border-radius: 50px;
        margin-top: 15px;
        margin-bottom: 20px;
    }

    .developer-name {
        font-size: 1.2rem;
        font-weight: 600;
        color: #EEF4F8;
    }

    .developer-email {
        font-size: 0.9rem;
        color: #C5A059;
        font-weight: 500;
    }

    .glass-card {
        background: #FFFFFF;
        border: 1px solid #EEF2F6;
        border-radius: 18px;
        padding: 24px;
        box-shadow: 0 10px 25px -5px rgba(11, 37, 69, 0.05);
        margin-bottom: 24px;
        transition: transform 0.25s ease, box-shadow 0.25s ease;
    }

    .glass-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 30px -5px rgba(11, 37, 69, 0.08);
        border-color: #C5A059;
    }

    .stButton>button {
        background: #0B2545 !important;
        color: #FDFBF7 !important;
        border-radius: 12px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        border: 1px solid #0B2545 !important;
        box-shadow: 0 4px 14px 0 rgba(11, 37, 69, 0.15) !important;
        transition: all 0.25s ease !important;
        width: 100%;
    }

    .stButton>button:hover {
        background: #13315C !important;
        border-color: #C5A059 !important;
        color: #C5A059 !important;
        transform: translateY(-2px);
    }

    /* Sidebar Visible Fix & Navigation Buttons Styling */
    section[data-testid="stSidebar"] {
        background-color: #0B2545 !important;
        min-width: 280px !important;
        max-width: 320px !important;
    }

    section[data-testid="stSidebar"] * {
        color: #FDFBF7 !important;
    }

    section[data-testid="stSidebar"] .stButton>button {
        background: rgba(253, 251, 247, 0.08) !important;
        color: #FDFBF7 !important;
        border: 1px solid rgba(197, 160, 89, 0.3) !important;
        margin-bottom: 8px !important;
        text-align: left !important;
        padding: 12px 18px !important;
    }

    section[data-testid="stSidebar"] .stButton>button:hover {
        background: #C5A059 !important;
        color: #0B2545 !important;
        border-color: #C5A059 !important;
    }

    /* Ensure Sidebar collapse/expand button is styled and visible */
    [data-testid="stSidebarCollapseButton"] {
        color: #0B2545 !important;
        background-color: #FDFBF7 !important;
        border-radius: 50% !important;
    }

    .section-header {
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: #0B2545;
        margin-bottom: 16px;
        border-bottom: 2px solid #C5A059;
        padding-bottom: 4px;
        display: inline-block;
    }

    .theme-badge {
        display: inline-block;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
        background: #13315C;
        color: #C5A059;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 14px;
    }

    .footer {
        text-align: center;
        padding: 25px 0 15px 0;
        font-size: 0.85rem;
        color: #13315C;
        border-top: 1px solid rgba(197, 160, 89, 0.3);
        margin-top: 50px;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# Session State Initialization
# -----------------------------------------------------------------------------
def init_session_state():
    """Ensures necessary session state key-value pairs are properly initialized."""
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Home"
    if "gallery" not in st.session_state:
        st.session_state["gallery"] = []
    if "last_generated" not in st.session_state:
        st.session_state["last_generated"] = None


# -----------------------------------------------------------------------------
# Prompt Construction Engine
# -----------------------------------------------------------------------------
def build_design_prompt(
    room_type: str,
    room_shape: str,
    room_size: str,
    style: str,
    primary_color: str,
    secondary_color: str,
    accent_color: str,
    color_preset: str,
    furniture: list,
    lighting: str,
    flooring: str,
    additional_reqs: str
) -> Tuple[str, str]:
    """Assembles structured inputs into an optimized, photorealistic text prompt."""
    
    if color_preset != "Custom":
        color_description = f"{color_preset} color scheme"
    else:
        color_description = f"custom palette with primary hex {primary_color}, secondary hex {secondary_color}, and accent hex {accent_color}"

    furniture_str = ", ".join(furniture) if furniture else "minimal essential furniture"

    positive_prompt = (
        f"A ultra-realistic high-end interior architecture photo of a {room_size.lower()} {room_shape.lower()} {room_type.lower()}. "
        f"Style: {style} interior design. Color theme: {color_description}. "
        f"Furniture included: {furniture_str}. Flooring: {flooring}. Lighting: {lighting}. "
    )

    if additional_reqs.strip():
        positive_prompt += f"Specific elements: {additional_reqs.strip()}. "

    positive_prompt += (
        "Architectural Digest, realistic lighting, 8k resolution, ray-tracing, detailed textures, clean composition, soft shadows, magazine aesthetic."
    )

    negative_prompt = "blurry, dark, ugly, deformed furniture, text, watermark, bad architecture, warped walls, low quality, noise"

    return positive_prompt, negative_prompt


# -----------------------------------------------------------------------------
# Fast High-Quality Cloud AI Image Generator
# -----------------------------------------------------------------------------
def generate_interior_design(prompt: str, seed: Optional[int] = None) -> Optional[Image.Image]:
    """Generates real photorealistic interior design images using cloud inference."""
    try:
        encoded_prompt = urllib.parse.quote(prompt)
        
        if seed is None:
            seed = int(time.time())
            
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=768&seed={seed}&nologo=true&model=flux"
        
        response = requests.get(image_url, timeout=30)
        
        if response.status_code == 200:
            img = Image.open(io.BytesIO(response.content))
            return img
        else:
            st.error("Failed to fetch image from AI engine. Please try again.")
            return None
    except Exception as e:
        st.error(f"Error during image generation: {str(e)}")
        return None


# -----------------------------------------------------------------------------
# PAGE 1: HOME
# -----------------------------------------------------------------------------
def home_page():
    st.markdown(
        """
        <div class="design-hero-bg">
            <span class="theme-badge">Architectural AI Platform</span>
            <div class="brand-title">AI Interior Designing</div>
            <p style="font-size:1.2rem; color:#E0E6ED; max-width:680px; margin:0 auto 18px auto; font-weight:300;">
                Transforming spatial concepts into realistic interior visualizations through generative artificial intelligence.
            </p>
            <div class="developer-card">
                <div class="developer-name">Developed by Amna Mudassar Ali</div>
                <div class="developer-email">✉ amnamudassarali23@gmail.com</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col_b1, col_b2, col_b3 = st.columns([1, 1.2, 1])
    with col_b2:
        if st.button("Launch AI Studio →", key="home_studio_btn"):
            st.session_state["current_page"] = "AI Designer"
            st.rerun()

    st.markdown("<br><hr style='border-color: rgba(197, 160, 89, 0.2);'><br>", unsafe_allow_html=True)

    f1, f2, f3 = st.columns(3)
    with f1:
        st.markdown(
            """
            <div class="glass-card">
                <h3 style="color:#0B2545; font-family:'Playfair Display', serif;">✨ Intelligent Synthesis</h3>
                <p style="color:#13315C; font-size:0.9rem;">Generate bespoke spatial concepts using tailored architectural prompts.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with f2:
        st.markdown(
            """
            <div class="glass-card">
                <h3 style="color:#0B2545; font-family:'Playfair Display', serif;">📐 Spatial Precision</h3>
                <p style="color:#13315C; font-size:0.9rem;">Specify room sizes, furniture arrays, custom lighting, and exact color palettes.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with f3:
        st.markdown(
            """
            <div class="glass-card">
                <h3 style="color:#0B2545; font-family:'Playfair Display', serif;">🛋️ 10+ Design Styles</h3>
                <p style="color:#13315C; font-size:0.9rem;">Explore Modern, Japandi, Scandinavian, Industrial, Luxury, and Minimalist aesthetics.</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# -----------------------------------------------------------------------------
# PAGE 2: AI DESIGNER
# -----------------------------------------------------------------------------
def designer_page():
    st.markdown('<div class="section-header">AI Interior Studio</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#13315C; margin-bottom:20px;">Configure room parameters below to generate your customized design concept.</p>', unsafe_allow_html=True)

    col_left, col_right = st.columns([1.1, 0.9], gap="large")

    with col_left:
        # Section 1: Room Specs
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">1. Room Specifications</div>', unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        with c1:
            room_type = st.selectbox("Room Type", [
                "Living Room", "Bedroom", "Kitchen", "Bathroom", "Dining Room",
                "Office", "Study Room", "Gaming Room", "Kids Room", "Guest Room", "Drawing Room"
            ])
        with c2:
            room_shape = st.selectbox("Room Shape", ["Square", "Rectangle", "L-Shaped", "Open Plan", "Narrow", "Custom"])
        with c3:
            room_size = st.selectbox("Room Size", ["Small", "Medium", "Large", "Custom Dimensions"])

        if room_size == "Custom Dimensions":
            cd1, cd2, cd3 = st.columns(3)
            with cd1:
                st.number_input("Length (ft)", min_value=5, max_value=100, value=15)
            with cd2:
                st.number_input("Width (ft)", min_value=5, max_value=100, value=12)
            with cd3:
                st.number_input("Height (ft)", min_value=7, max_value=30, value=9)
        st.markdown('</div>', unsafe_allow_html=True)

        # Section 2: Interior Style
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">2. Interior Style</div>', unsafe_allow_html=True)
        
        style_descriptions = {
            "Modern": "Clean lines, simple color palettes, sleek materials like glass and metal.",
            "Minimalist": "Ultra-clean aesthetics, essential furniture only, light monochromatic tones.",
            "Luxury": "Opulent textures, gold/brass accents, plush velvet, and high-end marble details.",
            "Scandinavian": "Warm wood tones, organic shapes, functional layouts, bright neutral backdrops.",
            "Industrial": "Exposed brick, steel beams, raw concrete, reclaimed wood, and dark metal accents.",
            "Bohemian": "Rich textures, vibrant patterns, rattan furniture, and abundant indoor foliage.",
            "Contemporary": "Fluid blend of current trends, subtle sophistication, and curved geometry.",
            "Japandi": "Harmonious union of Japanese minimalism and Scandinavian functionality.",
            "Rustic": "Natural wood logs, stone hearths, cozy earth tones, and handcrafted elements.",
            "Futuristic": "Seamless ambient LED panels, soft metallic curves, minimalist smart integration."
        }
        
        style = st.selectbox("Design Style", list(style_descriptions.keys()))
        st.info(f"**{style} Aesthetic:** {style_descriptions[style]}")
        st.markdown('</div>', unsafe_allow_html=True)

        # Section 3: Color Palette
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">3. Color Palette</div>', unsafe_allow_html=True)
        
        color_preset = st.selectbox("Preset Palette", [
            "NavBlue & Cream", "Warm Neutral", "Cool Neutral", "Earthy", 
            "Black & White", "Luxury Gold", "Pastel", "Dark Elegant", "Natural Green", "Custom"
        ])

        primary_color, secondary_color, accent_color = "#0B2545", "#FDFBF7", "#C5A059"
        if color_preset == "Custom":
            cp1, cp2, cp3 = st.columns(3)
            with cp1:
                primary_color = st.color_picker("Primary Color", "#0B2545")
            with cp2:
                secondary_color = st.color_picker("Secondary Color", "#FDFBF7")
            with cp3:
                accent_color = st.color_picker("Accent Color", "#C5A059")
        st.markdown('</div>', unsafe_allow_html=True)

        # Section 4: Furniture & Fixtures
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">4. Furniture & Elements</div>', unsafe_allow_html=True)
        
        furniture_options = [
            "Sofa", "Bed", "Wardrobe", "TV Unit", "Coffee Table", "Dining Table", 
            "Bookshelf", "Desk", "Chair", "Side Tables", "Cabinets", "Indoor Plants", 
            "Lamps", "Wall Art", "Mirrors", "Rugs"
        ]
        selected_furniture = st.multiselect(
            "Select Items", furniture_options, 
            default=["Sofa", "Coffee Table", "Indoor Plants", "Lamps", "Wall Art"]
        )

        f_col1, f_col2 = st.columns(2)
        with f_col1:
            lighting = st.selectbox("Lighting", [
                "Warm Ambient Lighting", "Natural Sun Light", "Cool Daylight", 
                "Luxury Chandelier", "Recessed LED Strips", "Soft Cinematic Lighting"
            ])
        with f_col2:
            flooring = st.selectbox("Flooring", [
                "Wooden Hardwood", "Marble Tile", "Polished Concrete", 
                "Plush Carpet", "Natural Stone", "Light Oak Vinyl"
            ])
        st.markdown('</div>', unsafe_allow_html=True)

        # Section 5: Additional Requirements
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">5. Special Instructions</div>', unsafe_allow_html=True)
        additional_reqs = st.text_area(
            "Describe your dream interior", 
            placeholder="e.g., A peaceful room with floor-to-ceiling windows, minimal navy accents, cream walls, and warm lighting..."
        )
        st.markdown('</div>', unsafe_allow_html=True)

        # Section 6: Reference Photo
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">6. Existing Room Photo (Optional)</div>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload reference photo", type=["jpg", "jpeg", "png"])
        st.markdown('</div>', unsafe_allow_html=True)

        generate_clicked = st.button("✨ Generate My Interior Design", key="gen_btn")

    with col_right:
        st.markdown('<div class="section-header">Studio Canvas</div>', unsafe_allow_html=True)

        if generate_clicked:
            pos_prompt, neg_prompt = build_design_prompt(
                room_type, room_shape, room_size, style, primary_color,
                secondary_color, accent_color, color_preset, selected_furniture,
                lighting, flooring, additional_reqs
            )

            with st.expander("🔍 View Compiled Prompt", expanded=False):
                st.code(f"POSITIVE PROMPT:\n{pos_prompt}", language="text")

            with st.spinner("AI is generating your customized interior design image..."):
                generated_image = generate_interior_design(pos_prompt)

            if generated_image:
                st.session_state["last_generated"] = {
                    "image": generated_image,
                    "room_type": room_type,
                    "style": style,
                    "color_preset": color_preset,
                    "lighting": lighting,
                    "flooring": flooring,
                    "uploaded_image": Image.open(uploaded_file) if uploaded_file else None
                }

        # Render Results Block
        if st.session_state["last_generated"] is not None:
            res = st.session_state["last_generated"]
            
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.subheader("Rendered Concept")
            
            if res["uploaded_image"] is not None:
                b_col1, b_col2 = st.columns(2)
                with b_col1:
                    st.caption("Existing Space")
                    st.image(res["uploaded_image"], use_container_width=True)
                with b_col2:
                    st.caption("AI Design Concept")
                    st.image(res["image"], use_container_width=True)
            else:
                st.image(res["image"], use_container_width=True)

            st.markdown(
                f"""
                **Design Specifications:**
                - **Type:** {res['room_type']} | **Style:** {res['style']}
                - **Palette:** {res['color_preset']}
                - **Lighting:** {res['lighting']} | **Flooring:** {res['flooring']}
                """
            )

            a_col1, a_col2, a_col3 = st.columns(3)
            
            buf = io.BytesIO()
            res["image"].save(buf, format="PNG")
            byte_im = buf.getvalue()

            with a_col1:
                st.download_button(
                    label="💾 Download",
                    data=byte_im,
                    file_name=f"{res['style']}_{res['room_type']}.png".lower().replace(" ", "_"),
                    mime="image/png"
                )
            
            with a_col2:
                if st.button("❤️ Save Gallery"):
                    st.session_state["gallery"].append(res)
                    st.success("Saved to gallery!")
            
            with a_col3:
                if st.button("🔄 Regenerate"):
                    st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.info("Configure options on the left and click 'Generate My Interior Design' to create your customized concept.")


# -----------------------------------------------------------------------------
# PAGE 3: DESIGN GALLERY
# -----------------------------------------------------------------------------
def gallery_page():
    st.markdown('<div class="section-header">Design Gallery</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#13315C; margin-bottom:20px;">Saved spatial visualizations created during your session.</p>', unsafe_allow_html=True)

    gallery = st.session_state.get("gallery", [])

    if not gallery:
        st.markdown(
            """
            <div class="glass-card" style="text-align:center; padding:40px 20px;">
                <h3 style="color:#0B2545;">Your Gallery is Currently Empty</h3>
                <p style="color:#13315C;">Generate interior concepts in the studio and save them here.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        col_g1, col_g2, col_g3 = st.columns([1, 1, 1])
        with col_g2:
            if st.button("Open AI Designer →"):
                st.session_state["current_page"] = "AI Designer"
                st.rerun()
    else:
        cols = st.columns(3)
        for idx, item in enumerate(gallery):
            with cols[idx % 3]:
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.image(item["image"], use_container_width=True)
                st.markdown(f"**{item['style']} {item['room_type']}**")
                st.caption(f"Lighting: {item['lighting']}")
                st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# PAGE 4: ABOUT
# -----------------------------------------------------------------------------
def about_page():
    st.markdown('<div class="section-header">About the Project</div>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="glass-card">
            <h3 style="color:#0B2545; font-family:'Playfair Display', serif;">AI Interior Designing</h3>
            <p style="color:#13315C; line-height:1.7;">
                <strong>AI Interior Designing</strong> translates physical room specs, color choices, and spatial preferences into realistic architectural concepts.
            </p>
            <hr style="border-color: rgba(197, 160, 89, 0.2);">
            <p style="color:#0B2545; font-weight:600; margin-bottom:2px;">Lead Developer:</p>
            <p style="color:#13315C; margin-bottom:2px;">Amna Mudassar Ali</p>
            <p style="color:#C5A059; font-weight:500;">amnamudassarali23@gmail.com</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------------------------------------------------------
# MAIN APPLICATION CONTROLLER
# -----------------------------------------------------------------------------
def main():
    apply_custom_css()
    init_session_state()

    # Left Sidebar Navigation Menu
    with st.sidebar:
        st.markdown("<h2 style='font-family:\"Playfair Display\", serif; color:#FDFBF7;'>🏛️ Navigation</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:#C5A059; font-size:0.85rem;'>NavBlue & Cream Studio</p>", unsafe_allow_html=True)
        st.markdown("---")

        # Sidebar navigation buttons
        if st.button("🏠 Home Page", key="sb_btn_home"):
            st.session_state["current_page"] = "Home"
            st.rerun()

        if st.button("🎨 AI Designer", key="sb_btn_designer"):
            st.session_state["current_page"] = "AI Designer"
            st.rerun()

        if st.button("🖼️ Design Gallery", key="sb_btn_gallery"):
            st.session_state["current_page"] = "Design Gallery"
            st.rerun()

        if st.button("ℹ️ About", key="sb_btn_about"):
            st.session_state["current_page"] = "About"
            st.rerun()

        st.markdown("---")
        st.markdown(
            """
            <div style="font-size:0.8rem; color:#E0E6ED;">
                <strong>Lead Developer:</strong><br>
                Amna Mudassar Ali<br>
                <span style="color:#C5A059;">amnamudassarali23@gmail.com</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Render selected page view
    active_page = st.session_state.get("current_page", "Home")
    if active_page == "Home":
        home_page()
    elif active_page == "AI Designer":
        designer_page()
    elif active_page == "Design Gallery":
        gallery_page()
    elif active_page == "About":
        about_page()

    st.markdown(
        """
        <div class="footer">
            AI Interior Designing | Developed by <strong>Amna Mudassar Ali</strong> (amnamudassarali23@gmail.com)
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
