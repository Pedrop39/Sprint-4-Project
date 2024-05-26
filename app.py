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

st.header("Car Condition vs. Price")

# Create a scatter plot using Plotly Express
fig = px.scatter(vehicle_df, x='condition', y='price', title='Car Condition vs. Price')
fig.update_xaxes(categoryorder='total descending')  # Sort x-axis labels by total count

# Display the chart
st.plotly_chart(fig)

st.header("Mean Odometer Value by Vehicle Type")

vehicle_df['odometer'] = pd.to_numeric(vehicle_df['odometer'], errors='coerce')
median_odometer = vehicle_df['odometer'].median()
vehicle_df['odometer'].fillna(median_odometer, inplace=True)

# Calculate the mean odometer value for each vehicle type
mean_odometer_by_type = vehicle_df.groupby('type')['odometer'].mean()
mean_odometer_by_type

# Dropdown menu for selecting vehicle type
selected_type = st.selectbox("Select a vehicle type", vehicle_df["type"].unique())

# Filter dataframe based on selected type
filtered_df = vehicle_df[vehicle_df["type"] == selected_type]

# Checkbox to toggle plot type
show_bar_chart = st.checkbox("Show Bar Chart")

# Plotly Express bar chart or scatter plot
if show_bar_chart:
    fig = px.bar(filtered_df, x="type", y="odometer", labels={"odometer": "Mean Odometer Value"})
else:
    st.write("Select the checkbox to show the bar chart.")

st.plotly_chart(fig)
