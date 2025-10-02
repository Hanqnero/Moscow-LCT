#!/usr/bin/env python3
"""
Tree Detection Web App - Main Entrypoint
Provides access to all detection interfaces
"""

import streamlit as st
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Tree Detection System",
    page_icon="🌲",
    layout="wide",
    initial_sidebar_state="expanded",
)


def check_models():
    """Check which models are available"""
    tree_model = Path("runs/detect/tree_detection_cpu/weights/best.pt")
    defect_model = Path("runs/defects/tree_defects_detection/weights/best.pt")
    defect_model_alt = Path("runs/defects/tree_defects_detection2/weights/best.pt")

    return {
        "tree": tree_model.exists(),
        "defect": defect_model.exists() or defect_model_alt.exists(),
        "tree_path": str(tree_model) if tree_model.exists() else None,
        "defect_path": (
            str(defect_model)
            if defect_model.exists()
            else str(defect_model_alt) if defect_model_alt.exists() else None
        ),
    }


def main():
    # Header
    st.title("🌲 Tree Detection System")
    st.markdown("### AI-powered Tree and Defect Detection")
    st.markdown("---")

    # Model status
    models = check_models()

    col1, col2 = st.columns(2)

    with col1:
        if models["tree"]:
            st.success("✅ Tree Detection Model Ready")
        else:
            st.error("❌ Tree Detection Model Not Found")
            st.info("Train with: `python train_cpu.py`")

    with col2:
        if models["defect"]:
            st.success("✅ Defect Detection Model Ready")
        else:
            st.error("❌ Defect Detection Model Not Found")
            st.info("Train with: `python train_defects.py`")

    st.markdown("---")

    # Application options
    st.header("📱 Choose an Application")

    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("🌳 Simple Tree Detection")
        st.markdown(
            """
        **Features:**
        - Detect trees in images
        - Basic tree identification
        - Fast processing
        - Single-stage detection
        
        **Best for:** Quick tree counting and basic analysis
        """
        )

        if st.button(
            "Launch Simple Detection",
            type="primary",
            use_container_width=True,
            key="simple",
        ):
            st.info("🚀 Starting Simple Tree Detection...")
            st.markdown("Run this command in terminal:")
            st.code("streamlit run inference_web.py", language="bash")
            st.markdown("Or click the link below:")
            st.markdown("[Open inference_web.py](http://localhost:8501)")

    with col_b:
        st.subheader("🔍 Two-Stage Detection")
        st.markdown(
            """
        **Features:**
        - Advanced tree detection
        - Tree type identification (bush, oak)
        - Defect detection (12 types)
        - Tree-defect association
        
        **Best for:** Detailed analysis and defect monitoring
        """
        )

        if st.button(
            "Launch Two-Stage Detection",
            type="primary",
            use_container_width=True,
            key="twostage",
        ):
            st.info("🚀 Starting Two-Stage Detection...")
            st.markdown("Run this command in terminal:")
            st.code("streamlit run two_stage_web.py", language="bash")
            st.markdown("Or click the link below:")
            st.markdown("[Open two_stage_web.py](http://localhost:8501)")

    st.markdown("---")

    # System information
    with st.expander("ℹ️ System Information", expanded=False):
        st.markdown(
            """
        ### Detection Capabilities
        
        #### Simple Tree Detection
        - **Classes:** 1 (tree)
        - **Model:** YOLOv11n
        - **Purpose:** General tree detection
        
        #### Two-Stage Detection
        - **Tree Types:** 2 (bush, oak)
        - **Defect Types:** 12 (crack, dead_bush, deadtree, dry_crone, leaned_tree, marked_tree, markedtree, markettree, rot, stem_damage, stem_rot, tree_hole)
        - **Model:** YOLOv11n (both stages)
        - **Purpose:** Detailed tree health analysis
        
        ### How to Train Models
        
        **Tree Detection Model:**
        ```bash
        python train_cpu.py
        ```
        
        **Defect Detection Model:**
        ```bash
        python train_defects.py
        ```
        
        ### Command-Line Interface
        
        You can also use the command-line tools:
        
        **Simple Detection:**
        ```bash
        python inference_simple.py <image_path>
        ```
        
        **Two-Stage Detection:**
        ```bash
        python two_stage_detection.py <image_path>
        ```
        """
        )

    # Quick start guide
    with st.expander("🚀 Quick Start Guide", expanded=False):
        st.markdown(
            """
        ### First Time Setup
        
        1. **Install Dependencies**
           ```bash
           pip install -r requirements.txt
           ```
        
        2. **Train Models** (if not already trained)
           ```bash
           python train_cpu.py          # Tree detection
           python train_defects.py      # Defect detection
           ```
        
        3. **Launch Application**
           ```bash
           streamlit run app.py         # This page
           ```
        
        ### Using the Applications
        
        1. **Choose an application** from the options above
        2. **Upload an image** using the file uploader
        3. **Adjust settings** in the sidebar (confidence thresholds, etc.)
        4. **Run detection** by clicking the "Run Detection" button
        5. **View results** and download annotated images or JSON data
        
        ### Tips
        
        - Use **Simple Detection** for quick tree counting
        - Use **Two-Stage Detection** for detailed health analysis
        - Lower confidence thresholds detect more objects (may include false positives)
        - Higher confidence thresholds are more precise (may miss some objects)
        - Defect detection works best with confidence around 0.05-0.20
        """
        )

    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666;'>"
        "🌲 Tree Detection System | Powered by YOLOv11 & Streamlit"
        "</div>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
