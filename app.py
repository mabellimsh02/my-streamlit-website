import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = "https://lottie.host/0aefadc4-2475-4ad8-be27-0fd5278502df/9YuLAAoNBK.json"

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Mabel :wave:")
    st.title("A student")
    st.write("I am passionate to learn more about the usage of Python in web development.")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns (2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am deeply interested in computer science, especially real-time systems and interactive simulations. I am always eager to learn new programming languages, and I put my best effort in polishing my skills through online courses and programming. I believe that being a student at SIT gives me an opportunity to refine my knowledge of intricate systems while acquiring industry-ready competencies in game development and high-performance computing.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ---- #

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Two columns: left for overview, right for simulation
left_col, right_col = st.columns([1, 2])

# === LEFT COLUMN: Overview ===
with left_col:
    st.title("COVID Simulation Project")
    st.markdown("""
    **Overview:**

    This simulation is inspired by the [COVID Simulation Project by Steve Bitner](http://nifty.stanford.edu/2021/bitner-covid-sim/).  
    It models how social behavior and infection parameters influence the spread of a virus over time using an SIR (Susceptible-Infected-Recovered) model.  
    Users can adjust parameters to visualize the progression of an outbreak interactively.
    """)

# === RIGHT COLUMN: Interactive Simulation ===
with right_col:
    st.subheader("Interactive Simulation Controls")

    # Sliders for user input
    distancing = st.slider("Social Distancing (%)", 0, 100, 60)
    infection_rate = st.slider("Infection Rate", 0.0, 1.0, 0.1)
    recovery_rate = st.slider("Recovery Rate", 0.0, 1.0, 0.03)

    # Basic simulation data (replace with your real model if needed)
    days = 100
    t = np.arange(days)
    infected = np.exp(0.05 * t) * (infection_rate * (100 - distancing) / 100)
    recovered = recovery_rate * t

    infected = np.clip(infected, 0, 1000)
    recovered = np.clip(recovered, 0, 1000)

    # Show as a line chart
    st.line_chart({
        "Infected": infected,
        "Recovered": recovered
    })

# --- CONTACT ---
with st.container():
    st.write("---")
    st.header("Get in Touch with Me!")
    st.write("##")

    # Documentation: https://formsubmit.co/!!! CHANGE EMAIL ADDRESS !!! 
    contact_form = """
<form action="https://formsubmit.co/mlimsh02@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder= "Your name" required>
     <input type="email" name="email" placeholder= "Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()