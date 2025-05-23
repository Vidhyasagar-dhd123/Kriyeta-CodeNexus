from flask import Flask , render_template, request, redirect, url_for
from flask import copy_current_request_context, session
from flask_socketio import SocketIO, send , emit, disconnect
from pymongo import DESCENDING, ASCENDING
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from db.config.database import user_collection, chat_collection
from bson.objectid import ObjectId
from ml.rag import rag,context_retrieval
import bson
from db.models.User import User
from agents.agents import get_data, generate_json
from agents.talker import check_data, get_tool
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


@socketio.on("message")
def handle_message(data):
    reply = ""
    if current_user.is_authenticated:
        print(data["data"])
        if data and data["data"]:
            tool = get_tool("What tool this sentence calling : "+str(data["data"]))
            print(tool)
            if 'HYPERTENSION' in tool:
                emit("check",['STRESS','AGE','CHOLESTROLE','HIGHBP','MENTALHEALTH'])
            elif 'DIABETES' in tool:
                emit("check",['Age','Sex','HighChol','CholCheck','BMI','Smoker','HeartDisease','PhysicalActivity','Fruits','Veggies','HvyAlchohol','GenHlth','MentHlth','PhysHlth','DiffWalk','Stroke','HighBP'])
            else:
                history = []
                hist = chat_collection.find({"user_mail":current_user.email}).sort("_id", DESCENDING).limit(20)
                for h in hist:
                    h = bson.decode(h["summary"])
                    history.extend(h["chat"])
                query = data["data"]
                reply, history = check_data(query,history)  
                chat_collection.insert_one({"user_mail":current_user.email,"query":query,"response":reply,"summary":bson.encode({"chat":history[-2:]})})
        else:
            reply = "Please Provide some input!"
   
        emit("message",{"data":reply})
    else:
        disconnect()


tools = ['diseaseCheck','getSuggestion']


@socketio.on("typing")
def handleTyping(data:str):
    if data.startswith('@'):
        for tool in tools:
            if data.replace('@','').lower() in tool.lower():
                emit("suggestion",'@'+str(tool))
                break
            else:
                emit("suggestion","")
    else:
        emit("suggestion","")
            



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
    history = []
    hist = chat_collection.find({"user_mail":current_user.email}).sort("_id", ASCENDING).limit(20)
    html = ""
    for h in hist:
        html +=f"<div class=\"message user\">"\
      "<img src=\"data:image/jpeg;base64,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\" class=\"avatar\" />"\
      "<div class=\"text\">{}</div>"\
    "</div><div class=\"message bot\">"\
      "<img src=\"data:image/jpeg;base64,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\" class=\"avatar\" />"\
      "<div class=\"text\">{} </div>"\
    "</div>".format(h["query"],h["response"])
    return render_template("chat.html",data=html)



@app.route("/logout")
@login_required
def logout():
    print(current_user)
    logout_user()
    return redirect(url_for("login"))

@socketio.on("sendData")
def handle_check(data):
    print("working")
    data = [float(d) for d in data]
    model = load_model("./logistic_model_diabetes.pkl")
    pred = model.predict(data)
    print(pred)
    emit("message",{"data":pred})

@app.route("/rag")
def rag_ret():
    return rag("What is diabetes")
if __name__ == "__main__":
    socketio.run(app,debug=True)