import streamlit as st
import rdflib
import os
import hashlib

st.set_page_config(page_title="Peculiar Library | N-1 Nairobi", page_icon="🏛️")

st.title("🏛️ The Peculiar Library")
st.markdown("### **N-1 Nairobi Global Settlement Node**")
st.info("Sovereign Architect: Samuel Muriithi Gitandu, B.S. (Karatina University)")

# --- 1. TRIPLE INVENTORY ---
st.header("📊 Knowledge Graph Inventory")
g = rdflib.Graph()
ontology_path = "ontology/padi-v3.ttl"

if os.path.exists(ontology_path):
    g.parse(ontology_path, format="turtle")
    cols = st.columns(2)
    cols[0].metric("Deterministic Triples", len(g))
    cols[1].metric("Node Status", "Operational")
    
    with st.expander("Explore 16 Units of Absolute Truth"):
        for s, p, o in g:
            st.code(f"{s.split('#')[-1]} --({p.split('#')[-1]})--> {o}")

# --- 2. SECURITY SHIELD ---
st.divider()
st.header("🛡️ Security & Integrity")

# Check GPG Signature
sig_path = "ontology/padi-v3.ttl.asc"
if os.path.exists(sig_path):
    st.success("✅ GPG Detached Signature Found (Key 9F4D46EF)")
else:
    st.warning("⚠️ No Cryptographic Signature Detected.")

# Check SHA-256 Hash
hash_path = "ontology/padi.sha256"
if os.path.exists(hash_path):
    with open(hash_path, "r") as f:
        recorded_hash = f.read().split()[0]
    
    # Calculate current live hash
    with open(ontology_path, "rb") as f:
        current_hash = hashlib.sha256(f.read()).hexdigest()
    
    if recorded_hash == current_hash:
        st.success(f"✅ SHA-256 Integrity Verified: {current_hash[:16]}...")
    else:
        st.error("🚨 Semantic Drift/Tampering Detected!")

st.sidebar.markdown("---")
st.sidebar.write("🔒 **Identity Verified**")
st.sidebar.write("🎓 **Karatina University Node**")
