from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

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
    return render_template('index.html')

@app.route('/timetable', methods=['GET'])
def timetable():
    day = request.args.get('day')
    file_path = "timetable.json"  # pls Replace this path with as per your system where you keep this file 
    timetable = get_timetable(file_path)
    if timetable and day in timetable:
        return jsonify(timetable[day])
    else:
        return jsonify({'error': 'Timetable not found for the selected day'}), 404

if __name__ == "__main__":
    app.run(debug=True)
