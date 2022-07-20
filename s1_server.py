# this will not create new filename for duplicate file uploads.
# (A) INIT
# (A1) LOAD MODULES
#pip freeze | findstr Werkzeug = Werkzeug==2.1.2
from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
from werkzeug.exceptions import *

# (A2) FLASK SETTINGS + INIT
app = Flask(__name__)
HOST_NAME = "localhost"
HOST_PORT = 80
app.config['SECRET_KEY'] = 'thisisasecret'
app.config["UPLOAD_FOLDER"] = "uploads/"
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024
#nb x *1024 = x Kb, X * 1024 * 1024 = X MB
app.debug = True

# (B) HTML UPLOAD PAGE
@app.route("/")
def index():
  return render_template("s2_upload.html", max_file_size = app.config["MAX_CONTENT_LENGTH"])

# (C) UPLOAD HANDLER
@app.route("/upload", methods = ["POST"])
def save_upload():
    try:
      if request.method == "POST":
        print("request.method == 'POST' = True")
        f = request.files["file"]
        print("type(f):", type(f))
        #print("f.stream.seek(0,2):", f.stream.seek(0,2))#returns filesize in bytes, causes .save to fail. zero filesize.
        #print("f.seek(0,2):", f.seek(0,2))#returns filesize in bytes, causes .save to fail. zero filesize.
        #print("f.tell():", f.tell())#returns filesize as zero, .save still works.
        #print("f.stream.tell():", f.stream.tell())#returns filesize as zero, .save still works.
        print("dir(f)\n", dir(f))
        print("f.content_length:", f.content_length)
        print("f.content_type:", f.content_type)
        print("f.filename:", f.filename)
        print("f.mimetype:", f.mimetype)
        print("f.mimetype_params:", f.mimetype_params)
        print("f.name:", f.name)
        print("type(f.headers):", type(f.headers))
        filename = secure_filename(f.filename)
        print("filename:", filename)
        f.save(app.config["UPLOAD_FOLDER"] + filename)
      return "UPLOAD OK"
    except RequestEntityTooLarge as e:
        print("error: ", str(e))
        print("type(e):", type(e))
        return "exception RequestEntityTooLarge caught.<br>" + str(e)
    except Exception as e:
        print("error in /upload: ", str(e))
        print("type(e):", type(e))
        flash('error in /upload')
        return "error in /upload: " + str(e)

# (D) START
if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT, debug=True)


#todo: call toll road company, pay for tams car over gateway bridge.
