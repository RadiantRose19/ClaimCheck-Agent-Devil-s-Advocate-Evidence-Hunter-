"""
ClaimCheck Agent - Streamlit Application
An Agentic AI System for Bidirectional Evidence Investigation and Self-Correcting Claim Verification
"""

import streamlit as st
import os


def main():
    """Main Streamlit application entry point."""
    st.set_page_config(
        page_title="ClaimCheck Agent",
        page_icon="🔍",
        layout="wide"
    )
    
    st.title("🔍 ClaimCheck Agent")
    st.markdown("### An Agentic AI System for Bidirectional Evidence Investigation and Self-Correcting Claim Verification")
    
    st.markdown("---")
    
    # Project description
    st.markdown("""
    **ClaimCheck Agent** is an AI system designed to verify factual claims in documents by investigating 
    evidence from both supporting and opposing perspectives.
    
    The system extracts factual claims, retrieves evidence that supports and challenges each claim, 
    evaluates evidence quality, and produces transparent verdicts with source references.
    """)
    
    # Setup status section
    st.markdown("## 📋 Current Setup Status")
    
    status_col1, status_col2 = st.columns(2)
    
    with status_col1:
        st.markdown("### ✅ Completed")
        st.markdown("- Repository scaffold created")
        st.markdown("- Project structure initialized")
        st.markdown("- Sample test data added")
        st.markdown("- Test cases defined")
        st.markdown("- Basic dependencies configured")
    
    with status_col2:
        st.markdown("### 🔜 Planned")
        st.markdown("- Document ingestion pipeline")
        st.markdown("- Semantic evidence retrieval")
        st.markdown("- Support & Challenge Hunter agents")
        st.markdown("- Evidence Judge with verdicts")
        st.markdown("- Self-correction mechanism")
        st.markdown("- Full verification workflow")
    
    st.markdown("---")
    
    # Placeholder for future workflow
    st.markdown("## 🚀 Claim Verification Workflow")
    st.info("The claim verification engine is under development. This section will be implemented in the next milestone.")
    
    st.markdown("""
    **Coming Soon:**
    - Upload documents (PDF, TXT, DOCX)
    - Extract factual claims automatically
    - Investigate supporting and challenging evidence
    - Receive verdicts with explanations
    - View execution traces and source references
    - Export verification reports
    """)
    
    st.markdown("---")
    
    # Technology stack
    st.markdown("## 🛠️ Technology Stack")
    
    tech_stack = {
        "Python & Streamlit": "Application framework and UI",
        "Gemini API": "Claim extraction and evidence assessment",
        "PyMuPDF & python-docx": "Document parsing",
        "Sentence Transformers": "Semantic embeddings",
        "FAISS": "Vector similarity search",
        "Pydantic": "Structured data validation",
        "pytest": "Testing framework"
    }
    
    for tech, purpose in tech_stack.items():
        st.markdown(f"**{tech}**: {purpose}")
    
    st.markdown("---")
    
    # Footer
    st.markdown("""
    <div style='text-align: center; color: gray; font-size: 0.8em;'>
    ClaimCheck Agent — Investigate both sides. Verify with evidence. Explain every verdict.
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
