import pickle 
import streamlit as st
from streamlit_option_menu import option_menu


diabetes_model=pickle.load(open("C:/Users/ujjav/Downloads/Model/diabetes_model_naive_bayes.sav","rb"))
heart_model=pickle.load(open("C:/Users/ujjav/Downloads/Model/heart_model_naive_bayes.sav","rb"))
#sidebar for navigation
with st.sidebar:
    selected=option_menu("Healthcare Recommendation System",
                         ["Heart Disease Recommendation",
                          "Diabetes Disease Recommendation"],
                         icons=["heart-pulse","capsule"],
                         default_index=0)
    
#diabetes prediction page
if(selected=="Diabetes Disease Recommendation"):
    #page title
    st.title("Diabetes Healthcare Recommendation System")    
    col1,col2,col3=st.columns(3)
    
    
    
    with col1:
        Pregnancies=st.text_input("Number of pregnancies")
    with col2:    
        Glucose=st.text_input("Glucose level")
    with col3:
        Blood_Pressure=st.text_input("Blood pressure level")
    with col1:
        Skin_Thickness=st.text_input("Skin thickness")
    with col2:
        Insulin=st.text_input("Insulin level")
    with col3:
        BMI=st.text_input("BMI")
    with col1:
        DPF=st.text_input("Diabete Pedigree Function")
    with col2:
        Age=st.text_input("Age")
    #code for prediction
    diab_diagnosis=""
    #creating button for prediction
    if st.button("Diabetes Test Result"):
        diab_prediction=diabetes_model.predict([[float(Pregnancies),float(Glucose),float(Blood_Pressure),float(Skin_Thickness),float(Insulin),float(BMI),float(DPF),float(Age)]])
        if(diab_prediction[0]==1):
            st.selectbox(label="Recommended Medicines are:",options=["Metformin: Learn more about metformin","Thiazolidinediones(glitazones)","Insulin releasing pills (secretagogues)","Starch blockers","Incretin based therapies"])
        if(diab_prediction[0]==0):
            diab_diagnosis='Patient is not diabetic'
        else:
            diab_diagnosis='Patient is diabetic'
    st.success(diab_diagnosis)    
    

#heart prediction page
if(selected=="Heart Disease Recommendation"):
    #page title
    st.title("Heart Healthcare Recommendation System") 
    col1,col2,col3=st.columns(3)
    with col1:
        age=st.text_input("Enter the age")
    with col2:
        sex=st.text_input("enter the gender 1 for male and 0 for female")
    with col3:
        cp=st.text_input("Enter the cp value")
    with col1:
        trestbps=st.text_input("Enter the value of resting blood pressure")
    with col2:
        chol=st.text_input("Enter the cholestrol level")
    with col3:
        fbs=st.text_input("Enter the fasting blood sugar level")
    with col1:
        restecg=st.text_input("Enter the ecg result value (0,1,2)")
    with col2:
        thalach=st.text_input("Enter the max heart rate")
    with col3:
        exang=st.text_input("Enter the exang value")
    with col1:
        oldpeak=st.text_input("Enter the oldpeak level")
    with col2:
        slope=st.text_input("Enter the slope level")
    with col3:
        ca=st.text_input("Enter the value of calcium particles")
    with col1:
        thal=st.text_input("Enter the haemoglobin level")
    heart_diagnosis=""
    if st.button("Heart Disease Test Result"):
        heart_prediction=heart_model.predict([[float(age), float(sex), float(cp), float(trestbps), float(chol),
                        float(fbs), float(restecg), float(thalach), float(exang),
                        float(oldpeak), float(slope), float(ca), float(thal)]])
        if(heart_prediction[0]==1):
            st.selectbox(label="Recommended Medicines are:",options=["MeidcAzilsartan (Edarbi)Candesartan (Atacand)","Eprosartan (Teveten)", "Irbesartan (Avapro)","Losartan (Cozaar)","Olmesartan (Benicar)","Telmisartan (Micardis)","Valsartan (Diovan)"])                                                                                                                                             
 

        if(heart_prediction[0]==0):
             heart_diagnosis="The patient is free from any heart disease"
        else:
             heart_diagnosis="Patient has heart disease"
    st.success(heart_diagnosis)         