import streamlit as st
import pickle
import numpy as np
import pandas as pd

pipe = pickle.load(open("pipe.pkl", "rb"))
df = pickle.load(open("df.pkl","rb"))
st.title("Freelancer Price Estimator")
st.write("Welcome to the Freelancer Dashboard! Here you can predict the hourly rate charged by a freelancer, based on feature like years of experiences, average rating, domain, and more.")

# Domain selectbox
domain = st.selectbox("Domain", df["Domain"].unique())

# Experience slider
experience = st.slider("Experience (Years)",
                       float(df["Experience_Years"].min()),
                       float(df["Experience_Years"].max()),
                       float(df["Experience_Years"].mean()))

# Projects completed
project = st.slider("Projects Completed",
                    int(df["Projects_Completed"].min()),
                    int(df["Projects_Completed"].max()),
                    int(df["Projects_Completed"].mean()))

# Rating
rating = st.slider("Average Rating",
                   float(df["Avg_Rating"].min()),
                   float(df["Avg_Rating"].max()),
                   float(df["Avg_Rating"][df["Avg_Rating"] > 0].mean())  # avoid skew from 0s if needed
                   )

# Premium certified
premium_certified = st.radio("Premium Certified", [0, 1])

# Portfolio pieces
portfolio_pieces = st.slider("Portfolio Pieces",
                              int(df["Portfolio_Pieces_Count"].min()),
                              int(df["Portfolio_Pieces_Count"].max()),
                              int(df["Portfolio_Pieces_Count"].mean()))

# Learning hours per week
learning = st.slider("Learning Hours per Week",
                     int(df["Learning_Hours_Per_Week"].min()),
                     int(df["Learning_Hours_Per_Week"].max()),
                     int(df["Learning_Hours_Per_Week"].mean()))

# New freelancer
new = st.radio("Is New Freelancer", [0, 1])

if st.button("Predict Hourly Price"):
    input_df = pd.DataFrame([{
        "Domain": domain,
        "Experience_Years": experience,
        "Projects_Completed": project,
        "Avg_Rating": rating,
        "Premium_Certified": premium_certified,
        "Portfolio_Pieces_Count": portfolio_pieces,
        "Learning_Hours_Per_Week": learning,
        "Is_New": new
    }])
    
    prediction = pipe.predict(input_df)[0]
    st.subheader(f"Estimated Hourly Rate: USD {round(prediction, 2)}")



