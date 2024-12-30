from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')
    return redirect(url_for('login'))

@app.route('/main')
def main_page():
    return render_template('main.html')

if __name__ == "__main__":
    app.run(debug=True)