from flask import Flask,jsonify,request
import pandas as pd 
import pickle
app=Flask(__name__)

predict_model=pickle.load(open("car_price_prediction_model.pkl","rb"))

@app.route("/")
def home():
    return jsonify({"message":"Hello World"})

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    df = pd.DataFrame([data])

    prediction = predict_model.predict(df)

    return jsonify({
        "prediction": float(prediction[0])
    })


if __name__ == "__main__":
    app.run(debug=True)