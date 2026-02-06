import streamlit as st
from chimera.orchestrator import run_pipeline

st.title("🧠 Project Chimera — Dashboard")

st.markdown("Governed autonomous influencer pipeline demo.")

if st.button("Run Chimera Pipeline"):
    result = run_pipeline()
    st.success("Pipeline Completed Successfully!")
    st.json(result)
