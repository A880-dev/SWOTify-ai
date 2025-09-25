import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

st.set_page_config(page_title="SWOTify", page_icon="🧠")

st.title("🧠 SWOTify")
st.subheader("Get a quick AI-powered SWOT analysis on any idea, startup, or brand.")

with st.form("swot_form"):
    topic = st.text_input("Enter your idea or topic:")
    submitted = st.form_submit_button("Analyze")

if submitted and topic:
    with st.spinner("Analyzing with AI..."):
        prompt = f"""
        Perform a SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis on the following topic:

        {topic}

        Give the response in four clearly labeled sections.
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
        )

        result = response.choices[0].message.content

        # Display in nice columns
        st.markdown("### 🔍 Here's your SWOT Analysis:")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### ✅ Strengths")
            st.write(result.split("Weaknesses")[0].split("Strengths")[1].strip())

        with col2:
            st.markdown("#### ⚠️ Weaknesses")
            st.write(result.split("Opportunities")[0].split("Weaknesses")[1].strip())

        with col1:
            st.markdown("#### 🚀 Opportunities")
            st.write(result.split("Threats")[0].split("Opportunities")[1].strip())

        with col2:
            st.markdown("#### 🔥 Threats")
            st.write(result.split("Threats")[1].strip())
