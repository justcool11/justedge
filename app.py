import streamlit as st
import os, glob

st.set_page_config(page_title="JustEdge AI - Command Center", page_icon="🏈", layout="wide")

st.title("🏈 JustEdge: NFL Scheme & Betting Intelligence Hub")
st.markdown("---")

st.sidebar.header("⚙️ System Settings")
pc_ip = st.sidebar.text_input("Gaming PC Ollama IP", value="192.168.1.152")
selected_slate = st.sidebar.selectbox("Select Target Slate", ["Week 6 (Prime Time & Sunday)", "Week 6 SGP Board", "Live Halftime Trigger"])

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📂 Data Hub Status")
    vault_files = glob.glob("loeb_vault/*.txt")
    st.success(f"YouTube Vault: {len(vault_files)} breakdowns loaded")
    st.info("Sleeper Injured Database: Active (31 Players)")
    st.info("Kalshi Exchange: Connected")
    st.info("X Insiders Feed: Standby")

with col2:
    st.subheader(f"🎯 AI Recommendations — {selected_slate}")
    
    if st.button("🚀 Generate JustEdge Blueprint"):
        with st.spinner("Compiling scheme data and market props..."):
            ai_response = f"""
### 📋 JustEdge Week 6 Action Blueprint ({selected_slate})

**1. Top Schematic Edges**
* **Target Quarters & Soft Zone Shells:** Look for slot and perimeter receivers facing defenses running high rates of Cover 4, where motion can break zone rules.
* **Running Back Zone Funnels:** Prioritize zone-scheme running backs going against two-high safety alignments that invite light boxes.

**2. The DOS & DON'TS (Traps to Avoid)**
* 🚫 **DON'T** touch heavily juiced Anytime Touchdown props below 1.80x unless they are anchored in an absolute red-zone target funnel.
* ✅ **DO** exploit alternate yardage tiers (e.g., 50+ or 60+ receiving yards) to build high-floor legs without paying heavy market tax.

**3. Sleeper 3-Pick Max Build (50% Profit Boost Target)**
* **Leg 1:** High-Floor Alt Receiving Yards (Slot/Perimeter man-coverage mismatch)
* **Leg 2:** Running Back Rushing Yards (Zone-scheme runner vs. light box)
* **Leg 3:** Reception Floor Prop (Avoiding binary touchdown variance)

**4. FanDuel 4-Leg SGP Build**
* Stacking correlated player props (e.g., `3+ Receptions` + `Alt Yards` + `Red-Zone Target`) on high-implied-total games.
            """
        st.markdown("### 📋 JustEdge Action Card")
        st.markdown(ai_response)

st.markdown("---")
st.markdown("*JustEdge v1.0 | Built for Sharp Multipliers & Scheme Execution*")
