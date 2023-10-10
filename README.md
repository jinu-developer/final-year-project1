# OncoMRI: The Tumor Teller :pill: :computer:
<p align="center">

![logo-color](https://github.com/Hs918131/OncoMRI/assets/91822610/739362e9-302a-4207-8c19-75b6e5d30b0b)

</p>
</br>

## Website Link: https://oncomri.streamlit.app/

## Details : 
### Team Member 1:
**Name** : Ayesha Khan</br>

**Country of Residence** : India</br>

**College Name** : Dr. APJ Abdul Kalam Technical University

**Graduation Year**: 2025

**Experience Level** : Student</br>

### Team Member 2:
**Name** : Harshit Sharma</br>

**Country of Residence** : India</br>

**College Name** : Dr. APJ Abdul Kalam Technical University

**Graduation Year**: 2025

**Experience Level** : Student</br>

## Theme : 
By combining advanced technology and compassionate care, we aim to improve brain health and create a healthier future with AI-powered solutions.

## Problem Statement:
The existing methods of diagnosing brain tumors through MRI scans often involve time-consuming and error-prone manual analysis by medical professionals. Additionally, there is a need for a secure and privacy-centric approach to handling sensitive patient data during the diagnostic process. The key points of the problem statement are as follows:

MRI scans are currently used to diagnose brain tumors, but this process often involves manual analysis by medical professionals, which can be time-consuming and prone to errors. Additionally, patient data must be handled securely and privately during the diagnostic process. The problem statement can be summarized as follows: 

* **Manual MRI Analysis**: Current methods rely heavily on manual analysis, which can cause delays in diagnosis and treatment planning. 
* **Accuracy and Efficiency**: Early detection and timely intervention are crucial for patient outcomes and survival rates, so there is a need for a more accurate and efficient tumor identification process. 
* **Lack of Comprehensive Information**: Patients often receive limited information about their brain tumor, which can hinder informed decision-making. Providing comprehensive insights is essential for patient empowerment. 
* **Data Privacy Concerns**: Patient data, including MRI scans, must be handled securely and not stored for privacy reasons. 
* **Streamlining Appointment Booking**: Appointment booking can be cumbersome and inefficient. An integrated system that facilitates seamless scheduling and communication is essential for patient convenience.


## Solution: 💡 
In light of these challenges, **OncoMRI** aims to create an intelligent and privacy-focused solution that revolutionizes brain tumor diagnosis using AI-driven analysis. By leveraging the power of **Azure Custom Vision**, the application seeks to empower patients with comprehensive tumor insights and personalized treatment recommendations, ultimately contributing to improved patient outcomes and enhanced brain health care.

* OncoMRI is an innovative medical software application designed to revolutionize brain tumor diagnosis through AI-driven MRI analysis.
* Leveraging **Azure Custom Vision's** pre-trained machine learning model, the app accurately identifies Meningioma, Glioma, and Pituitary tumors from uploaded MRI scans.
* The platform ensures privacy by not storing any user data or MRI scans, safeguarding sensitive medical information through **Streamlit**.
* With a user-friendly interface built using **Streamlit**, patients can easily upload MRI scans and receive rapid and precise tumor identification results.
* Detailed insights about the detected tumor, including its characteristics, causes, effects, and potential treatments, are provided to enable informed decision-making.
* Personalized treatment recommendations based on the tumor type and stage empower patients to make the best healthcare choices.
* OncoMRI streamlines appointment booking with specialized doctors through its integrated **Azure Logic App**, facilitating seamless communication.
* The app's focus on data privacy, accuracy, and efficiency contributes to early detection and timely intervention, improving patient outcomes and brain health care.

## Tech Stack:
The following tech stacks have been used to create the application and deploy it.  
* **Python** to build the application.
* **Streamlit** to create a responsive web application along with widgets. 
* **Streamlit Community Cloud** to deploy the web application for anyone across the globe to access it. 
* **Microsoft Azure AI Custom Vision** to get a computer vision model trained using our dataset and use it to predict the tumor type with the patient's MRI scan. 
* **Microsoft Azure Logic App** to send emails to the patient, doctor on appointment booking. 
* **GitHub** to host the source code, use the version control (collaboration history), pull requests and GitHub collaboration features to build efficiently with the teammates. It helps a lot to understand the changes and go back and forth if required to complete the software. 


## Installation Guide: ⬇️
First, install the following:
* Python

Then, follow this step-by-step process to run this application:
* Get your Azure subscription: https://azure.microsoft.com/en-in/free
* Create an Azure Custom Vision resource and train the model
* Create the Azure Logic App Resource and add HTTP/HTTPS Trigger and send email (V2) action with the body as input for the trigger function.  
* Travel to the directory where you wish to store the project files using the cd command.
* Clone the repository in your local system.
```bash
git clone https://github.com/Hs918131/OncoMRI
```
* Go to your project directory where all the files are present.
```bash
cd OncoMRI
```
* Install the required dependencies to run the project.
```bash
pip install -r requirements.txt
```
* Replace the endpoint and key with your Azure Custom Vision model resource endpoint and key in predictor.py. 
* Replace the logic app URL with the Azure logic app URL of the trigger in predictor.py.
* Run the application
```bash
streamlit run about.py
```
* Enjoy the app!

## Website Link :globe_with_meridians: : https://oncomri.streamlit.app/

## Social Impact / Novelty:
**OncoMRI** is a socially impactful and innovative solution that brings together AI technology, data privacy, and streamlined healthcare services to empower patients, advance medical practices, and improve brain health outcomes. Its emphasis on early detection, privacy, and informed decision-making holds the potential to positively impact the lives of countless individuals and contribute to the broader advancement of healthcare practices.
* **Enhanced Brain Health Care Access:** OncoMRI brings cutting-edge AI technology to the field of brain tumor diagnosis, making it more accessible to a broader population. With rapid and accurate tumor identification, patients from diverse backgrounds can benefit from early detection and timely treatment, improving overall brain health care outcomes.
* **Empowering Informed Decision-Making:** By providing comprehensive tumor insights and personalized treatment recommendations, OncoMRI empowers patients to actively participate in their healthcare journey. Informed patients can collaborate more effectively with medical professionals, leading to better treatment adherence and improved patient satisfaction.
* **Privacy-Centric Approach:** OncoMRI sets a new standard for data privacy in medical applications. Its commitment to not storing any user data or MRI scans ensures patient information remains secure, addressing concerns about data breaches and confidentiality in healthcare.
* **Time-Efficient Diagnosis:** The use of AI-driven MRI analysis significantly reduces the time required for tumor identification compared to traditional manual methods. Expedited diagnosis allows medical professionals to make timely treatment decisions, potentially leading to improved patient outcomes and reduced healthcare costs.
* **Encouraging Early Detection:** Early detection of brain tumors is critical for successful treatment and increased survival rates. OncoMRI' accurate and efficient identification of tumor types facilitates early intervention, potentially saving lives and improving the long-term prognosis for patients.
* **Promoting Medical Advancement:** The integration of Azure Custom Vision's pre-trained machine learning model into OncoMRI represents a novel approach in the field of medical imaging and diagnosis. This innovation showcases the potential for AI technology to revolutionize healthcare practices and contribute to ongoing medical advancements.
* **Improved Healthcare Collaboration:** The seamless integration of OncoMRI with Azure Logic App streamlines appointment booking and communication between patients and specialized doctors. This enhanced collaboration fosters better doctor-patient interactions and a smoother healthcare experience for all stakeholders.
* **Public Health Awareness:** By providing comprehensive insights into brain tumors and their implications, OncoMRI contributes to public health awareness. Increased understanding of brain health and the importance of early diagnosis may encourage more individuals to undergo regular screenings, promoting overall brain health and well-being.

## Future Scope:
OncoMRI has significant future potential to evolve and improve brain tumor diagnosis and treatment. Through continuous innovation, integration of advanced technologies, and global collaborations, OncoMRI can impact the lives of millions of individuals by fostering early detection, personalized care, and advancements in brain health research and treatment.
* **Expanding Tumor Identification Capabilities:** In the future, OncoMRI can be enhanced to detect and identify a broader range of brain tumors beyond Meningioma, Glioma, and Pituitary tumors. The integration of additional pre-trained machine learning models can extend its capabilities to include other rare or complex tumor types, further improving diagnostic accuracy.
* **Integration of Advanced Imaging Techniques:** OncoMRI can explore the incorporation of advanced imaging techniques, such as functional MRI (fMRI) and diffusion tensor imaging (DTI), to provide more detailed insights into tumor characteristics and potential impact on brain function. This would enable a more comprehensive understanding of the tumor's effects on the patient's overall health.
* **Multi-Modal Analysis for Holistic Diagnosis:** By integrating multiple imaging modalities and clinical data, OncoMRI can adopt a multi-modal analysis approach for a more holistic and accurate diagnosis. The combination of MRI scans with other patient data, such as genetic profiles and medical history, can lead to a deeper understanding of tumor behavior and personalized treatment recommendations.
* **Global Outreach and Collaboration:** OncoMRI can expand its reach to a global scale, collaborating with medical institutions and experts worldwide. This expansion would enable the platform to cater to a more diverse patient population, ensuring its benefits reach individuals from different geographic locations and socioeconomic backgrounds.
* **Predictive Analytics for Treatment Outcomes:** Leveraging historical treatment data, OncoMRI can incorporate predictive analytics to assess the likelihood of treatment success for specific tumor types and patient profiles. This feature would enable medical professionals and patients to make well-informed decisions regarding treatment plans and potential outcomes.
* **Integration with Electronic Health Records (EHRs):** To enhance patient care coordination, OncoMRI can integrate with existing electronic health record systems. This integration would enable seamless sharing of diagnostic reports and treatment recommendations with healthcare providers, facilitating a collaborative and patient-centric approach to care.
* **AI-Driven Research and Clinical Trials:** OncoMRI' vast dataset of anonymized MRI scans and associated information can be leveraged for AI-driven research and clinical trials. The application's anonymized data repository could contribute to advancing brain tumor research, accelerating drug discovery, and facilitating the development of innovative treatment options.
* **AI-Driven Radiomics and Prognostics:** OncoMRI can explore radiomics, which involves extracting quantitative features from MRI scans, to develop AI-driven prognostic models. These models could predict tumor growth rates, treatment responses, and patient outcomes, aiding in personalized treatment planning and long-term care.
* **Mobile Application and Remote Diagnosis:** Developing a mobile application for OncoMRI would enable users to access tumor analysis and treatment recommendations conveniently on their smartphones. This mobile version could also facilitate remote diagnosis, allowing healthcare providers to reach underserved areas and offer expert consultations without geographical constraints.

### Build with :heart: by Ayesha and Harshit

