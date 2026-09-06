"""
AI Interior Designing - Transform Your Space With Artificial Intelligence
Developer: Amna Mudassar Ali (amnamudassarali23@gmail.com)
A SaaS-grade Streamlit web application utilizing Generative AI for interior design visualization.
"""

import os
import io
import time
import base64
from typing import Tuple, Dict, Any, Optional

import streamlit as st
from PIL import Image
import torch

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

    /* Color Variables: NavBlue (#0B2545), Cream (#FDFBF7), Accent Gold (#C5A059), Soft Slate (#13315C) */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #0B2545;
    }

    /* Overall App Background in Soft Warm Cream */
    .stApp {
        background-color: #FDFBF7;
    }

    /* Specialized Designing Background for Home Hero Banner */
    .design-hero-bg {
        position: relative;
        background: linear-gradient(135deg, rgba(11, 37, 69, 0.95) 0%, rgba(19, 49, 92, 0.92) 100%),
                    radial-gradient(circle at 50% 50%, rgba(197, 160, 89, 0.15) 0%, transparent 60%);
        background-size: cover;
        border-radius: 24px;
        padding: 80px 40px;
        text-align: center;
        color: #FDFBF7;
        box-shadow: 0 20px 40px rgba(11, 37, 69, 0.15);
        border: 1px solid rgba(197, 160, 89, 0.3);
        margin-bottom: 30px;
        overflow: hidden;
    }

    .design-hero-bg::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background-image: repeating-linear-gradient(0deg, transparent, transparent 49px, rgba(253, 251, 247, 0.04) 50px),
                          repeating-linear-gradient(90deg, transparent, transparent 49px, rgba(253, 251, 247, 0.04) 50px);
        pointer-events: none;
    }

    /* Typography */
    .brand-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.8rem;
        font-weight: 700;
        letter-spacing: -0.02em;
        color: #FDFBF7;
        margin-bottom: 10px;
        text-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }

    .developer-card {
        display: inline-block;
        background: rgba(253, 251, 247, 0.12);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(197, 160, 89, 0.4);
        padding: 16px 32px;
        border-radius: 50px;
        margin-top: 20px;
        margin-bottom: 30px;
    }

    .developer-name {
        font-size: 1.25rem;
        font-weight: 600;
        color: #EEF4F8;
        letter-spacing: 0.03em;
    }

    .developer-email {
        font-size: 0.95rem;
        color: #C5A059;
        font-weight: 500;
    }

    /* Glassmorphism Cards in NavBlue/Cream context */
    .glass-card {
        background: #FFFFFF;
        border: 1px solid #EEF2F6;
        border-radius: 18px;
        padding: 26px;
        box-shadow: 0 10px 25px -5px rgba(11, 37, 69, 0.05);
        margin-bottom: 24px;
        transition: transform 0.25s ease, box-shadow 0.25s ease;
    }

    .glass-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 30px -5px rgba(11, 37, 69, 0.1);
        border-color: #C5A059;
    }

    /* NavBlue Primary Action Buttons */
    .stButton>button {
        background: #0B2545 !important;
        color: #FDFBF7 !important;
        border-radius: 12px !important;
        padding: 14px 28px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        border: 1px solid #0B2545 !important;
        box-shadow: 0 4px 14px 0 rgba(11, 37, 69, 0.2) !important;
        transition: all 0.25s ease !important;
        width: 100%;
    }

    .stButton>button:hover {
        background: #13315C !important;
        border-color: #C5A059 !important;
        color: #C5A059 !important;
        box-shadow: 0 6px 20px 0 rgba(11, 37, 69, 0.3) !important;
        transform: translateY(-2px);
    }

    /* Sidebar Styling - Deep NavBlue */
    section[data-testid="stSidebar"] {
        background-color: #0B2545 !important;
    }

    section[data-testid="stSidebar"] * {
        color: #FDFBF7 !important;
    }

    section[data-testid="stSidebar"] .stRadio > label {
        color: #C5A059 !important;
    }

    /* Form Controls & Inputs Styling */
    .stSelectbox label, .stMultiSelect label, .stColorPicker label, .stTextArea label, .stNumberInput label {
        color: #0B2545 !important;
        font-weight: 600 !important;
    }

    /* Section Headings */
    .section-header {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: #0B2545;
        margin-bottom: 18px;
        border-bottom: 2px solid #C5A059;
        padding-bottom: 6px;
        display: inline-block;
    }

    /* Custom Badges */
    .theme-badge {
        display: inline-block;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 700;
        background: #13315C;
        color: #C5A059;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 16px;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 30px 0 15px 0;
        font-size: 0.88rem;
        color: #13315C;
        border-top: 1px solid rgba(197, 160, 89, 0.3);
        margin-top: 60px;
    }

    /* Hide Default Streamlit Chrome */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
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
# ML Model Pipeline Management (Lazy Loading & Caching)
# -----------------------------------------------------------------------------
@st.cache_resource(show_spinner=False)
def load_sdxl_pipeline():
    """Loads and caches the Stable Diffusion XL pipeline using torch best practices."""
    try:
        from diffusers import StableDiffusionXLPipeline, EulerDiscreteScheduler

        model_id = "stabilityai/stable-diffusion-xl-base-1.0"
        
        device = "cuda" if torch.cuda.is_available() else "cpu"
        torch_dtype = torch.float16 if device == "cuda" else torch.float32

        pipe = StableDiffusionXLPipeline.from_pretrained(
            model_id,
            torch_dtype=torch_dtype,
            use_safetensors=True,
            variant="fp16" if device == "cuda" else None
        )
        pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config)
        pipe.to(device)

        if device == "cuda":
            pipe.enable_attention_slicing()

        return pipe, device, None
    except Exception as e:
        return None, "cpu", str(e)


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
        color_description = f"{color_preset.lower()} color scheme"
    else:
        color_description = f"palette featuring primary {primary_color}, secondary {secondary_color}, and accent {accent_color}"

    furniture_str = ", ".join(furniture) if furniture else "balanced essential furniture"

    # Positive Prompt
    positive_prompt = (
        f"A photorealistic, award-winning architectural interior design photograph of a {room_size.lower()} {room_shape.lower()} {room_type.lower()}. "
        f"Design Style: {style}. Color Palette: {color_description}. "
        f"Included Furniture & Decor: {furniture_str}. Flooring: {flooring} flooring. "
        f"Lighting: {lighting}. "
    )

    if additional_reqs.strip():
        positive_prompt += f"Specific Details: {additional_reqs.strip()}. "

    positive_prompt += (
        "Architectural Digest style, 8k resolution, highly detailed materials, natural sunlight, depth of field, "
        "flawless visual symmetry, volumetric lighting, interior design portfolio photograph."
    )

    # Negative Prompt
    negative_prompt = (
        "blurry, low resolution, distorted geometry, warped furniture, unrealistic architecture, "
        "duplicate objects, oversaturated, text, watermark, logo, signature, ugly layout, human figures, "
        "cluttered, noise, CGI artifact, bad shadows, missing limbs, draft render."
    )

    return positive_prompt, negative_prompt


