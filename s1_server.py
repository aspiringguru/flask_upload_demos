# (A) INIT
# (A1) LOAD MODULES
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

# (A2) FLASK SETTINGS + INIT
app = Flask(__name__)
HOST_NAME = "localhost"
HOST_PORT = 80
app.config["UPLOAD_FOLDER"] = "uploads/"
# app.debug = True

# (B) HTML UPLOAD PAGE
@app.route("/")
def index():
  return render_template("s2_upload.html")

# (C) UPLOAD HANDLER
@app.route("/upload", methods = ["POST"])
def save_upload():
  if request.method == "POST":
    print("request.method == 'POST' = True")
    f = request.files["file"]
    filename = secure_filename(f.filename)
    print("filename:", filename)
    f.save(app.config["UPLOAD_FOLDER"] + filename)
  return "UPLOAD OK"

# (D) START
if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT)


#todo: call toll road company, pay for tams car over gateway bridge.
