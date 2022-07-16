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
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024
#nb x *1024 = x Kb, X * 1024 * 1024 = X MB

images = UploadSet('images', IMAGES)
configure_uploads(app, images)

class MyForm(FlaskForm):
    image = FileField('image')

@app.route('/a', methods=['GET', 'POST'])
def index():
    form = MyForm()
    """
    #print("type(form):", type(form))
    #print("dir(form):", dir(form))
    print("form.data:", form.data)
    print("form.errors:", form.errors)
    print("form.form_errors:", form.form_errors)
    print("form.hidden_tag:", form.hidden_tag)
    print("form.image:", form.image)
    #
    #print("type(form.image):", type(form.image))
    #print("dir(form.image):", dir(form.image))
    print("form.image.type:", form.image.type)
    print("form.image.post_validate:", form.image.post_validate)
    print("form.image.pre_validate:", form.image.pre_validate)
    print("form.image.process_errors:", form.image.process_errors)
    print("form.image.validate:", form.image.validate)
    """
    try:
        if form.validate_on_submit():
            #uploaded files exceeding MAX_CONTENT_LENGTH fail here. error message is empty. 413 error.
            """
            print("form.validate_on_submit()=True")
            print("form.image.data:", form.image.data)
            print("type(form.image.data):", type(form.image.data))
            print("dir(form.image.data):", dir(form.image.data))
            print("form.image.data.filename:", form.image.data.filename)
            print("form.image.data.content_length:", form.image.data.content_length)
            print("form.image.data.mimetype_params:", form.image.data.mimetype_params)
            print("form.image.data.name:", form.image.data.name)
            print("form.image.data.content_type:", form.image.data.content_type)
            """
            if "image" not in form.image.data.content_type:
                return "incorrect file type, not an image."
            filename = images.save(form.image.data)
            print("filename:", filename)#same output as form.image.data.filename but images.save saves file.
            return f'Filename: {filename}'
        else:
            print("form.validate_on_submit()=False")
            return "form.validate_on_submit()=False"
    except Exception as e:
        print("form.validate_on_submit error\nexception start ---------------------------------------------")
        print("exception:"+str(e))
        print("exception end -----------------------------------------------")
    return render_template('index.html', form = form)


if __name__==('__main__'):
    app.run(debug=True)
