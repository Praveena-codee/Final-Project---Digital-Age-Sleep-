from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


     
     
if __name__ == "__main__":
    app.run()


###################################################
# # ##import necessary libraries

#from models import create_classes, db
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

import psycopg2 
from psycopg2.extras import RealDictCursor
import pandas as pd 
import numpy as np
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
#from sqlalchemy.dialects.postgresql import json
import pickle

# #CONNECTION TO sleep TABLE 
# try: 
#     connection = psycopg2.connect(user = "postgres", 
#                                   password= "Prav123", 
#                                   host = "127.0.0.1",
#                                   port = "5432", 
#                                   database = "sleepdb") 
#     cursor = connection.cursor(cursor_factory=RealDictCursor)
#     selection = "SELECT * FROM sleep" 
#     cursor.execute(selection)
#     sleep = cursor.fetchall()
#     sleep_df = pd.DataFrame(sleep)
# except (Exception, psycopg2.Error) as error : 
#     print ("Error", error)
# finally: 
#     if connection:
#         cursor.close()
#         connection.close()
#         print("Connection closed")

# #### Database Setup


# POSTGRES = {
#     'user': "postgres", 
#     'password': "Prav123", 
#     'host': "127.0.0.1",
#     'port': "5432", 
#     'database': "sleepdb",
# }

# #### Flask Setup

# app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))



# # ### Database Setup
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Prav123@localhost:5432/sleepdb'

# # # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db.init_app(app)
#db = SQLAlchemy(app)
# Sleep = create_classes(db)



# create route that renders index.html template
# @app.route("/")
# def home():
#     return render_template("index.html")
#     #return ("hi")


# @app.route('/predict',methods=['POST'])
# def predict():
#     '''
#     For rendering results on HTML GUI
#     '''
#     int_features = [int(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = model.predict(final_features)

#     output = prediction[0]

#     return render_template('index.html', prediction_text='sleep rate {}'.format(output))





# Query the database and send the jsonified results
# @app.route("/send")
# def send():
#     if request.method == "POST":
#         activities = request.form["Activities"]
#         devicesBR = request.form["Devices frequently used in Bedroom"]
#         devicescount = request.form["How many devices do you have in Bedroom?"]
#         usage = request.form["How do you use your devices in bedroom"]
#         Rules = request.form["Bedroom Rules"]
#         enforce = request.form["Do you follow Bedroom Rules"]
#         behaviour = request.form["Filter yours or your child's behaviour during"]
#         rate = request.form["How do you rate yours or child's behaviour today?"]
        

#         sleep = Sleep(activities=activities, devicesBR=devicesBR, devicescount=devicescount, usage=usage, Rules=Rules, enforce=enforce, behaviour=behaviour, rate=rate)
#         db.session.add(sleep)
#         db.session.commit()
#         return redirect("/send", code=302)

#     return render_template("form.html")

# @app.route("/send/api")
# def send_api():

# if (x > 7){
#  {
#     console.log("Good");
#   }
#   else if (x === 5) {
#     console.log("ok");
#   }
#   else {
#     console.log("bad");
#   }
# }
#  return render_template("index.html")
#       """Return result."""
#         #return render_template (ratesleep=ratesleep')



# @app.route("/api/sleep")
# def sleep_api():


#     results = db.session.query(Sleep.activities, Sleep.devicesBR, Sleep.devicescount, Sleep.usage, Sleep.Rules, Sleep.enforce, Sleep.behaviour, Sleep.rate, Sleep.ratesleep).all()

#     activities = [result[0] for result in results]
#     ratesleep = [result[1]for result in results]
#     ratesleep = [result[2] for result in results]




#### below is the test 

# import flask
# from flask import request
# app = flask.Flask(__name__)
# app.config["DEBUG"] = True

# from flask_cors import CORS
# CORS(app)

# @app.route('/send', methods=["GET", "POST"])
# def send_predict():
#     if request.method == "POST":
#     from sklearn.externals import joblib
#     model = joblib.load('sleep_analysis.ml')
#     sleep_predict = model.predict([[int(request.args['activities']),
#                             int(request.args['devicesBR']),
#                             int(request.args['devicescount']),
#                             int(request.args['usage']),
#                             int(request.args['Rules']),
#                             int(request.args['enforce']),
#                             int(request.args['behaviour']),
#                             int(request.args['rate']),
#                            ]])
#     return int(request.args['ratesleep'])
    
    # print(request.args)
    # return render_template("index.html")


# if __name__ == "__main__":
#     app.run(debug=True)

 

if __name__ == "__main__":
    app.run(debug=True)