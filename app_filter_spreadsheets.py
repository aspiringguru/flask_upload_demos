"""
d:
cd D:\2020\coding\flask_file_upload_2
flask_file_upload_2_env\Scripts\activate
python app_filter_spreadsheets.py

"""

#input files
#D:\2020\coding\tam_EC50\June_2022\input_files\EX070622
#uploaded files
#D:\2020\coding\flask_file_upload_2\static\uploaded_files


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
from werkzeug.utils import secure_filename
from process_spreadsheet import process_dataset
#

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisasecret'
app.config['UPLOADED_ALL_DEST'] = 'static/uploaded_files'
app.config['MAX_CONTENT_LENGTH'] = 40 * 1024 #max upload filsize in bytes.
output_path = 'static/process_output'
#https://flask.palletsprojects.com/en/2.1.x/config/#MAX_CONTENT_LENGTH
all = UploadSet('all', ALL)
configure_uploads(app, all)


def get_dup_filenames(fname):
    print("start get_dup_filenames, fname:", fname)
    dot_index = fname.rindex(".")
    trunc_uploaded_fname_lower = fname[:dot_index].lower()
    print("trunc_uploaded_fname_lower:", trunc_uploaded_fname_lower)
    _index = fname.rindex("_")
    print("trailing chars after last _:", trunc_uploaded_fname_lower[_index+1:])
    if trunc_uploaded_fname_lower[_index+1:].isnumeric():
        print("fname truncated to remove _xx:", trunc_uploaded_fname_lower[:_index])
        trunc_uploaded_fname_lower = trunc_uploaded_fname_lower[:_index]
    all_files = os.listdir(app.config['UPLOADED_ALL_DEST'])
    all_file_fsizes = []
    print("all_files:\n", all_files)
    existing_fnames = []
    existing_fname_sizes = []
    existing_file_create_times = []
    print("trunc_uploaded_fname_lower:", trunc_uploaded_fname_lower)
    print("trunc_uploaded_fname_lower without _:", trunc_uploaded_fname_lower.replace("_", "").replace(" ", ""))
    for filename in all_files:
        print(filename.lower().replace("_", ""))
        if trunc_uploaded_fname_lower.replace("_", "").replace(" ", "") in filename.lower().replace("_", ""):
            print(filename)
            if filename!=fname:
                existing_fname_size = os.path.getsize(app.config['UPLOADED_ALL_DEST']+"/"+filename)
                existing_fnames.append(filename)
                existing_fname_sizes.append(existing_fname_size)
                existing_file_create_time = time.ctime(os.path.getctime(app.config['UPLOADED_ALL_DEST']+"/"+filename))
                existing_file_create_times.append(existing_file_create_time)
    return existing_fnames, existing_fname_sizes, existing_file_create_times

def load_data_from_file(filename_):
    """
    todo: decide on returning empty dataframes, None objects or ??
    """
    print("load_data_from_file("+filename_+")")
    tabs = pd.ExcelFile( app.config['UPLOADED_ALL_DEST']+"/"+filename_).sheet_names
    data = pd.read_excel(app.config['UPLOADED_ALL_DEST']+"/"+filename_, tabs[0])
    #test shape of data. if not expected shape (ie: at least 7 rows x 15 columns),
    #   dataset1=None, dataset2=None. return empty sets.
    #print(data)
    print ("load_data_from_file : data.shape:", data.shape)
    if data.shape[0]>=8 and data.shape[1]==15:
        dataset1 = data.iloc[0:8, 0:15]
        print("load_data_from_file : dataset1:\n", dataset1)
    elif data.shape[0]<8 and data.shape[1]<15:
        dataset1 = None
        print("load_data_from_file : spreadsheet did not contain data formatting required.")
    #
    if data.shape[0]>8:
        print("load_data_from_file : found second dataset in file")
        for rownum in range(8,data.shape[0]):
            if data.iloc[rownum,:].dropna().size!=0:
                print("load_data_from_file : found start of next dataset within sheet at rownum="+str(rownum))
                break
        dataset2 = data.iloc[rownum+1:data.shape[0], 0:15]
        print("load_data_from_file : dataset2:\n", dataset2)
    else:
        print("load_data_from_file : second dataset not found in file")
        dataset2 = None
    return(dataset1, dataset2)
    #

#copy and modify method process_dataset(dataset, filename_) from process_spreadsheet_new.py
#look at importing from external file since code is long and verbose. (badly structuered!)