# -----------------------------------------------------------------------------
# Image Generation Pipeline Manager
# -----------------------------------------------------------------------------
def generate_interior_design(prompt: str, negative_prompt: str) -> Optional[Image.Image]:
    """Handles execution of the text-to-image diffusion model with graceful fallback mechanisms."""
    pipe, device, err = load_sdxl_pipeline()

    if pipe is None:
        st.warning(f"Local GPU/Model loading unavailable ({err}). Executing simulated render mode for demonstration.")
        time.sleep(2.5)
        placeholder_img = Image.new("RGB", (1024, 1024), color=(253, 251, 247))
        return placeholder_img

    try:
        with torch.inference_mode():
            result = pipe(
                prompt=prompt,
                negative_prompt=negative_prompt,
                num_inference_steps=30 if device == "cuda" else 15,
                guidance_scale=7.5,
                width=1024,
                height=1024
            )
        return result.images[0]
    except Exception as e:
        st.error(f"An error occurred during image generation: {str(e)}")
        return None


# -----------------------------------------------------------------------------
# PAGE 1: HOME (Focused Landing Page with Project & Developer Info)
# -----------------------------------------------------------------------------
def home_page():
    st.markdown(
        """
        <div class="design-hero-bg">
            <span class="theme-badge">Architectural AI Platform</span>
            <div class="brand-title">AI Interior Designing</div>
            <p style="font-size:1.25rem; color:#E0E6ED; max-width:700px; margin:0 auto 20px auto; font-weight:300;">
                Transforming spatial concepts into photorealistic interior visualizations through generative artificial intelligence.
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

    # Architectural Design Feature Cards
    f1, f2, f3 = st.columns(3)
    with f1:
        st.markdown(
            """
            <div class="glass-card">
                <h3 style="color:#0B2545; font-family:'Playfair Display', serif;">✨ Intelligent Synthesis</h3>
                <p style="color:#13315C; font-size:0.9rem;">Generate bespoke spatial concepts using tailored architectural diffusion pipelines.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with f2:
        st.markdown(
            """
            <div class="glass-card">
                <h3 style="color:#0B2545; font-family:'Playfair Display', serif;">📐 Spatial Precision</h3>
                <p style="color:#13315C; font-size:0.9rem;">Specify dimensions, furniture arrays, custom lighting setups, and exact color palettes.</p>
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
    st.markdown('<p style="color:#13315C; margin-bottom:24px;">Configure structural specs, materials, colors, and lighting parameters below.</p>', unsafe_allow_html=True)

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

        # Section 2: Architectural Style
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

        # Section 3: Color Palette & Preferences
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
        st.markdown('<div class="section-header">4. Furniture & Structural Elements</div>', unsafe_allow_html=True)
        
        furniture_options = [
            "Sofa", "Bed", "Wardrobe", "TV Unit", "Coffee Table", "Dining Table", 
            "Bookshelf", "Desk", "Chair", "Side Tables", "Cabinets", "Indoor Plants", 
            "Lamps", "Wall Art", "Mirrors", "Rugs"
        ]
        selected_furniture = st.multiselect(
            "Select Desired Items", furniture_options, 
            default=["Sofa", "Coffee Table", "Indoor Plants", "Lamps", "Wall Art"]
        )

        f_col1, f_col2 = st.columns(2)
        with f_col1:
            lighting = st.selectbox("Lighting Preference", [
                "Warm Ambient Lighting", "Natural Sun Light", "Cool Daylight", 
                "Luxury Chandelier", "Recessed LED Strips", "Soft Cinematic Lighting"
            ])
        with f_col2:
            flooring = st.selectbox("Flooring Option", [
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

        # Section 6: Optional Reference Photo
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">6. Existing Room Photograph (Optional)</div>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload reference photo", type=["jpg", "jpeg", "png"])
        st.markdown('</div>', unsafe_allow_html=True)

        # Action Button
        generate_clicked = st.button("✨ Generate My Interior Design", key="gen_btn")

    with col_right:
        st.markdown('<div class="section-header">Studio Canvas</div>', unsafe_allow_html=True)

        if generate_clicked:
            pos_prompt, neg_prompt = build_design_prompt(
                room_type, room_shape, room_size, style, primary_color,
                secondary_color, accent_color, color_preset, selected_furniture,
                lighting, flooring, additional_reqs
            )

            with st.expander("🔍 View Compiled Prompt Details", expanded=False):
                st.code(f"POSITIVE PROMPT:\n{pos_prompt}\n\nNEGATIVE PROMPT:\n{neg_prompt}", language="text")

            with st.spinner("AI is generating your interior concept..."):
                generated_image = generate_interior_design(pos_prompt, neg_prompt)

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
            st.subheader("Rendered Interior Concept")
            
            if res["uploaded_image"] is not None:
                b_col1, b_col2 = st.columns(2)
                with b_col1:
                    st.caption("Existing Space")
                    st.image(res["uploaded_image"], use_column_width=True)
                with b_col2:
                    st.caption("AI Concept")
                    st.image(res["image"], use_column_width=True)
            else:
                st.image(res["image"], use_column_width=True)

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
            st.info("Configure your preferences on the left and click 'Generate My Interior Design' to view the concept.")


# -----------------------------------------------------------------------------
# PAGE 3: DESIGN GALLERY
# -----------------------------------------------------------------------------
def gallery_page():
    st.markdown('<div class="section-header">Design Gallery</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#13315C; margin-bottom:24px;">Saved spatial visualizations created during your session.</p>', unsafe_allow_html=True)

    gallery = st.session_state.get("gallery", [])

    if not gallery:
        st.markdown(
            """
            <div class="glass-card" style="text-align:center; padding:50px 20px;">
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
                st.image(item["image"], use_column_width=True)
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
                <strong>AI Interior Designing</strong> is an architectural visualization platform designed to convert precise spatial 
                inputs, palette preferences, and lighting requirements into photorealistic interior images.
            </p>
            <hr style="border-color: rgba(197, 160, 89, 0.2);">
            <p style="color:#0B2545; font-weight:600; margin-bottom:4px;">Lead Developer:</p>
            <p style="color:#13315C; margin-bottom:2px;">Amna Mudassar Ali</p>
            <p style="color:#C5A059; font-weight:500;">amnamudassarali23@gmail.com</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    a1, a2 = st.columns(2)
    with a1:
        st.markdown(
            """
            <div class="glass-card">
                <h3 style="color:#0B2545; font-family:'Playfair Display', serif;">Technical Stack</h3>
                <ul style="color:#13315C; line-height:1.8;">
                    <li><strong>Framework:</strong> Streamlit (Custom NavBlue & Cream Theme)</li>
                    <li><strong>AI Engine:</strong> Stable Diffusion XL Base 1.0 (Hugging Face Diffusers)</li>
                    <li><strong>Processing:</strong> PyTorch (CUDA Dynamic Float16 Acceleration)</li>
                    <li><strong>Graphics:</strong> Pillow (PIL)</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
    with a2:
        st.markdown(
            """
            <div class="glass-card">
                <h3 style="color:#0B2545; font-family:'Playfair Display', serif;">Future Architecture Roadmap</h3>
                <ul style="color:#13315C; line-height:1.8;">
                    <li>ControlNet line/depth mapping integration.</li>
                    <li>Object segmentation for real-time furniture replacements.</li>
                    <li>Automated interior material cost estimations.</li>
                </ul>
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

    # Sidebar Navigation
    with st.sidebar:
        st.markdown("<h2 style='font-family:\"Playfair Display\", serif; color:#FDFBF7;'>🏛️ AI Interior</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:#C5A059; font-size:0.85rem;'>NavBlue & Cream Studio Edition</p>", unsafe_allow_html=True)
        st.markdown("---")

        nav_selection = st.radio(
            "Navigation",
            ["Home", "AI Designer", "Design Gallery", "About"],
            index=["Home", "AI Designer", "Design Gallery", "About"].index(st.session_state["current_page"])
        )

        st.session_state["current_page"] = nav_selection

        st.markdown("---")
        st.markdown("<p style='font-size:0.8rem; color:#E0E6ED;'>Developer:<br><strong>Amna Mudassar Ali</strong><br><span style='color:#C5A059;'>amnamudassarali23@gmail.com</span></p>", unsafe_allow_html=True)

    # Route Page Display
    if st.session_state["current_page"] == "Home":
        home_page()
    elif st.session_state["current_page"] == "AI Designer":
        designer_page()
    elif st.session_state["current_page"] == "Design Gallery":
        gallery_page()
    elif st.session_state["current_page"] == "About":
        about_page()

    # Footer
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
