from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Data from /api/list/flags/session using self hosted  dedicated ams2 server. Can update when new flags are added
# TODO : Grab values from API
data = [
    {"value": 2, "name": "FORCE_IDENTICAL_VEHICLES"},
    {"value": 8, "name": "ALLOW_CUSTOM_VEHICLE_SETUP"},
    {"value": 16, "name": "FORCE_REALISTIC_DRIVING_AIDS"},
    {"value": 32, "name": "ABS_ALLOWED"},
    {"value": 64, "name": "SC_ALLOWED"},
    {"value": 128, "name": "TCS_ALLOWED"},
    {"value": 256, "name": "FORCE_MANUAL"},
    {"value": 512, "name": "FORCE_SAME_VEHICLE_CLASS"},
    {"value": 1024, "name": "FORCE_MULTI_VEHICLE_CLASS"},
    {"value": 131072, "name": "FILL_SESSION_WITH_AI"},
    {"value": 262144, "name": "MECHANICAL_FAILURES"},
    {"value": 524288, "name": "AUTO_START_ENGINE"},
    {"value": 1048576, "name": "TIMED_RACE"},
    {"value": 4194304, "name": "PASSWORD_PROTECTED"},
    {"value": 8388608, "name": "ONLINE_REPUTATION_ENABLED"},
    {"value": 16777216, "name": "WAIT_FOR_RACE_READY_INPUT"},
    {"value": 33554432, "name": "HAS_RACE_DIRECTOR"},
    {"value": 67108864, "name": "HAS_BROADCASTER"},
    {"value": 134217728, "name": "PIT_SPEED_LIMITER"},
    {"value": 268435456, "name": "PIT_STOP_ERRORS_ALLOWED"},
    {"value": 536870912, "name": "DISABLE_DRIVING_LINE"},
    {"value": 1073741824, "name": "ANTI_GRIEFING_COLLISIONS"},
    {"value": -2147483648, "name": "COOLDOWNLAP"}
]

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/calculate', methods=['POST'])
def calculate():
    selected_values = request.json.get('selected_values', [])
    total_value = sum(selected_values)
    return jsonify(total_value=total_value)

@app.route('/populate', methods=['POST'])
def populate():
    total_value = request.json.get('total_value', 0)
    selected_values = []
    for item in sorted(data, key=lambda x: abs(x['value']), reverse=True):
        if total_value == 0:
            break
        if abs(item['value']) <= abs(total_value):
            selected_values.append(item['value'])
            total_value -= item['value']
    return jsonify(selected_values=selected_values)

if __name__ == '__main__':
    app.run(debug=True)

