import uuid 
from flask import Flask
from markupsafe import escape

def generate_uuid() -> str:
    return uuid.uuid4()

app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    return f"hello {escape(name)}!"

@app.route("/")
def hello_world() -> str:
    return "<p>Hello, World!</p>"

@app.route("/admin")
def get_admin() -> dict:
    return { "firstName": "Chidi", "uuid": get_uuid(), "lastName": "Nwaka", "role": "Admin", "country": "United States" }

@app.route("/uuid")
def get_uuid() -> str:
    return str(generate_uuid())
