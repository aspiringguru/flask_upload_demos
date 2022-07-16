#https://github.com/wobin1/how-to-handle-file-upload-in-flask/blob/master/app/app.py
#https://www.section.io/engineering-education/how-to-handle-file-uploads-with-flask/
#https://tedboy.github.io/flask/generated/generated/werkzeug.FileStorage.html

from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, ALL, UploadSet
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisasecret'
app.config['UPLOADED_ALL_DEST'] = 'static/uploaded_files'

all = UploadSet('all', ALL)
configure_uploads(app, all)


class MyForm(FlaskForm):
    all = FileField('all')

@app.route('/', methods=['POST', 'GET'])
def home():
    form = MyForm()
    if form.validate_on_submit():
        print("form.validate_on_submit() = True")
        print("type(form.all.data):", type(form.all.data))
        print("dir(form.all.data):", dir(form.all.data))
        print("form.all.data.content_length:", form.all.data.content_length)
        print("form.all.data.content_type:", form.all.data.content_type)
        if "image" in form.all.data.content_type:
            print("file type is an image")
        elif "pdf" in form.all.data.content_type:
            print("file type is a pdf")
        elif "excel" in form.all.data.content_type:
            print("file type is a spreadsheet")
        elif "spreadsheet" in form.all.data.content_type:
            print("file type is a spreadsheet")
        print("form.all.data.filename:", form.all.data.filename)
        print("form.all.data.headers:", form.all.data.headers)
        print("type(form.all.data.headers):", type(form.all.data.headers))
        print("dir(form.all.data.headers):", dir(form.all.data.headers))
        print("form.all.data.mimetype:", form.all.data.mimetype)
        print("form.all.data.mimetype_params:", form.all.data.mimetype_params)
        print("form.all.data.name:", form.all.data.name)
        fname = all.save(form.all.data)
        print("fname:", fname)
        print("filesize = :", os.path.getsize(app.config['UPLOADED_ALL_DEST']+"/"+fname))
        return f'Name of file: {fname}'
        #nb: saves to dir configured in app.config['UPLOADED_ALL_DEST']
        #
    print("form.validate_on_submit() = False")
    return render_template('home.html', form = form)

if __name__==('__main__'):
    app.run(debug=True)
