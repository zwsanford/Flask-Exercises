from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
with app.app_context():
    db = SQLAlchemy(app)

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(200), nullable=False)
    Organization = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<entry %r>' % self.id


@app.route('/', methods=('POST', 'GET'))
def home():
    if(request.method == 'POST'):
        name = request.form['name']
        org = request.form['organization']
        new_entry = ToDo(Name = name, Organization = org)

        try:
            db.session.add(new_entry)
            db.session.commit()
            return redirect("/")
        except:
            return render_template('error to commit to db.model')
    else:
        return render_template("home.html")

@app.route('/register')
def register():
    entrys = ToDo.query.order_by(ToDo.id).all()
    return render_template("register.html", entrys = entrys)


if __name__ == "__main__":
    app.run(debug=True)