from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)




@app.route('/', methods=('POST', 'GET'))
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        if(task_content):
            return redirect('calculate/' + str(task_content))
        else:
            return redirect('/calculate/')
    else:
        return render_template("index.html")

@app.route('/calculate/<task_content>')
def calc(task_content):
    try:
        if(int(task_content)):
            if(int(task_content)% 2 == 0):
                val = str(task_content) + " is even"
            else:
                val = str(task_content) + " is odd"
        return render_template("calc.html", data = val)
    except:
        val = str(task_content) + " is not an integer!"
        return render_template("calc.html", data = val)

@app.route('/calculate/')
def Null():
    val = "No number provided!"
    return render_template("calc.html", data = val)

if __name__ == "__main__":
    app.run(debug=True)