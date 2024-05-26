import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt

vehicle_df = pd.read_csv('vehicles_us.csv')

st.header("Car Condition vs. Number of Cars")

# Create a bar chart using Plotly Express
fig = px.bar(vehicle_df, x='condition', title='Car Condition vs. Number of Cars')
fig.update_xaxes(categoryorder='total descending')  # Sort x-axis labels by total count
fig.update_layout(xaxis_title='Car Condition', yaxis_title='Number of Cars')

# Display the chart
st.plotly_chart(fig)

# Dropdown menu for selecting vehicle type
selected_type = st.selectbox("Select a vehicle type", vehicle_df["type"].unique())

# Filter dataframe based on selected type
filtered_df = vehicle_df[vehicle_df["type"] == selected_type]

# Create a scatter plot using Plotly Express
fig = px.scatter(filtered_df, x="condition", y="price", color="paint_color",
                 title=f"{selected_type.capitalize()} Cars: Condition vs. Price",
                 labels={"condition": "Car Condition", "price": "Price"})

# Add interactive hover effects
fig.update_traces(hovertemplate="<b>Condition:</b> %{x}<br><b>Price:</b> %{y:$,.0f}")

# Display the chart
st.plotly_chart(fig)

st.header("Mean Odometer Value by Vehicle Type")

vehicle_df['odometer'] = pd.to_numeric(vehicle_df['odometer'], errors='coerce')
median_odometer = vehicle_df['odometer'].median()
vehicle_df['odometer'].fillna(median_odometer, inplace=True)

# Calculate the mean odometer value for each vehicle type
mean_odometer_by_type = vehicle_df.groupby('type')['odometer'].mean()
mean_odometer_by_type

# Dropdown menu for selecting the first vehicle type
selected_type_1 = st.selectbox("Select the first vehicle type", vehicle_df["type"].unique())

# Dropdown menu for selecting the second vehicle type
selected_type_2 = st.selectbox("Select the second vehicle type", vehicle_df["type"].unique())

# Filter dataframe based on selected types
filtered_df_1 = vehicle_df[vehicle_df["type"] == selected_type_1]
filtered_df_2 = vehicle_df[vehicle_df["type"] == selected_type_2]

# Checkbox to toggle plot type
show_bar_chart = st.checkbox("Show Bar Chart")

# Plotly Express bar chart or scatter plot
if show_bar_chart:
    fig = px.bar(filtered_df_1, x="type", y="odometer", labels={"odometer": "Mean Odometer Value"},
                 title=f"Comparison: {selected_type_1} vs. {selected_type_2}")
    fig.add_trace(px.bar(filtered_df_2, x="type", y="odometer", labels={"odometer": "Mean Odometer Value"}).data[0])
else:
    st.write("Select the checkbox to show the bar chart.")

st.plotly_chart(fig)

