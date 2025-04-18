from flask import Flask , render_template, request
from agents.agents import get_data
app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def home_route():
    if request.method =='POST':
        data = request.form["prompt"]
        result = get_data(data)
        return render_template("dummy.html",data=result)
    return render_template("dummy.html",data="")

@app.route("/login")
def login():
    return "This is the login Page"

@app.route("/chat")
def chat():
    return "This is the "

if __name__ == "__main__":
    app.run(debug=True)