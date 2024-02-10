
import streamlit as st # we import the streamlit library to create a web application and host it
import time #library used to give the real time and date updates
# azure services use api key to request the data and the predicted image.
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient 
from msrest.authentication import ApiKeyCredentials
import requests #request external services or api.

#endpoint and prediction key have a constant communication with the azure custom vision.
# Replace with your endpoint and prediction key
ENDPOINT = "https://centralindia.api.cognitive.microsoft.com/"# the url is used to communicate with the custom vision which will be used to authenticate and request the services.
PREDICTION_KEY = "8f1324da86044e98bc87eab3cea0d778"# the provided set of strings and numerics is the API key for Azure custom vision.

# Create a prediction client and set up the streamlit page configuration.
credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_KEY})
predictor = CustomVisionPredictionClient(ENDPOINT, credentials)

st.set_page_config(page_title="OncoMRI: TheTumorTeller App")


# dengue fever

doctors = [
    {
        "name": "Dr. Ayesha Khan",
        "specialization": "Oncologist",
        "location": "Lucknow",
        "available_days": "Mon, Tue, Fri",
        "contact": "ayesha200210@gmail.com",
    },
    {
        "name": "Dr. Harshit Sharma",
        "specialization": "Oncologist",
        "location": "Lucknow",
        "available_days": "Wed, Thu, Sat",
        "contact": "hs918131@gmail.com",
    },
    # Add more doctors here...
]
#fuction for calling doc's info while booking an appointment
def book_appointment(doctor_name, patient_email, patient_name):
    # Add your booking logic here, e.g., database integration, etc.


    # Send confirmation email to the patient
    send_confirmation_email(patient_email, doctor_name, patient_name)


    # Send appointment email to the doctor
    doctor_email = get_doctor_email(doctor_name)
    send_appointment_email(doctor_email, patient_email, doctor_name, patient_name)

    #calls the function success using st(streamlit) once the appointment is booked
    st.success(f"Appointment booked with {doctor_name}. You will be contacted soon!")


def send_confirmation_email(patient_email, doctor_name,patient_name):
   # Replace 'your_azure_logic_app_url' with the URL of your Azure logic app to send appointment emails
    
    # variable contains an URL that triggers an Azure Logic App workflow manually when accessed. It also includes the Logic App's endpoint, workflow ID,other parameters for authentication.
    azure_logic_app_url = f'https://prod-10.centralindia.logic.azure.com:443/workflows/5e4da251ed354e7291b18bbc4c46ab8d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=PzoP9Rs5rxxqAGKwC8t3zLXPlRRpteXtBb1ekR8hppM'
     
     #email format
    email_data = {
        "to": patient_email,
         "name": patient_name,
        "subject": "Appointment Confirmed at OncoMRI",
        "content": f"Your appointment with {doctor_name} has been booked successfully. You will be contacted soon.",
    }


   # it makes a POST request to an Azure Logic App URL with email data in JSON format. It checks the status code either its 200 or 202 according to it reverts back the message as success or failure for confirmation of email.
    # POST is a HTTP request method for sending or calling APIS's.
   
    response = requests.post(azure_logic_app_url, json=email_data)
    if response.status_code == 200 or response.status_code == 202:
        st.success("Confirmation email sent to the patient.")
    else:
        st.error("Failed to send confirmation email.")


def send_appointment_email(doctor_email, patient_email, doctor_name, patient_name):
    # Replace 'your_azure_logic_app_url' with the URL of your Azure logic app to send appointment emails
    azure_logic_app_url = f'https://prod-10.centralindia.logic.azure.com:443/workflows/5e4da251ed354e7291b18bbc4c46ab8d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=PzoP9Rs5rxxqAGKwC8t3zLXPlRRpteXtBb1ekR8hppM'

    email_data = {
        "to": doctor_email,
        "name": doctor_name,
        "subject": "New Appointment at OncoMRI",
        "content": f"A new appointment has been booked with you by {patient_name}. \n More details will be shared soon.",
    }


    response = requests.post(azure_logic_app_url, json=email_data)
    if response.status_code == 200 or response.status_code == 202:
        st.success("Appointment email sent to the doctor.")
    else:
        st.error("Failed to send appointment email.")


