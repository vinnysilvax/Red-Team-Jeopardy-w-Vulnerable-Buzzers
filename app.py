from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
buzzed = {"team": None}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buzzer/<team>')
def buzzer(team):
    return render_template('buzzer.html', team=team)

@app.route('/api/buzz', methods=['POST'])
def buzz():
    team = request.form.get('team')
    if buzzed['team'] is None:
        buzzed['team'] = team
        return jsonify({"status": "OK", "message": f"{team} buzzed first!"})
    else:
        return jsonify({"status": "FAIL", "message": f"Too late! {buzzed['team']} already buzzed."})

@app.route('/reset')
def reset():
    buzzed['team'] = None
    return "Buzzers reset."

if __name__ == '__main__':
    app.run(debug=True)
