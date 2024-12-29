# ANN Churn Classification Project

This repository contains a project for predicting customer churn using an Artificial Neural Network (ANN). The model has been trained on a dataset of customer information and is deployed on Streamlit Cloud for interactive use.

## Features

- **Customer Churn Prediction:** Use the model to predict whether a customer is likely to churn based on various input features.
- **Streamlit Web App:** An interactive web app where users can input customer data and get predictions in real-time.
- **User-Friendly Interface:** Simple and intuitive UI designed for both technical and non-technical users.


## Getting Started

### Prerequisites

- Python 3.8 or higher
- Streamlit 1.12.0 or higher

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DataWhizEngineer/ANN-Churn-Classification
   ```

2. Navigate to the project directory:
   ```bash
   cd ann-churn-classification
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application Locally

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and go to `http://localhost:8501` to interact with the app.

### Using the App on Streamlit Cloud

The app is deployed on Streamlit Cloud. You can access it directly via the following link:
[Churn Prediction App](https://ann-churn-classification-kht9z5dmbyab7agjnfvhzc.streamlit.app/)

## Project Structure

```
├── Churn_Modelling.csv    # Dataset used for training the model
├── LICENSE                # License information
├── README.md              # Project documentation
├── app.py                 # Streamlit app script
├── experiments.ipynb      # Jupyter notebook for experimental analysis
├── label_encoder_gender.pkl # Label encoder for the Gender feature
├── model.h5               # Trained ANN model
├── onehot_encoder_geo.pkl # OneHotEncoder for the Geography feature
├── prediction.ipynb       # Jupyter notebook for making predictions
├── requirements.txt       # Python dependencies
├── scaler.pkl             # Scaler for numerical feature normalization
```


## Dataset

The dataset used for this project includes the following features:
- CreditScore
- Geography
- Gender
- Age
- Tenure
- Balance
- NumOfProducts
- HasCrCard
- IsActiveMember
- EstimatedSalary
- Exited

The target variable is **Exited**, indicating whether a customer has churned (1) or not (0).


## Model Details

- **Architecture:** The ANN consists of multiple dense layers with ReLU activation and a sigmoid activation in the output layer.
- **Loss Function:** Binary Cross-Entropy
- **Optimizer:** Adam
- **Evaluation Metrics:** Accuracy, Precision, Recall, F1-Score

## Deployment

The trained model is serialized and stored in the `saved_model/` directory. It is loaded and used for predictions in the Streamlit app.

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

## License

This project is licensed under the No License. See the `LICENSE` file for more details.

## Acknowledgments

- The dataset used in this project is publicly available.
- Thanks to the Streamlit community for providing an excellent framework for building web apps.
