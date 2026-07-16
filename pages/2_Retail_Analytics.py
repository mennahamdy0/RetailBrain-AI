import streamlit as st
import pandas as pd
import plotly.express as px

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

st.title("Retail Analytics Dashboard")

st.write(
    "Analyze product detection results using interactive visualizations."
)

st.divider()

# ==========================================
# Session State Check
# ==========================================

if "statistics" not in st.session_state:

    st.warning("Please run Product Detection first.")

    st.stop()

statistics = st.session_state.statistics

# ==========================================
# Metrics
# ==========================================

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Detected Products",
        statistics["products"]
    )

with col2:

    st.metric(
        "Average Confidence",
        f"{statistics['avg_confidence']:.2f}"
    )

st.divider()

# ==========================================
# DataFrame
# ==========================================

df = pd.DataFrame({

    "Metric": [

        "Products",

        "Average Confidence"

    ],

    "Value": [

        statistics["products"],

        statistics["avg_confidence"]

    ]

})

# ==========================================
# Products Chart
# ==========================================

st.subheader("Detected Products")

fig = px.bar(

    df.iloc[:1],

    x="Metric",

    y="Value",

    text="Value"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# ==========================================
# Confidence Chart
# ==========================================

st.subheader("Average Confidence")

fig2 = px.bar(

    df.iloc[1:],

    x="Metric",

    y="Value",

    text="Value"

)

st.plotly_chart(

    fig2,

    use_container_width=True

)

st.divider()

# ==========================================
# Summary Table
# ==========================================

st.subheader("Summary")

st.dataframe(

    df,

    use_container_width=True,

    hide_index=True

)

# ==========================================
# Download CSV
# ==========================================

csv = df.to_csv(index=False)

st.download_button(

    "Download Report",

    csv,

    file_name="Retail_Report.csv",

    mime="text/csv"

)
