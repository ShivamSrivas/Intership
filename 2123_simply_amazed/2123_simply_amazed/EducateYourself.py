from flask import Flask,render_template,request,json,jsonify
import Database
from Database import MongoDB
insert_data=MongoDB.database()




app=Flask(__name__)
@app.route("/",methods=['GET'])
def main():
    return render_template("index.html")

@app.route("/Contact",methods=["Get"])
def Input():
    if request.method=="GET":
        name=str(request.form["name"])
        email=str(request.form['email'])
        message=str(request.form['message'])
        insert_data.insert({email:[email,message]})
    return "Thank you"

if __name__=="__main__":
    app.run(debug=True,port=4998)
