#from pip import main
#main(['install', '-U', 'flask_pymongo'])


from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo

#Import Scrape py
import scrape_mars
from config import mongodbpassword
print(mongodbpassword)
# Create an instance of Flask
app = Flask(__name__)

#Use PyMongo to establish Mongo Connection
# mongo = PyMongo(app, uri = f"mongodb+srv://jcrettig:{mongodbpassword}@cluster0.3ttox.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")                      
app.config["MONGO_URI"] = f"mongodb+srv://jcrettig:{mongodbpassword}@cluster0.3ttox.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongo = PyMongo(app)
#Route to render index.html template using data from Mongo
@app.route("/")
def home():

    #Find one record of data from the mongo database
    mars_data = mongo.db.mars_app.find_one()
    
    #Return template and data
    return render_template("index.html", mars=mars_data)   

#Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    # Run the scrape function
    martian_data = scrape_mars.scrape_all()

    #Update the Mongo database using update and upsert=True                         
    mongo.db.mars_app.update({},martian_data, upsert=True)

    #Redirect back to home page
    return redirect("/")

    
if __name__ == "__main__":
    app.run(debug=True)

    