class MyForm(FlaskForm):
    all = FileField('all')


@app.route('/delete_similar_filenames')
def delete_similar_filenames():
    form = MyForm()
    #localhost:5000/delete_similar_filenames?original_fname=Ecoli_24h_biofilm_3.xlsx
    #/delete_dup_files?original_fname=xx&filename_to_delete=yyy
    original_fname = request.args.get('original_fname')
    print("get_duplicate_filenames:start")
    dot_index = original_fname.rindex(".")
    truncated_fname = original_fname[:dot_index]
    if "_" in original_fname:
        _index = truncated_fname.rindex("_")
    else:
        _index = len(truncated_fname)
    print("truncated_fname:", truncated_fname)
    print("truncated_fname[_index+1:]:", truncated_fname[_index+1:])
    if truncated_fname[_index+1:].isnumeric():
        print("truncating fname at last _")
        truncated_fname = truncated_fname[:_index]
        print("truncated_fname:", truncated_fname)
    all_files = os.listdir(app.config['UPLOADED_ALL_DEST'])
    truncated_fname_no_ = truncated_fname.replace("_","")
    print("truncated_fname_no_ : ", truncated_fname_no_)
    deleted_file_count = 0
    for filename in all_files:
        temp = filename.replace("_","")
        print("filename:", filename+" : truncated_fname_no_:"+truncated_fname_no_+ "vs temp="+temp)
        if truncated_fname_no_.lower() in temp.lower():
            print("match found, delete this file.")
            os.remove(app.config['UPLOADED_ALL_DEST']+"/"+filename)
            print("deleted")
            deleted_file_count += 1
        else:
            print("match not found")
    # reload original home page and start again.
    return render_template("home_2.html",
                            form = form,
                            deleted_file_count=deleted_file_count,
                            max_file_size = app.config["MAX_CONTENT_LENGTH"] )


@app.route('/process_file')
def process_file():
    file_name = request.args.get('file_name')
    print("route : process_file : file_name=",file_name)
    dataset1, dataset2 = load_data_from_file(file_name)
    print("load_data_from_file("+file_name+") returned dataset1, dataset2")
    print("dataset1:\n", dataset1)
    print("dataset2:\n", dataset2)
    process_dataset(dataset1, file_name, output_path)
    #
    #return "this is route /process_file filesname = {}".format(file_name)
    print("rendering .... file_name:", file_name)
    output_file_name_prefix = file_name[:file_name.rindex(".")]
    return render_template("process_file.html",
                            file_name = file_name,
                            output_file_name_prefix=output_file_name_prefix,
                            dataset1=dataset1,
                            dataset2=dataset2)


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
            return render_template('home_2.html', form = form, err_msg=err_msg, max_file_size = app.config["MAX_CONTENT_LENGTH"])
        elif "pdf" in form.all.data.content_type:
            print("file type is a pdf")
            err_msg = "file submitted is a pdf. please submit a spreadsheet"
            return render_template('home_2.html', form = form, err_msg=err_msg, max_file_size = app.config["MAX_CONTENT_LENGTH"])
        elif "zip" in form.all.data.content_type:
            print(".zip file type detected")
            err_msg = ".zip file type detected. please submit a spreadsheet"
            return render_template('home_2.html', form = form, err_msg=err_msg, max_file_size = app.config["MAX_CONTENT_LENGTH"])
        elif "excel" in form.all.data.content_type or "spreadsheet" in form.all.data.content_type:
            print("file type is a spreadsheet")
        else:
            err_msg = "suitable filetype not identified. please submit a spreadsheet"
            return render_template('home_2.html', form = form, err_msg=err_msg, max_file_size = app.config["MAX_CONTENT_LENGTH"])
        fname = all.save(form.all.data)
        print("\nfname:", fname)
        #print("form.all.data.filename:", form.all.data.filename)
        fsize = os.path.getsize(app.config['UPLOADED_ALL_DEST']+"/"+fname)
        print("fsize = :", fsize)
        #dot_index = form.all.data.filename.rindex(".")
        #trunc_uploaded_fname_lower = form.all.data.filename[:dot_index].lower()
        #print("\ntrunc_uploaded_fname_lower:", trunc_uploaded_fname_lower)
        existing_fnames, existing_fname_sizes, existing_file_create_times = get_dup_filenames(fname)
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
    return render_template('home_2.html', form = form, max_file_size = app.config["MAX_CONTENT_LENGTH"])

if __name__==('__main__'):
    app.run(debug=True)
