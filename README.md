# Hot Metal Magnesium (Mg) Prediction Model

## Overview

This project is a machine learning-based web application developed to predict the required Magnesium (Mg) addition in Hot Metal desulfurization processes. The application helps estimate Mg requirements based on key process parameters, enabling faster decision-making and improving operational efficiency in metallurgical applications.

The model has been deployed as an interactive web application using Streamlit, allowing users to input process values and receive instant predictions through a simple interface.

## Features

* Predicts Magnesium (Mg) requirement in Hot Metal treatment
* Clean and user-friendly web interface
* Real-time prediction output
* Fast and lightweight deployment using Streamlit
* Machine learning model integration using Joblib
* Supports industrial process parameter inputs

## Input Parameters

The prediction model uses operational inputs such as:

* Hot Metal Weight
* Hot Metal Temperature
* Sulfur Percentage
* Silicon Percentage
* Target Sulfur Percentage
* Other relevant process parameters (if applicable)

## Technology Stack

* **Programming Language:** Python
* **Framework:** Streamlit
* **Libraries:** Pandas, NumPy, Scikit-learn, XGBoost, Joblib
* **Model Deployment:** Streamlit Community Cloud
* **Version Control:** GitHub

## Project Structure

```text
├── app.py
├── mg_model.pkl
├── requirements.txt
└── README.md
```

## Installation & Local Setup

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run app.py
```

## How It Works

1. User enters process parameters in the web interface.
2. The trained machine learning model loads from `mg_model.pkl`.
3. Input data is processed and passed to the model.
4. The application predicts the Magnesium (Mg) requirement instantly.
5. Output is displayed in an easy-to-understand format.

## Applications

This project can be useful for:

* Steel manufacturing plants
* Metallurgical process optimization
* Production planning
* Process automation support
* Industrial data-driven decision making

## Future Improvements

* Model retraining with larger industrial datasets
* Visualization dashboard for process trends
* Prediction confidence interval display
* Cloud database integration
* Mobile-friendly interface

## Author

Developed as a machine learning deployment project for industrial prediction and process optimization.

## License

This project is intended for educational and research purposes.
