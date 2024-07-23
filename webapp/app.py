from flask import Flask, request, render_template, redirect, url_for
import re

app = Flask(__name__)

# Load common passwords
with open('10-million-password-list-top-1000.txt', 'r') as file:
    common_passwords = set(line.strip() for line in file)

# Password validation function
def is_valid_password(password):
    # Length check
    if len(password) < 8:
        return False
    # Check against common passwords
    if password in common_passwords:
        return False
    # Regex for password complexity
    if not re.search(r'[A-Z]', password):  # at least one uppercase
        return False
    if not re.search(r'[a-z]', password):  # at least one lowercase
        return False
    if not re.search(r'[0-9]', password):  # at least one digit
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # at least one special character
        return False
    return True

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        password = request.form['password']
        if is_valid_password(password):
            return redirect(url_for('welcome', password=password))
        else:
            return render_template('home.html', error='Password does not meet requirements or is too common.')
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    password = request.args.get('password')
    return render_template('welcome.html', password=password)

@app.route('/logout')
def logout():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
