# Import required modules
from flask import Flask, render_template, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Homepage route - Renders HTML template
@app.route('/')
def home():
    return render_template('index.html', name="Sushmithaa", version="1.0.0")
# About page route
@app.route('/about')
def about():
    return render_template('about.html')

# API route - GET and POST
@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    if request.method == 'POST':
        data = request.json
        response = {
            "message": "Data received successfully!",
            "data": data
        }
        return jsonify(response), 201
    else:
        sample_data = {
            "id": 1,
            "name": "Flask Application",
            "version": "1.0.0"
        }
        return jsonify(sample_data)

# Error handler for 404
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.route('/cause-error')
def cause_error():
    return 1 / 0  # This will cause a division by zero error


# Run Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)