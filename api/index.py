from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask on Vercel!"

# expose app for Vercel
# Vercel looks for 'app' in the file
