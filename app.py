# import json
# import pyttsx3

# def get_timetable(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             timetable = json.load(file)
#         return timetable
#     except FileNotFoundError:
#         print("The timetable file was not found.")
#         return None
#     except json.JSONDecodeError:
#         print("Error decoding JSON from the timetable file.")
#         return None

# def display_and_speak_timetable(timetable, day):
#     if day in timetable:
#         print(f"Timetable for {day}:")
#         for time, subject in timetable[day].items():
#             print(f"{time}: {subject}")
#             engine.say(f"At {time}, you have {subject}")
#         engine.runAndWait()
#     else:
#         print(f"No timetable available for {day}.")

# if __name__ == "__main__":
#     file_path = "D:/Python Learning/79_timetable.json" # Pls Replace this path
#     timetable = get_timetable(file_path)
    
#     if timetable:
#         day = input("Enter the day of the week (e.g., Monday): ")
#         engine = pyttsx3.init()
#         display_and_speak_timetable(timetable, day)


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
    file_path = "D:/Python Learning/Time Table/79_timetable.json"  # Replace with your JSON file path
    timetable = get_timetable(file_path)
    if timetable and day in timetable:
        return jsonify(timetable[day])
    else:
        return jsonify({'error': 'Timetable not found for the selected day'}), 404

if __name__ == "__main__":
    app.run(debug=True)