from flask import Flask, render_template, request, jsonify
import requests
from config import API_KEY  # Importação da chave API

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    question = request.form['question']

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'  # Utilização da chave API importada
    }

    data = {
        'prompt': f'{question}  ',
        'max_tokens': 100,
        'temperature': 0.7,
    }


    response = requests.post(
        'https://api.openai.com/v1/engines/text-davinci-002/completions',
        headers=headers,
        json=data
    )
    
    response_data = response.json()

    # Adicionado tratamento de erro
    if 'error' in response_data:
        error_type = response_data['error']['type']
        if error_type == 'insufficient_quota':
            return jsonify({'error': 'You have exceeded your API quota.'})
        else:
            print("API response:", response_data)
            return jsonify({'error': 'An error occurred. Please check the console for details.'})
    
    if 'choices' in response_data:
        answer = response_data['choices'][0]['text'].strip()
        return jsonify({'answer': answer})
    else:
        print("API response:", response_data)
        return jsonify({'error': 'An error occurred. Please check the console for details.'})

if __name__ == '__main__':
    app.run(debug=True)
