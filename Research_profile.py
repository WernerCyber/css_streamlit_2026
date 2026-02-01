# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 14:38:26 2026

@author: krouk
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import date



# Title of the app
st.set_page_config(page_title="Research Profile",layout="wide")

# Collect basic information
name = "Mr. Werner Kroukamp"
field = "Drug Development"
institution = "University of the Witwatersrand, Johannesburg"

# Display basic profile information
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("<h1 style='text-align: center;'>Research Profile</h1>", unsafe_allow_html=True)
    

with col1:
    st.write("") 
with col3:
    st.write("")

st.write(f"**Name:** {name}")
st.write(f"**Research Focus:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
"wits_gh_banners.jpg",
caption="Wits University")


# Add education info
st.header(":blue[:material/Book_2: Education]")

st.markdown("* **Bachelor of Science (BSc)**")
st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;University of the Witwatersrand (2021)")

st.markdown("* **Bachelor of Science Honours (BSc Hons)**")
st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;University of the Witwatersrand (2024)")
st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Research Topic: Investigating the effect of a novel anti-cancer compound on the ER stress response of oesophageal cancer cells.")

st.markdown("* **Master of Science (MSc)**")
st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;University of the Witwatersrand (2025, currently completing final year)")
st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Research topic: Discovering the anti-cancer potential Of novel metal-bilirubin complexes and derivatives and the mode of cell death induced.")

#Add bit about lab skills
st.header(":blue[:material/lab_research: Research Skills]")

col1, col2 = st.columns(2)

with col1:
    st.markdown("* Compound synthesis")
    st.markdown("* Cell culture")
    st.markdown("* Molecular biochemistry techniques e.g. PCR, Western blotting, gel electrophorisis")
    st.markdown("* Flow cytometry")

with col2:
    st.markdown("* Spectroscopy techniques: IR and UV/Vis spectroscopy")
    st.markdown("* Data analysis")
    st.markdown("* IBM SPSS statistics")
    st.markdown("* Scientific writing and presentation skills")


#Bit on future research
st.header(":blue[:material/calendar_clock: Future Research]")

st.markdown("* **Doctor of Philosophy (PhD)**")
st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;University of the Witwatersrand (Intended to start: 2027)")
st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Research topic: Machine Learning–Driven Optimization of Therapeutic Compounds for Parkinson’s &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Disease.")

#Recent Interests
st.header(":blue[:material/interests: Recent Interests]")

st.markdown("* Coding skills: Python, Bash, Jupyter")
st.markdown("* Machine Learning")
st.markdown("* Quantum Computing")

#Contact details
st.header(":blue[:material/contact_page: Contact details]")

st.markdown("* **Phone:** 0716868696")
st.markdown("* **Email:** kroukampwerner@gmail.com")

year = date.today().year

footer = f"""
<style>
.footer {{
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: black;
    color: white;
    text-align: center;
    padding: 10px;
    font-size: 14px;
    z-index: 9999;
}}
</style>
<div class="footer">
    <p>© {year} Werner Kroukamp. Streamlit.</p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)







