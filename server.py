#https://www.section.io/engineering-education/how-to-handle-file-uploads-with-flask/
#https://github.com/wobin1/how-to-handle-file-upload-in-flask
#https://github.com/maxcountryman/flask-uploads/blob/master/flask_uploads.py
#pip install flask
#pip install Flask-Reuploaded
#pip install flask_wtf
#https://github.com/maxcountryman/flask-uploads

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, IMAGES, UploadSet

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisasecret'
app.config['UPLOADED_IMAGES_DEST'] = 'uploads/images'

images = UploadSet('images', IMAGES)
configure_uploads(app, images)

class MyForm(FlaskForm):
    image = FileField('image')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    try:
        if form.validate_on_submit():
            print("form.validate_on_submit()=True")
            print("form.image.data:", form.image.data)
            filename = images.save(form.image.data)
            print("filename:", filename)
            return f'Filename: {filename}'
        else:
            print("form.validate_on_submit()=False")
    except Exception as e:
        print("exception start ---------------------------------------------")
        print("exception:"+str(e))
        print("exception end -----------------------------------------------")
    return render_template('index.html', form = form)

if __name__==('__main__'):
    app.run(debug=True)
