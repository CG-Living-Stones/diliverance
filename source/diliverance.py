from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/aboutdili')
def about():
    return render_template('about.html')

@app.route('/events/2023')
def events2023():
    return render_template('events/events2023.html')

@app.route('/events/') 
@app.route('/events/2025')
def events2025():
    return render_template('events/events2025.html')

# @app.route('/events/') 
# @app.route('/events/2026')
# def events():
#     return render_template('events/events2026.html')

@app.route('/meettheteam')
def team():
    return render_template('team.html')

@app.route('/contribute')
def donate():
    return render_template('donate.html')

if __name__ == '__main__':
    app.run(debug=True)

app = app
