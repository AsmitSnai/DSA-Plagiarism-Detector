# app.py
import streamlit as st
from src.algorithms import StringMatcher
from src.preprocessor import clean_text, get_sentences
from src.fingerprint import WinnowingEngine
from src.semantic import SemanticEngine

# Ultra-premium soft, light-themed custom interface injection
st.markdown("""
<style>
    .reportview-container, .main { background-color: #F8FAFC; }
    div.stButton > button:first-child {
        background-color: #3B82F6; color: white; border-radius: 8px; border: none;
        box-shadow: 0 4px 10px rgba(59, 130, 246, 0.15); padding: 12px 28px; font-weight: 600;
    }
    div.stButton > button:hover { background-color: #2563EB; }
    .highlight-exact { background-color: #FED7AA; padding: 2px 4px; border-radius: 4px; color: #7C2D12; }
    .telemetry-card { background: white; padding: 24px; border-radius: 16px; border: 1px solid #E2E8F0; box-shadow: 0 4px 20px rgba(0,0,0,0.02); }
    .section-title { font-size: 1.1rem; font-weight: 600; color: #1E293B; margin-bottom: 12px; }
</style>
""", unsafe_allow_html=True)

st.title("🛡️ Enterprise Plagiarism Engine")
st.markdown("#### Hybrid Multi-Tier Structural & Semantic Analysis System")

col1, col2 = st.columns(2)
with col1:
    source_text = st.text_area("Original Source Document", height=200, placeholder="Insert reference material...")
with col2:
    suspect_text = st.text_area("Submitted Analysis Target", height=200, placeholder="Insert text to check content integrity...")

if st.button("Execute Multi-Tier Scan"):
    if not source_text or not suspect_text:
        st.warning("Please provide structural text inside both analysis fields.")
    else:
        with st.spinner("Processing structural analysis layers..."):
            # Step 1: Preprocessing
            c_source = clean_text(source_text)
            c_suspect = clean_text(suspect_text)
            
            # Tier 1: Exact Substring Matching Layer
            sentences = get_sentences(c_suspect)
            matched_sentences = set()
            exact_words = 0
            total_words = len(c_suspect.split()) if len(c_suspect.split()) > 0 else 1
            
            for s in sentences:
                if len(s) < 12: continue
                # Running deterministic KMP across the document structure
                if StringMatcher.kmp_search(s.lower(), c_source.lower()):
                    matched_sentences.add(s)
                    exact_words += len(s.split())
            
            exact_percentage = (exact_words / total_words) * 100
            
            # Tier 2: Structural Fingerprinting (Winnowing)
            source_fingerprints = WinnowingEngine.winnow(c_source)
            suspect_fingerprints = WinnowingEngine.winnow(c_suspect)
            
            common_hashes = source_fingerprints.intersection(suspect_fingerprints)
            fingerprint_score = (2.0 * len(common_hashes) / (len(source_fingerprints) + len(suspect_fingerprints))) * 100 if (len(source_fingerprints) + len(suspect_fingerprints)) > 0 else 0
            
            # Tier 3: Vector Semantic Vector Mapping
            semantic_score = SemanticEngine.calculate_cosine_similarity(c_source, c_suspect) * 100

            # UI Component Rendering
            st.markdown("---")
            st.markdown("### 📊 Engine Telemetry Output")
            
            m1, m2, m3 = st.columns(3)
            with m1:
                st.markdown(f"<div class='telemetry-card'><p class='section-title'>KMP Exact Match</p><h2>{exact_percentage:.1f}%</h2></div>", unsafe_allow_html=True)
            with m2:
                st.markdown(f"<div class='telemetry-card'><p class='section-title'>Winnow Fingerprint</p><h2>{fingerprint_score:.1f}%</h2></div>", unsafe_allow_html=True)
            with m3:
                st.markdown(f"<div class='telemetry-card'><p class='section-title'>Semantic Cosine</p><h2>{semantic_score:.1f}%</h2></div>", unsafe_allow_html=True)
            
            # Dynamic text highlighting delivery
            st.markdown("### 📝 Text Alignment Inspection Map")
            display_output = c_suspect
            for target in matched_sentences:
                display_output = display_output.replace(target, f"<span class='highlight-exact'>{target}</span>")
                
            st.markdown(f"<div style='background: white; padding: 24px; border-radius: 16px; border: 1px solid #E2E8F0; line-height: 1.7;'>{display_output}</div>", unsafe_allow_html=True)