"""
AI Interior Designing - Transform Your Space With Artificial Intelligence
A production-grade Streamlit web application utilizing Generative AI (SDXL) for interior design visualization.
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
    page_title="AI Interior Designing | Transform Your Space",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)


# -----------------------------------------------------------------------------
# Styling & Custom CSS (SaaS / Luxury Theme)
# -----------------------------------------------------------------------------
def apply_custom_css():
    """Injects high-end, modern typography, glassmorphism card styling, and custom UI components."""
    custom_css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
        color: #1A1A1A;
    }

    /* Background styling */
    .stApp {
        background: linear-gradient(135deg, #F8F9FA 0%, #F1F3F5 100%);
    }

    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(229, 231, 235, 0.8);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.04), 0 4px 6px -2px rgba(0, 0, 0, 0.02);
        margin-bottom: 24px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 20px 35px -10px rgba(0, 0, 0, 0.07);
    }

    /* Hero Banner */
    .hero-container {
        text-align: center;
        padding: 60px 20px 40px 20px;
        background: linear-gradient(180deg, rgba(255,255,255,0.9) 0%, rgba(248,249,250,0) 100%);
        border-radius: 24px;
        margin-bottom: 30px;
    }

    .hero-title {
        font-size: 3.2rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        background: linear-gradient(135deg, #111827 0%, #4B5563 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 12px;
    }

    .hero-subtitle {
        font-size: 1.25rem;
        color: #4B5563;
        font-weight: 400;
        max-width: 680px;
        margin: 0 auto 28px auto;
        line-height: 1.6;
    }

    /* Primary Action Buttons */
    .stButton>button {
        background: #111827 !important;
        color: #FFFFFF !important;
        border-radius: 12px !important;
        padding: 12px 28px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        border: none !important;
        box-shadow: 0 4px 14px 0 rgba(0,0,0,0.15) !important;
        transition: all 0.25s ease !important;
        width: 100%;
    }

    .stButton>button:hover {
        background: #374151 !important;
        box-shadow: 0 6px 20px 0 rgba(0,0,0,0.2) !important;
        transform: translateY(-1px);
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E5E7EB;
    }

    /* Section Headings */
    .section-header {
        font-size: 1.35rem;
        font-weight: 700;
        color: #111827;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Badges & Tags */
    .feature-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        background: #F3F4F6;
        color: #374151;
        margin-bottom: 12px;
    }

    /* Custom Footer */
    .footer {
        text-align: center;
        padding: 30px 0 10px 0;
        font-size: 0.85rem;
        color: #9CA3AF;
        border-top: 1px solid #E5E7EB;
        margin-top: 50px;
    }

    /* Hide Streamlit default branding elements */
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
    if "current_page" not in st.mutable_session_state:
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
    
    # Palette definition
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
        time.sleep(2.5)  # Simulate diffusion steps
        # Create a placeholder canvas simulating an interior visualization
        placeholder_img = Image.new("RGB", (1024, 1024), color=(240, 238, 233))
        return placeholder_img

    try:
        # Run local GPU pipeline
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
# PAGE 1: HOME
# -----------------------------------------------------------------------------
def home_page():
    # Hero Section
    st.markdown(
        """
        <div class="hero-container">
            <span class="feature-badge">Powered by Generative AI</span>
            <div class="hero-title">AI Interior Designing</div>
            <div class="hero-subtitle">Transform your space with artificial intelligence. Visualize beautiful interior designs personalized to your room, style, colors, and preferences.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col_btn1, col_btn2, col_btn3 = st.columns([1, 1.2, 1])
    with col_btn2:
        if st.button("Start Designing →", key="hero_cta"):
            st.session_state["current_page"] = "AI Designer"
            st.rerun()

    st.markdown("<br><hr><br>", unsafe_allow_html=True)

    # Features Grid
    f1, f2, f3, f4 = st.columns(4)
    with f1:
        st.markdown(
            """
            <div class="glass-card">
                <h3>⚡ AI-Powered</h3>
                <p style="color:#6B7280; font-size:0.9rem;">Generate unique, studio-grade interior concepts in seconds using diffusion models.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with f2:
        st.markdown(
            """
            <div class="glass-card">
                <h3>🎯 Personalized</h3>
                <p style="color:#6B7280; font-size:0.9rem;">Tailor room dimensions, layout shape, lighting, exact hex colors, and furniture selections.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with f3:
        st.markdown(
            """
            <div class="glass-card">
                <h3>👁️ Instant Visuals</h3>
                <p style="color:#6B7280; font-size:0.9rem;">Evaluate photorealistic visual iterations before purchasing materials or hiring architects.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with f4:
        st.markdown(
            """
            <div class="glass-card">
                <h3>🎨 10+ Styles</h3>
                <p style="color:#6B7280; font-size:0.9rem;">Explore Modern, Japandi, Scandinavian, Luxury, Industrial, Minimalist, and more.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # How It Works
    st.markdown('<div class="section-header">How It Works</div>', unsafe_allow_html=True)
    hw1, hw2, hw3 = st.columns(3)
    with hw1:
        st.markdown(
            """
            <div class="glass-card">
                <h4 style="color:#111827;">1. Configure Room Parameters</h4>
                <p style="color:#6B7280; font-size:0.88rem;">Select your room type, physical layout, dimensions, and optional reference photograph.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with hw2:
        st.markdown(
            """
            <div class="glass-card">
                <h4 style="color:#111827;">2. Define Design Aesthetic</h4>
                <p style="color:#6B7280; font-size:0.88rem;">Choose your preferred architectural style, furniture set, lighting fixtures, and color palettes.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with hw3:
        st.markdown(
            """
            <div class="glass-card">
                <h4 style="color:#111827;">3. Generate & Refine</h4>
                <p style="color:#6B7280; font-size:0.88rem;">Synthesize ultra-high resolution concepts, compare before/after layouts, and export your portfolio.</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# -----------------------------------------------------------------------------
# PAGE 2: AI DESIGNER
# -----------------------------------------------------------------------------
def designer_page():
    st.markdown('<div class="hero-title" style="font-size:2.2rem;">AI Interior Designer</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#6B7280; margin-bottom:24px;">Specify your architectural parameters to synthesize personalized interior concepts.</p>', unsafe_allow_html=True)

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
            "Warm Neutral", "Cool Neutral", "Earthy", "Black & White", 
            "Luxury Gold", "Pastel", "Dark Elegant", "Natural Green", "Custom"
        ])

        primary_color, secondary_color, accent_color = "#E5E0D8", "#4A3B32", "#C5A059"
        if color_preset == "Custom":
            cp1, cp2, cp3 = st.columns(3)
            with cp1:
                primary_color = st.color_picker("Primary Color", "#E5E0D8")
            with cp2:
                secondary_color = st.color_picker("Secondary Color", "#4A3B32")
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
            placeholder="e.g., Create a peaceful room with floor-to-ceiling windows overlooking a pine forest, minimalist artwork, beige textiles..."
        )
        st.markdown('</div>', unsafe_allow_html=True)

        # Optional Image Upload
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">6. Existing Room Photograph (Optional)</div>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload reference photo", type=["jpg", "jpeg", "png"])
        
        # Developer Note regarding Image-to-Image / ControlNet integration
        st.caption(
            "*Note for Engineers: Uploaded photographs can be processed via Stable Diffusion ControlNet "
            "(MLSD / Depth Estimation pipeline) to preserve structural wall geometry while redesigning interior elements.*"
        )
        st.markdown('</div>', unsafe_allow_html=True)

        # Generate Button Action
        generate_clicked = st.button("✨ Generate My Interior Design", key="gen_btn")

    with col_right:
        st.markdown('<div class="section-header">Design Studio Preview</div>', unsafe_allow_html=True)

        if generate_clicked:
            # Build prompts
            pos_prompt, neg_prompt = build_design_prompt(
                room_type, room_shape, room_size, style, primary_color,
                secondary_color, accent_color, color_preset, selected_furniture,
                lighting, flooring, additional_reqs
            )

            with st.expander("🔍 View Compiled Prompt Details", expanded=False):
                st.code(f"POSITIVE PROMPT:\n{pos_prompt}\n\nNEGATIVE PROMPT:\n{neg_prompt}", language="text")

            with st.spinner("AI is designing your dream interior..."):
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
            st.subheader("Your AI Interior Concept")
            
            # Display Before / After if upload exists
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

            # Metadata display
            st.markdown(
                f"""
                **Specs Summary:**
                - **Type:** {res['room_type']} | **Style:** {res['style']}
                - **Palette:** {res['color_preset']}
                - **Lighting:** {res['lighting']} | **Flooring:** {res['flooring']}
                """
            )

            # Action Buttons
            a_col1, a_col2, a_col3 = st.columns(3)
            
            # Download prep
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
            st.info("Configure settings on the left panel and click 'Generate My Interior Design' to render your visualization.")


# -----------------------------------------------------------------------------
# PAGE 3: DESIGN GALLERY
# -----------------------------------------------------------------------------
def gallery_page():
    st.markdown('<div class="hero-title" style="font-size:2.2rem;">Design Gallery</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#6B7280; margin-bottom:24px;">Browse interior design concepts rendered during your current session.</p>', unsafe_allow_html=True)

    gallery = st.session_state.get("gallery", [])

    if not gallery:
        st.markdown(
            """
            <div class="glass-card" style="text-align:center; padding:60px 20px;">
                <h3>Your design gallery is empty</h3>
                <p style="color:#6B7280;">Start generating interior concepts in the studio to populate your portfolio.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        col_g1, col_g2, col_g3 = st.columns([1, 1, 1])
        with col_g2:
            if st.button("Go to AI Designer →"):
                st.session_state["current_page"] = "AI Designer"
                st.rerun()
    else:
        # Display gallery items in 3-column grid
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
    st.markdown('<div class="hero-title" style="font-size:2.2rem;">About AI Interior Designing</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="glass-card">
            <h3>Vision & Concept</h3>
            <p style="color:#4B5563; line-height:1.7;">
                AI Interior Designing is an intelligent conceptualization assistant engineered to democratize architectural 
                visualization. By combining state-of-the-art latent diffusion models with structured architectural parameters, 
                our platform enables property owners, interior designers, and architects to explore potential aesthetics in seconds.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    a1, a2 = st.columns(2)
    with a1:
        st.markdown(
            """
            <div class="glass-card">
                <h3>Technical Architecture</h3>
                <ul style="color:#4B5563; line-height:1.8;">
                    <li><strong>Interface:</strong> Streamlit with custom SaaS CSS glassmorphism.</li>
                    <li><strong>Generative Model:</strong> Stable Diffusion XL Base 1.0 (Diffusers).</li>
                    <li><strong>Engine:</strong> PyTorch with dynamic FP16 CUDA acceleration.</li>
                    <li><strong>Image Processing:</strong> Pillow (PIL).</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
    with a2:
        st.markdown(
            """
            <div class="glass-card">
                <h3>Future Roadmap</h3>
                <ul style="color:#4B5563; line-height:1.8;">
                    <li>ControlNet depth mapping for precise room boundary enforcement.</li>
                    <li>Automated furniture catalog lookup and localized price estimation.</li>
                    <li>Multi-angle 3D spatial reconstruction.</li>
                    <li>Interactive AI chat assistant for real-time style tweaking.</li>
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
        st.markdown("## 🏛️ AI Interior")
        st.markdown("*Transform Your Space With AI*")
        st.markdown("---")

        nav_selection = st.radio(
            "Navigation",
            ["Home", "AI Designer", "Design Gallery", "About"],
            index=["Home", "AI Designer", "Design Gallery", "About"].index(st.session_state["current_page"])
        )

        st.session_state["current_page"] = nav_selection

        st.markdown("---")
        st.caption("System Status: **Online**")
        st.caption(f"Accelerator: **{'CUDA GPU' if torch.cuda.is_available() else 'CPU Mode'}**")

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
            AI Interior Designing | Powered by Python, Streamlit & Generative AI
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
