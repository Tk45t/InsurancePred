import streamlit as st
import pickle
st.title('Insurance Premium Prediction App')
model = pickle.load(open('model.pkl', 'rb'))  
age_input = st.text_input('Enter age:')     
bmi_input = st.text_input('Enter BMI:')
children_input = st.selectbox('Select No. of childrens:',[1,2,3,4,5],index=None)
st.write('You select:',children_input)
gender = st.radio("Select your gender", ['Male', 'Female'],index=None)
smoking_status = st.radio("Do you smoke?", ['Yes', 'No'],index=None)
if st.button("Predict"):  
    try:
        age = int(age_input)   
        bmi = float(bmi_input)
        children = int(children_input)
        sex = 0 if gender == 'Male' else 1
        smoker = 1 if smoking_status == 'Yes' else 0
        x_test = [[age, sex, bmi, children, smoker]]  
        prediction = model.predict(x_test)[0]   
        st.success(f"Predicted Insurance Premium: ₹{int(prediction):.2f}")
    except Exception as e:
        st.error(f"❌ Error: {e}")
