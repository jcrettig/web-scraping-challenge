from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo

#Import Scrape py
import scrape_mars.py 

#Create an instance of Flask
mongo = PyMongo(app, url = "mongodb://localhost:27017/mars_app")                      ### not sure what goes at the end

#Route to render index.html template using data from Mongo
@app.route("/")
def home():

    #Find one record of data from the mongo database
    mars_data = mongo.db.collection.find_one()

    #Return template and data
    return render_template("index.html", mars=mars_data)

#Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    # Run the scrape function
    martian_data = scrape_mars.scrape_info()

    #Update the Mongo database using update and upsert=True                           ###since we are using upsert we don't need to delete?
    mongo.db.collecton.update({},martian_data, upsert=True)

    #Redirect back to home page
    return redirect("/")

    if__name__ == "__main__":
        app.run(debug=True)

