from flask import Flask, request, render_template
import pandas as pd
import joblib

# Load the model, scaler, and label encoder
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

app = Flask(__name__)

# List of input fields and crop labels
feature_order = ['soil_moisture', 'soil_type', 'sunlight_exposure', 'wind_speed', 
                 'co2_concentration', 'organic_matter', 'irrigation_frequency',
                 'crop_density', 'pest_pressure', 'fertilizer_usage', 'growth_stage',
                 'urban_area_proximity', 'water_source_type', 'frost_risk', 
                 'water_usage_efficiency', 'crop_label']

# Fertilizer recommendations logic
def recommend_fertilizer(predicted_adjustments):
    recommendations = []
    if predicted_adjustments[0] > 0:  
        recommendations.append(f"Add {predicted_adjustments[0]:.2f} units of Urea (Nitrogen).")
    if predicted_adjustments[1] > 0:  
        recommendations.append(f"Add {predicted_adjustments[1]:.2f} units of DAP (Phosphorus).")
    if predicted_adjustments[2] > 0:  
        recommendations.append(f"Add {predicted_adjustments[2]:.2f} units of Muriate of Potash (Potassium).")
    return recommendations

# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    predicted_output = None
    user_input = None
    fertilizer_recommendations = None

    if request.method == "POST":
        # Collect user input
        crop_name = request.form.get("crop")  # Get crop name
        crop_encoded = label_encoder.transform([crop_name])[0]  # Encode crop name
        
        user_input = {key: float(request.form[key]) for key in feature_order[:-1]}
        user_input['crop_label'] = crop_encoded  # Add encoded crop
        
        # Convert input to DataFrame and scale
        input_data = pd.DataFrame([user_input])
        input_data_scaled = scaler.transform(input_data)

        # Predict adjustments
        predicted_adjustments = model.predict(input_data_scaled)[0]

        # Format predictions
        predicted_output = {
            "Nitrogen (N)": f"{predicted_adjustments[0]:.2f}",
            "Phosphorus (P)": f"{predicted_adjustments[1]:.2f}",
            "Potassium (K)": f"{predicted_adjustments[2]:.2f}",
            "Temperature (°C)": f"{predicted_adjustments[3]:.2f}",
            "Humidity (%)": f"{predicted_adjustments[4]:.2f}",
            "pH": f"{predicted_adjustments[5]:.2f}",
            "Rainfall (mm)": f"{predicted_adjustments[6]:.2f}",
        }

        # Generate fertilizer recommendations
        fertilizer_recommendations = recommend_fertilizer(predicted_adjustments)

    return render_template("index.html", user_input=user_input, predicted_output=predicted_output,
                           fertilizer_recommendations=fertilizer_recommendations,
                           crops=label_encoder.classes_)

if __name__ == "__main__":
    app.run(debug=True)
