from flask import Flask, render_template, request
import random
import string
import time

app = Flask(__name__)

def generate_password(length, use_lowercase, use_uppercase, use_special_chars):
    chars = ""
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_special_chars:
        chars += string.punctuation

    random.seed(time.time())
    password = "".join(random.choice(chars) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    password_length = int(request.form['length'])
    use_lowercase = 'lowercase' in request.form
    use_uppercase = 'uppercase' in request.form
    use_special_chars = 'specialchars' in request.form

    password = generate_password(password_length, use_lowercase, use_uppercase, use_special_chars)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run()
