from typing import Text
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

#init Flask app
app = Flask(__name__)
#config the flask app to query the postgres localhost server
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost/height_collector'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sydvzbdpfzsmxt:a4eb623e8dc286d4ccd10f5aa8b18d969f893669ae3f5beb4f1a6e631f097393@ec2-18-214-238-28.compute-1.amazonaws.com:5432/d5f2n2168cr8d9?sslmode=require'
db = SQLAlchemy(app)

#Configures the web form to pass entered data to the local SQL table
#db.create_all() creates an empty table in the db with these columns since it inherits db.Model
class Data(db.Model):
    #defines the outline of the data table (aka columns)
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique = True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_= email_
        self.height_= height_

#home page
@app.route("/")
def index():
    return render_template("index.html")

#On press of submit
@app.route("/success", methods = ['POST'])
def success():
    if request.method == 'POST':
        #Gets the user input from the form
        email = request.form["email_name"]
        height = request.form["height_name"]
        #Check if the data is unique
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            #Creates an object instance of the Data class with the parameters email, height
            data = Data(email,height)
            #Adds an entry (row) to the open db
            db.session.add(data)
            db.session.commit()

            #Calculate the average of the heights
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            average_height = round(average_height,1)

            count=db.session.query(Data.height).count()

            ## send_email(email, height, average_height, count)

            return render_template("success.html")
        return render_template("index.html", text="Seems like we've got some data already for this email")

if __name__ == '__main__':
    app.debug = True
    app.run()