def get_doctor_email(doctor_name):
    # Replace this function with a method to retrieve the doctor's email from your database or list
    # In this example, we'll assume the email is stored in the 'contact' field of the doctor's details.
    for doctor in doctors:
        if doctor["name"] == doctor_name:
            return doctor["contact"]


def doctor():
    st.write("Select a doctor to view details and book an appointment:")
    selected_doctor = st.selectbox("Select a doctor", [doctor["name"] for doctor in doctors])


    # Add an input field for the patient's email
    patient_email = st.text_input("Enter your email", "")
    patient_name = st.text_input("Enter your name", "")


    if st.button("Book Appointment"):
        if not patient_email:
            st.warning("Please enter your email.")
        if not patient_name:
            st.warning("Please enter your name.")
        else:
            book_appointment(selected_doctor, patient_email, patient_name)

    # description of doctor with the function st.write as per users choice
    for doctor in doctors:
        if doctor["name"] == selected_doctor:
            st.subheader(doctor["name"])
            st.write(f"Specialization: {doctor['specialization']}")
            st.write(f"Location: {doctor['location']}")
            st.write(f"Available Days: {doctor['available_days']}")



# Description about the types of tumour that will be dectected by the AI and for users to get a knowledge about.
gcauses = """
The exact causes of glioma, a type of brain tumor, are not fully understood. However, certain risk factors have been identified. These include exposure to ionizing radiation, a family history of glioma, and certain genetic disorders such as neurofibromatosis type 1 and Li-Fraumeni syndrome. While these factors may increase the risk, in many cases, the underlying cause of glioma remains unknown.
"""
geffects = """
Gliomas can have significant effects on brain function and overall health. As the tumor grows, it can exert pressure on surrounding brain tissue, leading to symptoms such as headaches, seizures, difficulty speaking or understanding language, memory problems, changes in personality or mood, and neurological deficits like weakness or loss of sensation in the limbs. The severity and specific symptoms experienced by an individual can vary depending on the location, size, and grade of the glioma.
"""
gtreat = """
The treatment of glioma depends on several factors, including the tumor's location, size, grade, and the patient's overall health. Treatment options may include surgery to remove the tumor, radiation therapy to target and kill cancer cells, and chemotherapy to destroy or slow down tumor growth. In some cases, a combination of these treatments may be used. The choice of treatment is determined by a multidisciplinary team of medical professionals and is tailored to the individual patient's needs and circumstances. Regular monitoring and follow-up care are essential to assess the tumor's response to treatment and manage any potential side effects.
"""

mcauses = """The exact causes of meningioma, a type of brain tumor, are not well understood. However, certain risk factors have been identified, including radiation exposure, such as previous radiation therapy to the head, and certain genetic conditions like neurofibromatosis type 2 (NF2). Hormonal factors, such as increased levels of estrogen, have also been associated with an increased risk of developing meningiomas. Nonetheless, the underlying cause of most meningiomas remains unknown.
"""
meffects = """Meningiomas can have varying effects depending on their size, location, and growth rate. Some meningiomas may not cause noticeable symptoms and can be incidentally discovered during imaging tests conducted for unrelated reasons. However, when symptoms do occur, they can include headaches, seizures, changes in vision or hearing, weakness or numbness in the limbs, and cognitive or personality changes. The specific symptoms and their severity can differ from person to person.
"""
mtreat = """
The treatment of meningioma depends on factors such as tumor size, location, and growth rate, as well as the individual's overall health. Treatment options may include observation with regular monitoring for slow-growing or asymptomatic tumors, surgery to remove the tumor, radiation therapy to target and destroy cancer cells, and in some cases, medication to manage symptoms or slow down tumor growth. The choice of treatment is based on a thorough evaluation by a multidisciplinary team of healthcare professionals and is tailored to the specific needs of each patient. Regular follow-up care is important to assess the tumor's response to treatment and address any potential complications or recurrence.
"""

