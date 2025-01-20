import streamlit as st
import pandas as pd

st.title('Sales Data Analytics App')

df = pd.read_csv('sample-data.csv')

st.write("Original Data Preview:")
st.dataframe(df)

st.markdown("---")

aggregated_data = df.groupby("Country", as_index=False)["Amount"].sum()
aggregated_data_2 = df.groupby("Country", as_index=False)["Boxes Shipped"].sum()

col1, col2 = st.columns(2)

with col1:
    st.write("### Sales Amount by Country")
    st.dataframe(aggregated_data)

with col2:
    st.write("### Boxes Shipped by Country")
    st.dataframe(aggregated_data_2)

st.markdown("---")

st.write("### Sales Amount by Country Visualization")
st.bar_chart(data=aggregated_data, x="Country", y="Amount")
st.markdown("---")
st.write("### Boxes Shipped by Country Visualization")
st.bar_chart(data=aggregated_data_2, x="Country", y="Boxes Shipped")

df['Date'] = pd.to_datetime(df['Date'])

df['Year-Month'] = df['Date'].dt.to_period('M').astype(str)

month_country_data = df.groupby(['Year-Month', 'Country'], as_index=False)['Amount'].sum()

pivot_data = month_country_data.pivot(index='Year-Month', columns='Country', values='Amount')

pivot_data.sort_index(inplace=True)
st.markdown("---")
st.title("Month-wise Sales Line Chart for Each Country")
st.line_chart(pivot_data)
