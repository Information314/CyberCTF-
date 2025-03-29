from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy Challenges
challenges = [
    {"id": 1, "title": "Basic Web Exploit", "points": 100, "flag": "flag{web_hack}"},
    {"id": 2, "title": "SQL Injection", "points": 200, "flag": "flag{sql_master}"}
]

@app.route('/')
def home():
    return "Welcome to CyberCTF"

@app.route('/challenges')
def challenge_page():
    return str(challenges)

@app.route('/submit_flag', methods=['POST'])
def submit_flag():
    flag = request.form.get('flag')
    for challenge in challenges:
        if flag == challenge['flag']:
            return "✅ Correct Flag! Points Added!"
    return "❌ Wrong Flag! Try Again."

if __name__ == "__main__":
    app.run(debug=True)