pcauses = """
The exact causes of pituitary tumors, also known as pituitary adenomas, are not fully understood. However, certain factors may increase the risk of their development. These include genetic conditions like multiple endocrine neoplasia type 1 (MEN1) and Carney complex, as well as rare hereditary syndromes such as familial isolated pituitary adenoma. Hormonal imbalances, exposure to certain chemicals, and head injuries have also been suggested as potential contributing factors. However, in many cases, the underlying cause of pituitary tumors remains unknown."""
peffects = """Pituitary tumors can have diverse effects depending on their size, location, and hormone production. They can disrupt the normal functioning of the pituitary gland, leading to hormonal imbalances and associated symptoms. The specific effects can vary widely, ranging from vision problems and headaches due to pressure on nearby structures, to hormonal disturbances resulting in issues such as infertility, growth abnormalities, changes in body composition, and metabolic problems. The effects of pituitary tumors are highly dependent on the specific hormones involved and the individual's overall health.
"""
ptreat = """The treatment of pituitary tumors depends on several factors, including the tumor's size, hormone production, and the individual's overall health. Treatment options may include medication to regulate hormone levels, surgery to remove the tumor, radiation therapy to destroy tumor cells, or a combination of these approaches. The choice of treatment is determined by a multidisciplinary team of medical professionals and is tailored to the individual patient's needs and circumstances. Regular monitoring and follow-up care are often necessary to manage hormone levels, monitor tumor growth, and ensure optimal treatment outcomes.
"""
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
st.title("OncoMRI: TheTumorTeller")
#in this section we upload our MRI scan image in order for AI to detect the type of tumour
st.text(
    "Upload an image of a close up of a tumerous MRI scan and we will tell you what type it is."
)
# read images.zip as a binary file and put it into the button
with open("test.zip", "rb") as fp:
    btn = st.download_button(
        label="Download test images",
        data=fp,
        file_name="test.zip",
        mime="application/zip",
    )
    #image type to be uploaded.
image = st.file_uploader(
    "Upload Image", type=["jpg", "jpeg", "png", "webp"], accept_multiple_files=False
)

