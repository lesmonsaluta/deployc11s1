import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st


class Pages:

    
    
    def introduction():
        # Write the title and the subheader
        st.title(
            "Towards Financial Inclusion (FI): using survey data to assess FI status of the Philippines"
        )
        st.subheader(
            """
            In line with the National Strategy for Financial Inclusion (NSFI) 2022-2028 by Bangko Sentral ng Pilipinas (BSP), this sprint aims to:
            1. Profile financial inclusion (FI) metrics in the Philippines using survey data from World Bank.
            2. Formulate policy recommendations to further improve access to financial services particularly to vulnerable sectors.
            """
        )

    
        # Load data
        data = pd.read_csv('micro_world.csv', encoding='ISO-8859-1')
    
        # Display data
        st.markdown("**The Data**")
        st.dataframe(data)
        st.markdown("Source: Global Findex 2017 from World Bank.")
    
    def body():
        st.title("This is the Body")
    
    
    def ending():
        st.title("This is the Ending")
