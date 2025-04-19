from flask import Flask , render_template, request, redirect, url_for
from flask import copy_current_request_context, session
from flask_socketio import SocketIO, send , emit, disconnect
from pymongo import DESCENDING
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from db.config.database import user_collection, chat_collection
from bson.objectid import ObjectId
from ml.rag import rag,context_retrieval
import bson
import re
from db.models.User import User
from agents.agents import get_data, generate_json
from agents.talker import check_data
app = Flask(__name__)
app.secret_key = 'secret!'
socketio = SocketIO(app,cors_allowed_origins="*")

login_manager = LoginManager()
login_manager.init_app(app)

class CurUser(UserMixin):
    def __init__(self,user_data):
        self.id = str(user_data["_id"])
        self.email = str(user_data["email"])
        self.name = user_data["username"]
    
    def get_data(user_id):
        user_data = user_collection.find_one({"_id":ObjectId(user_id)})
        return CurUser(user_data) if user_data else None



@login_manager.user_loader
def user_loader(user_id):
    return CurUser.get_data(user_id)


@socketio.on("my event")
def handle_message(data):
    reply = ""
    if current_user.is_authenticated:
        if data and data["data"]:
            history = []
            hist = chat_collection.find({"user_mail":current_user.email}).sort("_id", DESCENDING).limit(1)
            for h in hist:
                h = bson.decode(h["summary"])
                history.extend(h["chat"])
            query = data["data"]
            reply, history = check_data(query,history)  
            chat_collection.insert_one({"user_mail":current_user.email,"query":query,"response":reply,"summary":bson.encode({"chat":history[-2:]})})
        else:
            reply = "Please Provide some input!"
   
        emit("message",reply)
    else:
        disconnect()

@app.route("/",methods=['POST','GET'])
def home_route():
    if current_user.is_authenticated:
        data = {"button":"<a href=\"/logout\" class=\"sign-in\">Log Out</a>"}
    else:
        data = {"button":"<a href=\"/signup\" class=\"sign-in\">Sign In</a>"}
    return render_template("mainpage.html",data=data)

@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == 'POST':

        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        if (username=='' or password=='' or email==''):
            return redirect(url_for("signup"))
        user = user_collection.find({"email":email})
        user = User(username,password,email)
        user_collection.insert_one(user.to_dict())
        user = user_collection.find_one({"email":email})
        login_user(CurUser(user))
        session["user"] = user["username"]
        print("Inserted ")
        return redirect(url_for("login"))
    return render_template("signup.html",data="")



@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home_route"))
    if request.method =='POST':
        email = request.form["email"]
        password = request.form["password"]
        user = user_collection.find_one({"email":email})
        if user and user["password"] == password:
            login_user(CurUser(user))
            session["user"] = user["username"]
            return redirect(url_for("home_route"))
        return "invalid request"
    return render_template("index.html",data="")

@app.route("/chat")
@login_required
def chat():

    return render_template("dummy.html",data="")



@app.route("/logout")
@login_required
def logout():
    print(current_user)
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    socketio.run(app,debug=True)