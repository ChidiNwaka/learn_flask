import uuid 
from flask import Flask, g, session
from markupsafe import escape

app = Flask(__name__)
app.secret_key = str(uuid.uuid4()) # This generates a random secret key for the session, to be updated with a jwt or similar token

def generate_uuid() -> str:
    return str(uuid.uuid4())

@app.before_request
def assign_uuid():
    print("calling the assign_uuid function first")
    if 'uuid' not in session:
        session['uuid'] = generate_uuid()
    g.uuid = session['uuid']

@app.route("/<name>")
def hello(name):
    return f"hello {escape(name)}!"

@app.route("/")
def hello_world() -> str:
    return "<p>Hello, World!</p>"

@app.route("/admin")
def get_admin() -> dict:
    return { "firstName": "Chidi", "uuid": g.uuid, "lastName": "Nwaka", "role": "Admin", "country": "United States" }

@app.route("/uuid")
def get_uuid() -> str:
    return g.uuid 
