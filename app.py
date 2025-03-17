from flask import Flask, render_template, request, jsonify
from utils import generate_packing_list, init_db, close_db

app = Flask(__name__)

# Initialize database (if used)
@app.before_request
def setup():
    init_db()

# Close database connection after each request
@app.teardown_appcontext
def teardown(exception):
    close_db(exception)

@app.route('/', methods=['GET'])
def index():
    """Render the home page with input form."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """Generate and display packing list."""
    trip_type = request.form['trip_type']
    duration = request.form['duration']
    weather = request.form['weather']
    
    try:
        packing_list = generate_packing_list(trip_type, duration, weather)
        return render_template('result.html', packing_list=packing_list, trip_type=trip_type, duration=duration, weather=weather)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)