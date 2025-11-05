from flask import Flask,send_file, request

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/join', methods=['POST'])
def join():
    email = request.form.get('email')
    # For now, we’ll just print the email in the terminal.
    # You can later connect this to a database or Google Sheets.
    print(f"New signup: {email}")
    return "<h2>Thanks for joining Virtual Study Clubs!</h2><p>We’ll contact you soon at your email.</p>"

if __name__ == '__main__':
    app.run(debug=True)
