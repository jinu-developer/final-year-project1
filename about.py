# about.py is the about page of our website ONCO-MRI
import streamlit as st

# switch page is a library to switch between different pages in streamlit
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(page_title="final year project", page_icon="💊", layout="wide")
st.markdown(
    """
        <style>
            [data-testid="stSidebarNav"] {
                background-repeat: no-repeat;                
            }
            [data-testid="stSidebarNav"]::before {
                content: "OncoMRI";
                margin-left: 20px;
                margin-top: 20px;

                font-size: 30px;
                text-align: center;
                position: relative;
            }
        </style>
        """,
    unsafe_allow_html=True,
)
# this piece of code is the introduction to the website and will be displayed on this page.
st.title("Welcome to Intracranial tumor image classification")

st.write(
    "This project is made with the goal to help people identify types of tumors found within a MRI by  M.Abarna , Jinu Johnson , V.Joshini under the guidance of Dr.M.Robinson Joel sir of Kings Engineering College"
)

aps = st.button("Find Out!") # to find out the type of tumour we have to click on this button
if aps:
    switch_page("predictor") # switch to the predictor.py page

st.write("""This project was initiated because of the significant importance of brain cancer as a pressing issue. Brain cancer, including gliomas, meningiomas, and pituitary tumors, affects countless individuals and their families around the world. It is a devastating disease that can have profound effects on physical, emotional, and cognitive well-being. Understanding the causes, effects, and available treatments for these brain tumors is crucial for raising awareness, promoting early detection, and improving patient outcomes.

By exploring the causes of these tumors, we can work towards identifying risk factors and developing preventive strategies. Understanding the effects of brain cancer helps us recognize the impact it has on individuals' lives, guiding efforts to provide appropriate support and care for patients. Additionally, knowledge of the available treatments helps healthcare professionals and patients make informed decisions about managing and combating these tumors effectively.""")

st.header("Types of tumors")
st.dataframe(
    data={
        "Tumor Types": [
            "Glioma",
            "Meningioma",
            "Pituitary",
        ],
    },
    width=1000,
)
# Description about the types of tumour with the help of images.
st.subheader("Glioma")
st.write(
    """
    Glioma is a brain tumor that develops from glial cells. Its exact causes are not fully known, but risk factors include radiation exposure and certain genetic disorders. Gliomas can affect brain function, causing headaches, seizures, and neurological deficits. MRI is used to detect and evaluate gliomas, showing abnormal masses or areas of increased signal intensity. The size, location, and enhancement pattern of the tumor help determine its grade and guide treatment decisions.
 """
)
st.image("images/glioma.webp", caption="Glioma", width=350)

st.subheader("Meningioma")
st.write(
    """
 Meningioma is a brain tumor that originates from the meninges, the protective membranes covering the brain and spinal cord. Its exact cause is unknown, but risk factors include radiation exposure, certain genetic conditions, and hormonal factors. Meningiomas can vary in symptoms depending on size and location. MRI is commonly used to detect and evaluate meningiomas, showing well-defined masses with a dural tail.
"""
)
st.image("images/Meningioma.jfif", caption="Meningioma", width=350)

st.subheader("Pituitary")
st.write(
"""
A pituitary tumor, also known as pituitary adenoma, is a non-cancerous growth in the pituitary gland. It can be functioning or non-functioning, causing hormonal imbalances or symptoms due to its size. Symptoms may include headaches, vision problems, fatigue, and hormonal disturbances. Diagnosis involves imaging tests like MRI, and treatment options include medication, surgery, or radiation therapy.
"""
)
st.image("images/petu.jfif", caption="Pituitary", width=350)

st.header("Contributors")
#  Model description and how it works
st.write(
    "M.Abarna(210820205002)
Jinu Johnson(210820205037)
V.Joshini(210820205039)
Under The Guidance of Dr.M.Robinson Joel , Kings engineering college"
)
st.write("The relevent graphs and info are shown below.")
st.subheader("Run One")
st.caption("Performance")
st.image("images/results.png")
st.caption("Test Batch One")
st.image("images/vb.jpg")
