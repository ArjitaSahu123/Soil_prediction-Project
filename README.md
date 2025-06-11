# 🌱 Soil Adjustment Prediction System

A Machine Learning-based web application that analyzes soil parameters and recommends suitable crops for cultivation, along with adjustment suggestions for improved soil health.

## 📌 Features

- 🌾 **Crop Recommendation**: Suggests the most suitable crop based on soil parameters.
- 🔬 **Soil Health Prediction**: Uses a neural network to predict soil health categories.
- 📊 **Data Normalization & Encoding**: Preprocessing includes label encoding and feature scaling.
- 🌐 **Web Interface**: User-friendly UI built using Flask templates.
- 🧠 **Pre-trained Models**:
  - `model.pkl`: Traditional ML model for crop recommendation.
  - `neural_model.h5`: Neural network model for soil health prediction.

## 🆚 What Makes This Model Unique?

Unlike many basic models that only recommend crops based on basic nutrient values (N, P, K), this project incorporates:

- ✅ **Multi-Model Approach**: Combines both classical ML (RandomForest, DecisionTree, etc.) and deep learning (Neural Networks) for more robust predictions.
- ✅ **Dual Functionality**: Not just crop recommendation, but also soil *adjustment advice* via classification of soil health.
- ✅ **Feature-Rich Input**: Utilizes real-world parameters like humidity, temperature, pH, and rainfall to ensure location-aware and seasonally accurate suggestions.
- ✅ **Custom Preprocessing Pipelines**: Includes saved `scaler.pkl` and `label_encoder.pkl` to replicate training environment in production.
- ✅ **Optimized for Deployment**: Models are lightweight and fast, making them suitable for real-time applications in web or mobile environments.

This multi-layered architecture ensures a more accurate, scalable, and actionable decision-making system compared to traditional, single-purpose models.

## 🗂️ Project Structure

├── app.py # Main Flask application
├── soil_predict.ipynb # Jupyter notebook with model training and testing
├── Crop_recommendationV2.csv # Dataset used for training
├── model.pkl # ML model for crop recommendation
├── neural_model.h5 # Neural network for soil health prediction
├── scaler.pkl # Scaler used to normalize input data
├── label_encoder.pkl # Label encoder for categorical features
├── templates/ # HTML templates for frontend
├── static/ # Static files (CSS, JS)
└── README.md # Project documentation

## 🧪 Technologies Used

- Python
- Flask
- Pandas, NumPy
- Scikit-learn
- TensorFlow / Keras
- HTML/CSS (for frontend)
- Jupyter Notebook

## 📊 Dataset

The dataset `Crop_recommendationV2.csv` contains labeled samples with the following features:

- **N** – Nitrogen level in the soil
- **P** – Phosphorus level
- **K** – Potassium level
- **temperature** – Temperature in Celsius
- **humidity** – Relative humidity
- **ph** – Soil pH value
- **rainfall** – Rainfall in mm
- **label** – Suitable crop name

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ArjitaSahu123/soil-adjustment-prediction.git
cd soil-adjustment-prediction
```

### 2. Install Dependencies
It is recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
If requirements.txt is not present, manually install:
``` bash
pip install flask pandas numpy scikit-learn tensorflow
```

### 3. Run the Application
 ``` bash
python app.py
```
###  The app will be available at http://127.0.0.1:5000/.

### Work flow
![Screenshot 2024-11-04 143649](https://github.com/user-attachments/assets/145764c3-9986-4d5e-b81b-805bc8c892bb)

 ###📷 Screenshots
![Screenshot 2024-12-08 152300](https://github.com/user-attachments/assets/ea9822bf-c03e-44aa-9f3d-783af1851ab8)

 ![Screenshot 2024-12-08 152334](https://github.com/user-attachments/assets/9a00d793-3ed9-4140-b2b7-9cb7b81ea4b5)

![Screenshot 2024-12-08 152357](https://github.com/user-attachments/assets/40fc31da-6b3d-42fa-909a-5849d55739c7)

![Screenshot 2024-12-08 152415](https://github.com/user-attachments/assets/8b1b577d-92e2-4edd-8a54-a87bf9fc7baf)



🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


👩‍💻 Author
Arjita Sahu
📧 Contact: [arjitasahu.2020@gmail.com]
🔗 GitHub: ArjitaSahu123

