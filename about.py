import streamlit as st

from streamlit_extras.switch_page_button import switch_page
st.set_page_config(page_title="OncoMRI: TumorTeller", page_icon="💊", layout="wide")
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

st.title("Welcome to OncoMRI: TumorTeller")

st.write(
    "This project is made with the goal to help people identify types of tumors found within a MRI."
)

aps = st.button("Find Out!")
if aps:
    switch_page("predictor")

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

st.header("Model")
st.write(
    "We used a dataset from Kaggle to train our model. The dataset is [linked here](https://www.kaggle.com/datasets/denizkavi1/brain-tumor) and our team annotated over 15000 images in order to train the ai model. The model we used was yolov7 because of its quick inference speed and high accuracy. The model was trained two times, the first one for 200 epochs on a batch size of 64 then a run for 100 epochs on the same batch size to fine tune the model further."
)
st.write("The relevent graphs and info are shown below.")
st.subheader("Run One")
st.caption("Performance")
st.image("images/results.png")
st.caption("Test Batch One")
st.image("images/vb.jpg")
