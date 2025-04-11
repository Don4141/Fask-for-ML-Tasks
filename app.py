from flask import Flask, render_template
from pyngrok import ngrok
import threading

app = Flask(__name__, template_folder="templates", static_folder="static")
port = 5000

@app.route("/")
def home():
    return render_template("index.html")

# Function to run the app
def run_app():
    app.run()

# Open an ngrok tunnel to the HTTP server
public_url = ngrok.connect(port).public_url
print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))

# Update any base URLs to use the public ngrok URL
app.config["BASE_URL"] = public_url

# Start Flask app in a thread
thread = threading.Thread(target=run_app)
thread.start()