if image is not None:#condition for no image found
    disp = False
    
    with image:
        st.image(image, caption="Your MRI Scan", width=350)#once the image is uploaded the title your MRI scan will be shown.
        image_data = image.read()#passed to custom vision for classification purpose.
        results = predictor.classify_image("6abac90a-193b-4a67-b10a-8dae2d78e206", "Iteration1", image_data)
    disp = True
    
    c = st.image("loader1.gif")
    time.sleep(3) # pauses the line for 3 second for processing and before showing the result.
    c.empty()

    # Process and display the results after classification if img provived
    if results.predictions:
        st.subheader("Prediction Results:")
        name="unknown"
        predict=0
        for prediction in results.predictions:
            #This part of code gives the result which has highest confidence score greater than 0.5 and sets the tag name.
            if prediction.probability > predict and prediction.probability > 0.5:
                predict = prediction.probability
                name = prediction.tag_name
    #Once the tumour is detected it displays the name of the tumour along with its confidence level.
    if name!="unknown":
        st.text(f"Detected {name} with high confidence")
        if name == "Glioma":
            st.write(
                """
                Glioma is a brain tumor that develops from glial cells. Its exact causes are not fully known, but risk factors include radiation exposure and certain genetic disorders. Gliomas can affect brain function, causing headaches, seizures, and neurological deficits. MRI is used to detect and evaluate gliomas, showing abnormal masses or areas of increased signal intensity. The size, location, and enhancement pattern of the tumor help determine its grade and guide treatment decisions.
                """
            )
            st.image("images/glioma.webp", caption="Glioma", width=350)
            st.write("More Info")#More info have three tabs ie:causes, effects and treatment.

            tab1, tab2, tab3 = st.tabs(
                ["Causes", "Effects", "Treatment"]
            )
            # we provide the link for all the tabs present
            with tab1:#CAUSES OF GLIOMA TUMOUR
                st.write(gcauses)
                st.write(
                    "More Info can be found on the [Mayo clinic website](https://www.mayoclinic.org/diseases-conditions/glioma/symptoms-causes/syc-20350251)"
                )
            with tab2:#EFFECTS
                st.write(geffects)
                st.write(
                    "More Info can be found on the [Mayo clinic website](https://www.mayoclinic.org/diseases-conditions/glioma/symptoms-causes/syc-20350251)"
                )
            with tab3:#TREATMENT
                st.write(gtreat)
                st.write(
                    "More Info can be found on the [Mayo clinic website](https://www.mayoclinic.org/diseases-conditions/glioma/symptoms-causes/syc-20350251)"
                )
            doctor()

        elif (
            name == "Meningioma"
        ):
            st.write(
                """
                Meningioma is a brain tumor that originates from the meninges, the protective membranes covering the brain and spinal cord. Its exact cause is unknown, but risk factors include radiation exposure, certain genetic conditions, and hormonal factors. Meningiomas can vary in symptoms depending on size and location. MRI is commonly used to detect and evaluate meningiomas, showing well-defined masses with a dural tail.
                """
            )
            st.image("images/Meningioma.jfif", caption="Meningioma", width=350)
            st.write("Known Carried Diseases")
            btab1, btab2, btab3 = st.tabs(
                ["Causes", "Effects", "Treatment"]
            )
            with btab1:
                st.write(mcauses)
                st.write(
                    "More Info can be found on the [Cancer Website](https://www.cancer.gov/rare-brain-spine-tumor/tumors/meningioma)"
                )
            with btab2:
                st.write(meffects)
                st.write(
                    "More Info can be found on the [Cancer Website](https://www.cancer.gov/rare-brain-spine-tumor/tumors/meningioma)"
                )
            with btab3:
                st.write(mtreat)
                st.write(
                    "More Info can be found on the [Cancer Website](https://www.cancer.gov/rare-brain-spine-tumor/tumors/meningioma)"
                )
            doctor()

        elif name == "Pituitary":
            st.write(
                """
                A pituitary tumor, also known as pituitary adenoma, is a non-cancerous growth in the pituitary gland. It can be functioning or non-functioning, causing hormonal imbalances or symptoms due to its size. Symptoms may include headaches, vision problems, fatigue, and hormonal disturbances. Diagnosis involves imaging tests like MRI, and treatment options include medication, surgery, or radiation therapy.
                """
            )
            st.image("images/petu.jfif", caption="Pituitary", width=350)
            st.write("Known Carried Diseases")
            ctab1, ctab2, ctab3 = st.tabs(
                ["Causes", "Effects", "Treatment"]
            )
            with ctab1:
                st.write(pcauses)
                st.write(
                    "More Info can be found on the [MAYO clinic website](https://www.mayoclinic.org/diseases-conditions/pituitary-tumors/symptoms-causes/syc-20350548)"
                )
            with ctab2:
                st.write(peffects)
                st.write(
                    "More Info can be found on the [MAYO clinic website](https://www.mayoclinic.org/diseases-conditions/pituitary-tumors/symptoms-causes/syc-20350548)"
                )
            with ctab3:
                st.write(ptreat)
                st.write(
                    "More Info can be found on the [MAYO clinic website](https://www.mayoclinic.org/diseases-conditions/pituitary-tumors/symptoms-causes/syc-20350548)"
                )
            doctor()

    else:
        # if there is no disease detect then this message will be printed.
        st.text("No disease detected")
    
