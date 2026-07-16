import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Retail Analytics",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# Header
# ==========================================

st.title("📊 Retail Analytics Dashboard")

st.markdown("""
Visualize AI-powered analytics generated from the product detection results.
""")

st.divider()

# ==========================================
# Check Session
# ==========================================

if "statistics" not in st.session_state:

    st.warning("⚠ Please run Product Detection first.")

    st.stop()

statistics = st.session_state.statistics

# ==========================================
# Metrics
# ==========================================

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "📦 Total Products",
        statistics["products"]
    )

with col2:

    st.metric(
        "🎯 Average Confidence",
        f"{statistics['avg_confidence']:.2f}"
    )

st.divider()

# ==========================================
# Products Chart
# ==========================================

st.subheader("Detected Products")

fig, ax = plt.subplots(figsize=(5,4))

ax.bar(
    ["Products"],
    [statistics["products"]]
)

ax.set_ylabel("Count")

st.pyplot(fig)

st.divider()

# ==========================================
# Confidence Progress
# ==========================================

st.subheader("Detection Confidence")

st.progress(float(statistics["avg_confidence"]))

st.write(f"Confidence Score: **{statistics['avg_confidence']:.2%}**")

st.divider()

# ==========================================
# Summary Table
# ==========================================

summary = pd.DataFrame({

    "Metric":[
        "Detected Products",
        "Average Confidence"
    ],

    "Value":[
        statistics["products"],
        round(statistics["avg_confidence"],3)
    ]

})

st.subheader("Summary")

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)
st.divider()

csv = summary.to_csv(index=False)

st.download_button(

    label="📥 Download Report (CSV)",

    data=csv,

    file_name="Retail_Report.csv",

    mime="text/csv",

    use_container_width=True

)
