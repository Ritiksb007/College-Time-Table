from flask import Flask, jsonify, request, send_from_directory
import json
import os

app = Flask(__name__)

# Set the custom folder where the index.html is stored
CUSTOM_HTML_FOLDER = os.path.abspath('')  # Root folder where index.html will be

def get_timetable(file_path):
    try:
        with open(file_path, 'r') as file:
            timetable = json.load(file)
        return timetable
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

@app.route('/')
def index():
    # Serve the index.html from the custom folder (outside templates)
    return send_from_directory(CUSTOM_HTML_FOLDER, 'index.html')

@app.route('/timetable', methods=['GET'])
def timetable():
    day = request.args.get('day')
    file_path = "timetable.json"  # Please replace this path with your actual file path
    timetable = get_timetable(file_path)
    if timetable and day in timetable:
        return jsonify(timetable[day])
    else:
        return jsonify({'error': 'Timetable not found for the selected day'}), 404

if __name__ == "__main__":
    app.run(debug=True)
