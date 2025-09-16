import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("India States Population Visualization")

# Dataset with 29 states (dummy values, you can replace with real census)
data = {
    "State": [
        "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
        "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
        "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
        "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
        "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
        "Uttar Pradesh", "Uttarakhand", "West Bengal", "Jammu & Kashmir"
    ],
    "Population (millions)": [
        53, 1.6, 36, 124, 32,
        1.5, 71, 29, 7.5, 39,
        69, 35, 86, 123, 3,
        3.2, 1.1, 2.2, 47, 28,
        81, 0.7, 77, 40, 4,
        200, 11, 91, 13
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Show dataset
st.subheader("States and Population Data")
st.dataframe(df)

# Select visualization type
vis_type = st.selectbox(
    "Select Visualization Type",
    ["Bar Chart", "Line Chart", "Pie Chart"]
)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

if vis_type == "Bar Chart":
    ax.bar(df["State"], df["Population (millions)"], color="skyblue")
    ax.set_title("Population by State")
    plt.xticks(rotation=90)

elif vis_type == "Line Chart":
    ax.plot(df["State"], df["Population (millions)"], marker="o", linestyle="-", color="green")
    ax.set_title("Population Trend by State")
    plt.xticks(rotation=90)

elif vis_type == "Pie Chart":
    ax.pie(df["Population (millions)"], labels=df["State"], autopct="%1.1f%%", startangle=90)
    ax.set_title("Population Distribution")

# Display plot
st.pyplot(fig)
