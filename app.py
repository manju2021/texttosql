from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_query', methods=['POST'])
def run_query():
    user_query = request.form.get('query')
    # Process the user query (mock result here)
    result = {"message": "Query executed successfully", "data": [["Col1", "Col2"], ["Value1", "Value2"]]}
    return jsonify(result)  

@app.route('/analyze_application', methods=['POST'])
def analyze_application():
    data = request.form
    # Mock analysis
    result = {"message": "Application analysis complete", "chart_data": [1, 2, 3, 4]}
    return jsonify(result)

@app.route('/analyze_aor', methods=['POST'])
def analyze_aor():
    data = request.form
    # Mock analysis
    result = {"message": "AOR analysis complete", "chart_data": [4, 3, 2, 1]}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
