import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Print API Key to confirm it's loaded (for debugging)
print("Loaded API Key:", os.getenv('GEMINI_API_KEY'))

# Configure Gemini with API key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Initialize Gemini model
model = genai.GenerativeModel(model_name='models/gemini-1.5-flash')

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'next-predict-secret')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        user_input = request.form.get('user_input', '').strip()
        if not user_input:
            return render_template('index.html', error="Please enter a sentence.")

        prompt = f"Given the sentence: \"{user_input}\", predict a realistic next sentence."

        predictions = []
        for _ in range(3):
            try:
                response = model.generate_content(prompt)
                predictions.append(response.text.strip())
            except Exception as e:
                print(f"[Gemini API Error] {e}")
                predictions.append("Prediction failed.")

        return render_template('index.html', input_text=user_input, predictions=predictions)

    except Exception as e:
        print(f"[Server Error] {e}")
        return render_template('index.html', error="Something went wrong while processing your request.")

if __name__ == '__main__':
    if not os.getenv('GEMINI_API_KEY'):
        print("⚠️ WARNING: GEMINI_API_KEY not found in .env file.")
    app.run(debug=True, host='0.0.0.0', port=5051)