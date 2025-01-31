import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache
def load_data():
    return pd.read_csv('all_data.csv')

df = load_data()


st.sidebar.title('E-commerce Dashboard Settings')

 
show_data_preview = st.sidebar.checkbox('Show Data Preview', value=True)
show_summary_stats = st.sidebar.checkbox('Show Summary Statistics', value=True)

 
cities = df['customer_city'].unique()
selected_city = st.sidebar.selectbox('Select Customer City', cities)


st.title('E-commerce Dashboard')

if show_data_preview:
    st.write(df.head())    

if show_summary_stats:
    st.write(df.describe())

st.subheader('Order Status Distribution')
order_status_count = df['order_status'].value_counts()
fig = px.pie(order_status_count, names=order_status_count.index, values=order_status_count.values,
             title="Order Status Distribution")
st.plotly_chart(fig)

st.subheader('Average Review Score by Product Category')
avg_review_scores = df.groupby('product_category_name_english')['review_score'].mean().reset_index()
fig2 = px.bar(avg_review_scores, x='product_category_name_english', y='review_score', 
              title="Average Review Score by Product Category", labels={'review_score': 'Avg Review Score'})
st.plotly_chart(fig2)

st.subheader('Payment Type Distribution')
payment_type_count = df['payment_type'].value_counts()
fig3 = px.bar(payment_type_count, x=payment_type_count.index, y=payment_type_count.values,
              title="Payment Type Distribution", labels={'y': 'Count', 'x': 'Payment Type'})
st.plotly_chart(fig3)

 
filtered_df = df[df['customer_city'] == selected_city]
st.write(f"Showing data for customers from {selected_city}:")
st.write(filtered_df.head())

st.subheader('Average Delivery Time by Product Category')
avg_delivery_time = df.groupby('product_category_name_english')['delivery_time'].mean().reset_index()
fig4 = px.bar(avg_delivery_time, x='product_category_name_english', y='delivery_time',
              title="Average Delivery Time by Product Category", labels={'delivery_time': 'Avg Delivery Time (days)'})
st.plotly_chart(fig4)
