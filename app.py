#--------- SETTING UP FLASK ----------

#Importing the module and creating 
#app

from flask import Flask
app = Flask(__name__)


#basic route
#it's corresponding request handler

@app.route("/")
def main():
    return "Welcome!"

#Check if executed file is main prog
if __name__ == "__main__":
    app.run()


#---------CREATING HOME PAGE -----------