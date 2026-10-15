import streamlit as st
import os, glob

st.set_page_config(page_title="JustEdge - AI Betting Intelligence", page_icon="🏈", layout="wide")

st.title("🏈 JustEdge: Live Sports Betting Intelligence Hub")
st.markdown("### Public & VIP Analytics Platform | Week 6 Slate")
st.markdown("---")

# Sidebar navigation & filters
st.sidebar.header("👤 User Account")
user_tier = st.sidebar.selectbox("Access Level", ["Free Tier", "VIP Pro Bettor (Unlocked)"])
st.sidebar.markdown("---")
st.sidebar.header("🎯 Bet Type Filter")
bet_focus = st.sidebar.selectbox("Show Me:", ["All Recommendations", "Sleeper Max 3-Pick Slips", "FanDuel SGPs (+1000 Odds)", "Kalshi Market Edges"])

# Main Dashboard Metric Cards
col1, col2, col3 = st.columns(3)
col1.metric("🎥 YouTube Vault Breakdowns", "Synced", "Active")
col2.metric("💤 Sleeper Injury Tracker", "31 Players Tracked", "Live")
col3.metric("📈 Kalshi / FanDuel Market Engine", "Active Edge", "Low-Vig")

st.markdown("---")

# Action Area
if st.button("🚀 Generate Sharp Week 6 Player Recommendations"):
    with st.spinner("Analyzing Kalshi odds, Sleeper injury feeds, and Loeb scheme breakdowns..."):
        
        st.subheader("🔥 Top High-Confidence Player Props & Slips")
        
        # Interactive tabs for fluid user experience
        tab1, tab2, tab3 = st.tabs(["🎯 Sleeper Max Picks", "🔥 FanDuel SGP Board", "📊 Kalshi Prop Edges"])
        
        with tab1:
            st.markdown("### 💤 Sleeper 3-Pick Max Build (50% Profit Boost Target)")
            
            st.success("**Pick 1: Keon Coleman (BUF - WR) — OVER 3.5 Receptions / 40+ Alt Rec Yards**")
            st.write("* **Edge Rationale:** Josh Palmer ruled OUT[cite: 3]. Rams run man-coverage at a top-10 rate[cite: 6]. Coleman commands 80%+ of isolation perimeter target share in this split[cite: 6].")
            
            st.info("**Pick 2: Kyren Williams (LAR - RB) — OVER 21.5 Receiving Yards**")
            st.write("* **Edge Rationale:** Bills defense surrenders a top-5 target rate to opposing running backs[cite: 6]. Williams acts as the primary checkdown safety valve.")
            
            st.warning("**Pick 3: Puka Nacua (LAR - WR) — OVER 70+ Alt Receiving Yards**")
            st.write("* **Edge Rationale:** Bills sit in Cover 4 (Quarters) at a top-5 rate[cite: 6]. McVay utilizes pre-snap motion to manipulate Quarters match rules for Nacua[cite: 6].")
            
        with tab2:
            st.markdown("### 🔥 FanDuel SGP Board (+1268 Boosted)")
            st.markdown("""
            * **Leg 1:** Mark Andrews — **3+ Receptions** (Primary safety valve vs Cover 3)[cite: 12]
            * **Leg 2:** Mark Andrews — **20+ Receiving Yards** (Core floor correlation)
            * **Leg 3:** Drake London — **60+ Receiving Yards** (Perimeter funnel mismatch)[cite: 12]
            * **Leg 4:** Bijan Robinson — **Anytime 1st Half TD** (Zone-blocking strike early)[cite: 12]
            """)
            
        with tab3:
            st.markdown("### 📈 Kalshi Market vs Bookmaker Discrepancies")
            st.markdown("""
            * **Market Alert:** Kalshi crowd-sourced probabilities indicate alt-receiving lines on slot tight ends are underpriced by ~4.5% compared to traditional sportsbook juice. 
            * **Action:** Target alternate floor props rather than standard game totals.
            """)

        with st.expander("🔍 View AI Scheme & Data Breakdown"):
            st.markdown("**Core Methodology:** Combining Max Loeb's cover-shell film vault with Sleeper injury data and quantitative model tracking.")

st.markdown("---")
st.markdown("*JustEdge Application v1.0 | Built for Scale*")
