import streamlit as st
import pandas as pd
import joblib
covid_detector = joblib.load("covid_detector.joblib")


def main():
    st.title("Covid-19 Detection")
    
    activity = ["Predictions","About"]
    choice = st.sidebar.selectbox("Menu",activity)
    
    if choice == "Predictions":
        st.subheader("Covid-19 Detector")
        
        def user_check():
            cough = st.sidebar.radio('Do you cough?', ['Yes', 'No'])
            cough = (1 if cough == 'Yes' else 0)      
                
            fever = st.sidebar.radio('Do you have Fever?', ['Yes', 'No'])
            fever = (1 if fever == 'Yes' else 0)
                
            sore_throat = st.sidebar.radio('Do you have sore throat?', ['Yes', 'No'])
            sore_throat = (1 if sore_throat == 'Yes' else 0)
                
            shortness_of_breath = st.sidebar.radio('Do you experience shortness of breath?', ['Yes', 'No'])
            shortness_of_breath = (1 if shortness_of_breath == 'Yes' else 0)
                        
            head_ache = st.sidebar.radio("Do you have headache?", ['Yes', 'No'])
            head_ache = (1 if head_ache == 'Yes' else 0)
            
            age_60_and_above = st.sidebar.radio("Aged 60 years and above?", ['Yes', 'No'])
            age_60_and_above = (0.09246934 if age_60_and_above == 'Yes' else 0.90753066)
                        
            test_indication = st.sidebar.radio('What was your test indication?', ['Other', 'Abroad', 'Contact with confirmed'])
            if test_indication == 'Other':
                test_indication = 0.87069931
            elif test_indication == 'Abroad':
                test_indication = 0.09119277
            else:
                test_indication = 0.03810792
                
            user_check = {
                'cough' : cough,
                'fever' : fever,
                'sore_throat' : sore_throat,
                'shortness_of_breath' : shortness_of_breath,
                'head_ache' : head_ache,
                'age_60_and_above' : age_60_and_above,
                'test_indication' : test_indication                            
            }
            
            new_input = pd.DataFrame(user_check, index=[0])
            return new_input

        user_data = user_check()
        
        user_result = covid_detector.predict(user_data)
        
        # mse = 0.0326592958975851
        # corona_result; 0 - Negative, 1 - Positive
        
        st.write("Your corona_result is :",user_result[0])
        st.subheader('Therefore according to your symptoms you are: ')
        output = ''
        if user_result[0] >= 0.5:
            output = 'Positive'
        else:
            output = 'Negative'
    
        st.write(output)
           
    else:
        st.subheader("About")
        st.markdown("""
            ### A simple RandomForestClassifier    
            The model used is based on the data available here; https://github.com/nshomron/covidpred/tree/master/data
            
            ##### By
            + **[Mulongo Cheloti](https://www.linkedin.com/in/paul-mulongo-997b1316a/)**
            
            """)
if __name__ == '__main__':
    main()