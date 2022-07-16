#https://github.com/wobin1/how-to-handle-file-upload-in-flask/blob/master/app/app.py
#https://www.section.io/engineering-education/how-to-handle-file-uploads-with-flask/
#https://tedboy.github.io/flask/generated/generated/werkzeug.FileStorage.html

import pandas as pd
from flask import Flask, request
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, ALL, UploadSet
import os
import time
#https://flask-uploads.readthedocs.io/en/latest/#upload-sets
import matplotlib.pyplot as plt
from UliPlot.XLSX import auto_adjust_xlsx_column_width

#

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisasecret'
app.config['UPLOADED_ALL_DEST'] = 'static/uploaded_files'
app.config['MAX_CONTENT_LENGTH'] = 40 * 1024 #max upload filsize in bytes.
#https://flask.palletsprojects.com/en/2.1.x/config/#MAX_CONTENT_LENGTH
all = UploadSet('all', ALL)
configure_uploads(app, all)


class MyForm(FlaskForm):
    all = FileField('all')

@app.route('/process_file')
def process_file():
    file_name = request.args.get('file_name')
    return "this is route /process_file filesname = {}".format(file_name)


@app.route('/', methods=['POST', 'GET'])
def home():
    form = MyForm()
    if form.validate_on_submit():
        print("form.validate_on_submit() = True")
        print("type(form.all.data):", type(form.all.data))
        print("dir(form.all.data):", dir(form.all.data))
        print("form.all.data.content_length:", form.all.data.content_length)
        print("form.all.data.content_type:", form.all.data.content_type)
        print("form.all.data.filename:", form.all.data.filename)
        print("form.all.data.headers:", form.all.data.headers)
        print("\ntype(form.all.data.headers):", type(form.all.data.headers))
        print("dir(form.all.data.headers):", dir(form.all.data.headers))
        print("form.all.data.mimetype:", form.all.data.mimetype)
        print("form.all.data.mimetype_params:", form.all.data.mimetype_params)
        print("form.all.data.name:", form.all.data.name)
        if "image" in form.all.data.content_type:
            print("file type is an image")
            err_msg = "file submitted is an image. Please submit a spreadsheet"
            return render_template('home_2.html', form = form, err_msg=err_msg)
        elif "pdf" in form.all.data.content_type:
            print("file type is a pdf")
            err_msg = "file submitted is a pdf. please submit a spreadsheet"
            return render_template('home_2.html', form = form, err_msg=err_msg)
        elif "zip" in form.all.data.content_type:
            print(".zip file type detected")
            err_msg = ".zip file type detected. please submit a spreadsheet"
            return render_template('home_2.html', form = form, err_msg=err_msg)
        elif "excel" in form.all.data.content_type or "spreadsheet" in form.all.data.content_type:
            print("file type is a spreadsheet")
        else:
            err_msg = "suitable filetype not identified. please submit a spreadsheet"
            return render_template('home_2.html', form = form, err_msg=err_msg)
        fname = all.save(form.all.data)
        print("fname:", fname)
        fsize = os.path.getsize(app.config['UPLOADED_ALL_DEST']+"/"+fname)
        print("fsize = :", fsize)
        all_files = os.listdir(app.config['UPLOADED_ALL_DEST'])
        all_file_fsizes = []
        print("all_files:\n", all_files)
        existing_fnames = []
        existing_fname_sizes = []
        existing_file_create_times = []
        dot_index = form.all.data.filename.rindex(".")
        existing_fname = form.all.data.filename[:dot_index].lower()
        print("existing_fname:", existing_fname)
        print("existing_fname without _:", existing_fname.replace("_", "").replace(" ", ""))
        for filename in all_files:
            print(filename.lower().replace("_", ""))
            if existing_fname.replace("_", "").replace(" ", "") in filename.lower().replace("_", ""):
                print(filename)
                if filename!=fname:
                    existing_fname_size = os.path.getsize(app.config['UPLOADED_ALL_DEST']+"/"+filename)
                    existing_fnames.append(filename)
                    existing_fname_sizes.append(existing_fname_size)
                    existing_file_create_time = time.ctime(os.path.getctime(app.config['UPLOADED_ALL_DEST']+"/"+filename))
                    existing_file_create_times.append(existing_file_create_time)
        #create dataframe using existing_fnames & existing_fname_sizes
        df_existing_files = pd.DataFrame(list(zip(existing_fnames, existing_fname_sizes, existing_file_create_times)),
            columns =['existing_fnames', 'file size', 'file date-time created'])
        print("df_existing_files:\n", df_existing_files)
        print("existing_fnames:", existing_fnames)
        #return f'Name of file: {fname}'
        return render_template('uploaded_1.html',
            fname=fname,
            fsize=fsize,
            column_names=df_existing_files.columns.values,
            row_data=list(df_existing_files.values.tolist()), zip=zip,
            df_existing_files=df_existing_files,
            existing_fnames=existing_fnames)
        #nb: saves to dir configured in app.config['UPLOADED_ALL_DEST']
        #
    print("form.validate_on_submit() = False")
    return render_template('home_2.html', form = form)

if __name__==('__main__'):
    app.run(debug=True)
