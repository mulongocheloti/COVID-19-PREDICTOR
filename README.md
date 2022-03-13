# COVID-19-PREDICTOR

<b>PROBLEM DEFINITION: Create an app that allows patients to input their symptoms and try to predict whether they have COVID or not.</b>

DATASET: https://github.com/nshomron/covidpred/tree/master/data

The main files are <b><a href='https://github.com/mulongocheloti/COVID-19-PREDICTOR/blob/main/Covid-19_Prediction_Model.ipynb'>.ipynb file</a>, <a href='https://github.com/mulongocheloti/COVID-19-PREDICTOR/blob/main/covid_detector.joblib'>joblib pipeline file</a></b> and <b><a href='https://github.com/mulongocheloti/COVID-19-PREDICTOR/blob/main/app.py'>streamlit application file</a></b>

<b>PROJECT STEPS</b>
1.  <b>LOAD THE DATASET</b><br>
    Download the file and unzip then move it into your working directory
2.  <b>IMPORT NECCESSARY LIBRARIES</b><br>
    I then created an environment named <b>covid</b> and installed jupyter notebook.<br>
    Launch Jupyter Notebook and install <b>pandas, numpy</b> and <b>matplotlib</b> first
3.  <b>DATA PREPOCESSING</b><br>
    Using pandas load the dataset, do data type conversion, handle null/missing values, do dimension reduction, visualize the data.<br>
    Frequency encoding and split <b>features</b> from the <b>target</b><br>
4.  <b>MODEL SELECTION</b><br>
    Using <b>KFold</b> and <b>Cross_Validation</b> determine the best algorithm between <b>LinearRegression</b> and <B>RandomForestClassifier</b>.<br>
    Selected the <b>RandomForestClassifier()</b>.<br>
5.  <b>MODELLING</b><br>
    Using <b>train_test_split</b> from sklearn.model_selection we split the data into training and test sets.<br>
    Train the model and do the predictions.<br>
6.  <B>MODEL VALIDATION</b><br>
    Compare the predicted values to the actual values using <b>mean squared error</b>.<br>
7.  <b>CREATE A PIPELINE USING JOBLIB</b><br>
    Install joblib and streamlit using !pip<br>
    Import joblib and save the model as <b>covid_detector.joblib</b><br>
8.  <b>STREAMLIT APPLICATION CODE</b><br>
    Now outside jupyter notebook, using streamlit code a .py file that will create a web page used for model deployment locally and save it as <b>app.py</b><br>
9.  <b>MODEL DEPLOYMENT</b><br>
    Open cmd from your working directory and type as shown below<br>
    <img src='https://github.com/mulongocheloti/COVID-19-PREDICTOR/blob/snaps/run%20streamlit%20cmd.PNG'><br>
    <br>
    This opens your browser and the web page is displayed<br>
    <br>
    <img src='https://github.com/mulongocheloti/COVID-19-PREDICTOR/blob/snaps/deploy1.PNG'><br>
    <br>
    Now patients can enter their symptoms as parameters and see if they are positive or not.<br>
    <br>
    <img src='https://github.com/mulongocheloti/COVID-19-PREDICTOR/blob/snaps/deploy2.PNG'>
    <br>
    <br>
    <img src='https://github.com/mulongocheloti/COVID-19-PREDICTOR/blob/snaps/about.PNG'><br>
    <br>
    # THANK YOU
