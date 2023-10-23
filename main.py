import streamlit as st
import plotly.express as px
from backend import noise_sensor_1, noise_sensor_2, noise_sensor_3, noise_sensor_4, noise_sensor_5, noise_sensor_6,noise_data_insights 

from send_mail import send_alert
import pandas as pd
import time
# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
max=0
mean=0
sensor="NO DATA AVAILABLE"


st.set_page_config(
    layout="wide",
    page_title="Noise Level Detector and Alert System",
    page_icon=":sound:"
)

# Title of the page
st.title("Noise Pollution Detector and Alert System using Image Recognition.")
st.write(" ")
st.write(" ")
st.write(" ")

#Information Box and Camera Box

col_1 , col_2 = st.columns([7,3])
with col_1 :
    st.subheader("INFORMATIONs")
    max_container = st.empty()
    mean_container = st.empty()
    sensor_container = st.empty()
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
with col_2 :
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")

# Create Plotly figures (initialize with initial data)
col1 , col2 = st.columns([1,1])
with col1 :
    df_1 = noise_sensor_1()
    fig1 = px.line(x=df_1.columns, y=df_1.iloc[0, :], labels={"x": "NOISE READINGS", "y": "LOUDNESS(dB)"})
    chart1 = st.plotly_chart(fig1, use_container_width=True)
with col2 :
    df_2 = noise_sensor_2()
    fig2 = px.line(x=df_2.columns, y=df_2.iloc[0, :], labels={"x": "NOISE READINGS", "y": "LOUDNESS(dB)"})
    chart2 = st.plotly_chart(fig2, use_container_width=True)

col3 , col4 = st.columns([1,1])
with col3 :
    df_3 = noise_sensor_3()
    fig3 = px.line(x=df_3.columns, y=df_3.iloc[0, :], labels={"x": "NOISE READINGS", "y": "LOUDNESS(dB)"})
    chart3 = st.plotly_chart(fig3, use_container_width=True)

with col4 :
    df_4 = noise_sensor_4()
    fig4 = px.line(x=df_4.columns, y=df_4.iloc[0, :], labels={"x": "NOISE READINGS", "y": "LOUDNESS(dB)"})
    chart4 = st.plotly_chart(fig4, use_container_width=True)


col5 , col6 = st.columns([1,1])
with col5 :
    df_5 = noise_sensor_5()
    fig5 = px.line(x=df_5.columns, y=df_5.iloc[0, :], labels={"x": "NOISE READINGS", "y": "LOUDNESS(dB)"})
    chart5 = st.plotly_chart(fig5, use_container_width=True)

with col6 :
    df_6 = noise_sensor_6()
    fig6 = px.line(x=df_6.columns, y=df_6.iloc[0, :], labels={"x": "NOISE READINGS", "y": "LOUDNESS(dB)"})
    chart6 = st.plotly_chart(fig6, use_container_width=True)

# Periodically update the data and charts
while True:
    #Fetch the new information data
    max, mean, sensor = noise_data_insights()
    if(max>=490):
        message_content=f'''Noise level crossed the thresold value in the {sensor} and the maximum value recorded is {max} , Kindly look after the situation as Camera has been triggered'''
        message = f'''\
Subject :  !!!! ALERT !!!!
        
{message_content}
'''
        send_alert(message,"shrijeetkumarverma140504@gmail.com")
    
    # Update the information container
    with max_container.container():
        st.write(f"LAST MAXIMUM LOUDNESS RECORDED = {max}")
    with mean_container.container():
        st.write(f"MEAN OF THE MAXIMUM LOUDNESS OF ALL SENSORS  = {mean}")
    with sensor_container.container():
        st.write(f"SENSOR WITH THE MAXIMUM LOUDNESS = {sensor}")

    # Fetch new data for each sensor
    df_1 = noise_sensor_1()
    df_2 = noise_sensor_2()
    df_3 = noise_sensor_3()
    df_4 = noise_sensor_4()
    df_5 = noise_sensor_5()
    df_6 = noise_sensor_6()

    # Update the figures with new data
    fig1.update_traces(x=df_1.columns, y=df_1.iloc[0, :])
    fig2.update_traces(x=df_2.columns, y=df_2.iloc[0, :])
    fig3.update_traces(x=df_3.columns, y=df_3.iloc[0, :])
    fig4.update_traces(x=df_4.columns, y=df_4.iloc[0, :])
    fig5.update_traces(x=df_5.columns, y=df_5.iloc[0, :])
    fig6.update_traces(x=df_6.columns, y=df_6.iloc[0, :])

    # Update the charts with the updated figures
    chart1.plotly_chart(fig1, use_container_width=True)
    chart2.plotly_chart(fig2, use_container_width=True)
    chart3.plotly_chart(fig3, use_container_width=True)
    chart4.plotly_chart(fig4, use_container_width=True)
    chart5.plotly_chart(fig5, use_container_width=True)
    chart6.plotly_chart(fig6, use_container_width=True)

    # Sleep for a while before updating again
    time.sleep(1)  # Update every 1 second


