from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    meal = data.get('meal', '')
    
    # Placeholder response for now
    print(f"Received meal input: {meal}")
    return jsonify({
        'status': 'success',
        'received': meal,
        'message': 'This is where macro analysis would go.'
    })

if __name__ == '__main__':
    app.run(debug=True)