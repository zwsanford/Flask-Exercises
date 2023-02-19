from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def date():
    data = datetime.now().strftime("%c")
    return render_template('date.html', date = data)

if __name__ == "__main__":
    app.run(debug=True)