# mg-prediction-model
# Hot Metal Mg Prediction Model

This is a Streamlit web application for predicting Magnesium (Mg) in Hot Metal based on process input parameters.

## Features

* User-friendly interface
* Real-time prediction
* Input parameters:

  * HM Weight
  * HM Temperature
  * HM Sulfur (%)
  * HM Silicon (%)
  * Target Sulfur (%)

## Tech Stack

* Python
* Streamlit
* Pandas
* Joblib
* Scikit-learn

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Model File

The trained model is stored in `mg_model.pkl`.
