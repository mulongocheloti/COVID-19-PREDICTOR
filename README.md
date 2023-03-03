# COVID-19-PREDICTOR
---
<b>PROBLEM DEFINITION: Create an app that allows patients to input their symptoms and try to predict whether they have COVID or not.</b>


DATASET: https://github.com/nshomron/covidpred/tree/master/data

The main files are <b><a href='https://github.com/mulongocheloti/COVID-19-PREDICTOR/blob/main/Covid-19_Prediction_Model.ipynb'>.ipynb file</a>, <a href='https://github.com/mulongocheloti/COVID-19-PREDICTOR/blob/main/covid_detector.joblib'>joblib pipeline file</a></b> and <b><a href='https://github.com/mulongocheloti/COVID-19-PREDICTOR/blob/main/app.py'>streamlit application file</a></b>

---
<b>PROJECT STEPS</b>
1.  <b>SET UP</b><br>
    Data Download: Downloaded the file and unzip then move it into your working directory<br>
    I then created an environment named <b>covid</b> and installed jupyter notebook.<br>
    Launched Jupyter Notebook and installed <b>pandas, numpy</b> and <b>matplotlib</b>
	<br>
2.  <b>DATA PREPOCESSING</b><br>
    Using pandas load the dataset, do data type conversion, handle null/missing values, do dimension reduction, visualize the data.<br>
    Frequency encoding and split <b>features</b> from the <b>target</b><br>
	![Data Preprocessing](Snaps/data-preprocessing.PNG)<br>
    <br>
3.  <b>MODEL SELECTION</b><br>
    Using <b>K-Fold Cross validation</b> determine the best algorithm between <b>LinearRegression</b> and <B>RandomForestClassifier</b>.<br>
	![Best Algo](Snaps/choosing-best-algorithm.PNG)<br>
	<br>
    Selected the <b>RandomForestClassifier()</b>.<br>
4.  <b>MODELING</b><br>
    Using <b>train_test_split</b> from sklearn.model_selection we split the data into training and test sets.<br>
    Train the model and do the predictions.<br>
    Compare the predicted values to the actual values using <b>mean squared error</b>.<br>
	![Modeling](Snaps/modeling.PNG)<br>
	<br>
5.  <b>CREATE A PIPELINE USING JOBLIB</b><br>
    Install joblib and streamlit using !pip<br>
    Import joblib and save the model as <b>covid_detector.joblib</b><br>
	![Saving the model](Snaps/save-the-model.PNG)<br>
	<br>
6.  <b>STREAMLIT APPLICATION CODE</b><br>
    Now outside jupyter notebook, using streamlit code a .py file that will create a web page used for model deployment locally and save it as <b>app.py</b><br>
	![Streamlit code](Snaps/app1.PNG)<br>
	![Streamlit code](Snaps/app2.PNG)<br>
	<br>
7.  <b>MODEL DEPLOYMENT</b><br>
    Open cmd from your working directory and type as shown below<br>
    ![Model Deployment](Snaps/cmd-run-streamlit.PNG)
	<br>
    <br>
    This opens your browser and the web page is displayed<br>



https://user-images.githubusercontent.com/68067031/222804948-0fc7cac4-f77c-4e74-ac1a-493c3a09c578.mp4

# THANK YOU
