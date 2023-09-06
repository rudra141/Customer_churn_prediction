import pickle
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open('trained_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', prediction_text="")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the form data
        gender = int(request.form['gender'])
        location = int(request.form['location'])
        age = int(request.form['age'])

        # Preprocess the data and perform prediction using your model
        prediction = model.predict([[gender, location, age]])

        # Display the prediction result
        return render_template('index.html', prediction_text=f"Churn Prediction: {prediction[0]}")

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
