"""
AI Hub for Cyber Security — Live Status Dashboard
--------------------------------------------------
A Streamlit single-page app featuring:
  1. A real-time, second-accurate clock
  2. Live CPU and RAM usage monitors
  3. An English teaser section announcing the upcoming AI Hub for Cyber Security
  4. An animated, AI-themed background (circuit / neural-network style, pure CSS+SVG,
     no external image downloads required)

Run with:
    streamlit run app.py
"""

import datetime

import psutil
import streamlit as st
from streamlit_autorefresh import st_autorefresh

# ----------------------------------------------------------------------------
# Page configuration
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="AI Hub | Cyber Security",
    page_icon="🛡️",
    layout="wide",
)

# Auto-refresh the whole app every 1000 ms so the clock / CPU / RAM stay live
st_autorefresh(interval=1000, key="live_refresh")

# ----------------------------------------------------------------------------
# Background + global styling
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    /* ---------- Animated AI / circuit-board background ---------- */
    .stApp {
        background:
            radial-gradient(circle at 20% 20%, rgba(0, 255, 200, 0.08), transparent 40%),
            radial-gradient(circle at 80% 30%, rgba(0, 150, 255, 0.10), transparent 45%),
            radial-gradient(circle at 50% 80%, rgba(120, 0, 255, 0.10), transparent 45%),
            repeating-linear-gradient(
                0deg,
                rgba(0, 255, 200, 0.05) 0px,
                rgba(0, 255, 200, 0.05) 1px,
                transparent 1px,
                transparent 40px
            ),
            repeating-linear-gradient(
                90deg,
                rgba(0, 255, 200, 0.05) 0px,
                rgba(0, 255, 200, 0.05) 1px,
                transparent 1px,
                transparent 40px
            ),
            linear-gradient(135deg, #050810 0%, #0a1128 45%, #050810 100%);
        background-size: 200% 200%, 200% 200%, 200% 200%, 40px 40px, 40px 40px, 200% 200%;
        animation: aiFlow 18s ease-in-out infinite;
        color: #e6f1ff;
    }

    @keyframes aiFlow {
        0%   { background-position: 0% 0%, 100% 0%, 50% 100%, 0 0, 0 0, 0% 0%; }
        50%  { background-position: 100% 100%, 0% 100%, 50% 0%, 40px 40px, 40px 40px, 100% 100%; }
        100% { background-position: 0% 0%, 100% 0%, 50% 100%, 0 0, 0 0, 0% 0%; }
    }

    /* ---------- Glass-card style panels ---------- */
    .ai-card {
        background: rgba(10, 20, 40, 0.55);
        border: 1px solid rgba(0, 255, 200, 0.25);
        border-radius: 16px;
        padding: 1.4rem 1.6rem;
        backdrop-filter: blur(6px);
        box-shadow: 0 0 25px rgba(0, 255, 200, 0.08);
        margin-bottom: 1rem;
    }

    .clock-text {
        font-family: 'Courier New', monospace;
        font-size: 3.4rem;
        font-weight: 700;
        letter-spacing: 4px;
        color: #00ffc8;
        text-shadow: 0 0 12px rgba(0, 255, 200, 0.55), 0 0 30px rgba(0, 255, 200, 0.25);
        margin: 0;
    }

    .date-text {
        font-family: 'Courier New', monospace;
        font-size: 1.1rem;
        color: #8fd9ff;
        letter-spacing: 2px;
        margin-top: -0.3rem;
    }

    .badge-pulse {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #00ffc8;
        box-shadow: 0 0 8px #00ffc8;
        margin-right: 8px;
        animation: pulse 1.4s ease-in-out infinite;
    }

    @keyframes pulse {
        0%   { transform: scale(1);   opacity: 1;   }
        50%  { transform: scale(1.6); opacity: 0.4; }
        100% { transform: scale(1);   opacity: 1;   }
    }

    .hub-title {
        font-size: 2.1rem;
        font-weight: 800;
        background: linear-gradient(90deg, #00ffc8, #4da8ff, #b967ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.3rem;
    }

    .hub-sub {
        color: #a9c6e8;
        font-size: 1.05rem;
        line-height: 1.6;
    }

    .metric-label {
        color: #8fd9ff;
        font-size: 0.95rem;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Header
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div style="text-align:center; margin-bottom: 1.5rem;">
        <span class="badge-pulse"></span>
        <span style="color:#00ffc8; letter-spacing:3px; font-size:0.95rem;">
            SYSTEM ONLINE
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# 1) Real-time clock (second-level precision)
# ----------------------------------------------------------------------------
now = datetime.datetime.now()

st.markdown(
    f"""
    <div class="ai-card" style="text-align:center;">
        <div class="clock-text">{now.strftime('%H:%M:%S')}</div>
        <div class="date-text">{now.strftime('%A, %d %B %Y')}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# 2) CPU / RAM usage
# ----------------------------------------------------------------------------
cpu_percent = psutil.cpu_percent(interval=0.1)
ram = psutil.virtual_memory()
ram_percent = ram.percent
ram_used_gb = ram.used / (1024 ** 3)
ram_total_gb = ram.total / (1024 ** 3)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="ai-card">', unsafe_allow_html=True)
    st.markdown('<div class="metric-label">CPU Usage</div>', unsafe_allow_html=True)
    st.progress(min(int(cpu_percent), 100))
    st.markdown(f"### {cpu_percent:.1f}%")
    st.caption(f"{psutil.cpu_count(logical=True)} logical cores")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="ai-card">', unsafe_allow_html=True)
    st.markdown('<div class="metric-label">RAM Usage</div>', unsafe_allow_html=True)
    st.progress(min(int(ram_percent), 100))
    st.markdown(f"### {ram_percent:.1f}%")
    st.caption(f"{ram_used_gb:.1f} GB / {ram_total_gb:.1f} GB used")
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# 3) AI Hub for Cyber Security — teaser text
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div class="ai-card">
        <div class="hub-title">The Future of Defense is Almost Here</div>
        <div class="hub-sub">
            <b>AI Hub for Cyber Security</b> is approaching launch — a unified platform where
            artificial intelligence meets digital defense. Real-time threat detection,
            autonomous incident response, predictive risk analysis, and intelligent
            monitoring are converging into a single command center built for the
            next generation of cyber resilience.
            <br><br>
            Stay ready. The convergence of AI and cyber security is coming online.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Footer
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div style="text-align:center; color:#5f7fa3; font-size:0.85rem; margin-top:1rem;">
        Powered by Streamlit • Live system telemetry
    </div>
    """,
    unsafe_allow_html=True,
)
