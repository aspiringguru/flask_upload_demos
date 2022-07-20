"""
d:
cd D:\2020\coding\tam_EC50\June_2022
#setup virtual environment
#python -m venv tam_env
tam_env\Scripts\activate.bat
pip install pandas
pip install openpyxl
pip install matplotlib
pip install UliPlot
#pip install -U plotly

d:
cd D:\2020\coding\tam_EC50\June_2022
tam_env\Scripts\activate.bat
python

#not used.
#pip install -U ggplot
"""
import pandas as pd
import os
import matplotlib.pyplot as plt
from UliPlot.XLSX import auto_adjust_xlsx_column_width

#for initial working demo, load only the first set of data.
#later will search for second set of data, skip blank rows.
#spreadsheets will not have consistant number of blank rows between sets of data.


def process_dataset(dataset, filename_, output_path):
    print("process_dataset: filename_=", filename_)
    #get wavelength from column 14
    wavelength = dataset.loc[:,dataset.columns[-1]].dropna().values[0]
    print("wavelength:", wavelength)
    #-------------------------------------------------------------------------------
    sterility_control = dataset.iloc[3:5, 11:12]
    sterility_control_mean = sterility_control.mean().values[0]
    sterility_control_sem = round(sterility_control.sem().iloc[0], 5)
    print("sterility_control_sem:", sterility_control_sem)
    #-------------------------------------------------------------------------------
    PHMB_01 = dataset.iloc[1:3, 10:11]
    print("PHMB_01:", PHMB_01)
    PHMB_01_mean = PHMB_01.mean().values[0]
    print("PHMB_01_mean:", PHMB_01_mean)
    PHMB_01_sem = round(PHMB_01.sem().iloc[0], 5)
    print("PHMB_01_sem:", PHMB_01_sem)
    #["title", mean, mean-sterility_control_mean, Standard error of mean]
    PHMB_01_row = ["0", PHMB_01_mean, PHMB_01_mean-sterility_control_mean, PHMB_01_sem]
    #
    PHMB_01_2 = dataset.iloc[1:3, 2:3]
    PHMB_01_2
    PHMB_01_2.dtypes
    PHMB_01_2_mean = PHMB_01_2.mean().values[0]
    PHMB_01_2_mean
    PHMB_01_2_sem = round(PHMB_01_2.sem().iloc[0], 5)
    PHMB_01_2_sem
    PHMB_01_2_row = ["1/2", PHMB_01_2_mean, PHMB_01_2_mean-sterility_control_mean, PHMB_01_2_sem]
    #
    PHMB_01_4 = dataset.iloc[1:3, 3:4]
    PHMB_01_4
    PHMB_01_4_mean = PHMB_01_4.mean().values[0]
    PHMB_01_4_mean
    PHMB_01_4_sem = round(PHMB_01_4.sem().iloc[0], 5)
    PHMB_01_4_sem
    PHMB_01_4_row = ["1/4", PHMB_01_4_mean, PHMB_01_4_mean-sterility_control_mean, PHMB_01_4_sem]
    #
    PHMB_01_8 = dataset.iloc[1:3, 4:5]
    PHMB_01_8
    PHMB_01_8_mean = PHMB_01_8.mean().values[0]
    PHMB_01_8_mean
    PHMB_01_8_sem = round(PHMB_01_8.sem().iloc[0], 5)
    PHMB_01_8_sem
    PHMB_01_8_row = ["1/8", PHMB_01_8_mean, PHMB_01_8_mean-sterility_control_mean, PHMB_01_8_sem]
    #
    PHMB_01_16 = dataset.iloc[1:3, 5:6]
    PHMB_01_16
    PHMB_01_16_mean = PHMB_01_16.mean().values[0]
    PHMB_01_16_mean
    PHMB_01_16_sem = round(PHMB_01_16.sem().iloc[0], 5)
    PHMB_01_16_sem
    PHMB_01_16_row = ["1/16", PHMB_01_16_mean, PHMB_01_16_mean-sterility_control_mean, PHMB_01_16_sem]
    #
    PHMB_01_32 = dataset.iloc[1:3, 6:7]
    PHMB_01_32
    PHMB_01_32_mean = PHMB_01_32.mean().values[0]
    PHMB_01_32_mean
    PHMB_01_32_sem = round(PHMB_01_32.sem().iloc[0], 5)
    PHMB_01_32_sem
    PHMB_01_32_row = ["1/32", PHMB_01_32_mean, PHMB_01_32_mean-sterility_control_mean, PHMB_01_32_sem]
    #
    PHMB_01_64 = dataset.iloc[1:3, 7:8]
    PHMB_01_64
    PHMB_01_64_mean = PHMB_01_64.mean().values[0]
    PHMB_01_64_mean
    PHMB_01_64_sem = round(PHMB_01_64.sem().iloc[0], 5)
    PHMB_01_64_sem
    PHMB_01_64_row = ["1/64", PHMB_01_64_mean, PHMB_01_64_mean-sterility_control_mean, PHMB_01_64_sem]
    #
    PHMB_01_128 = dataset.iloc[1:3, 8:9]
    PHMB_01_128
    PHMB_01_128_mean = PHMB_01_128.mean().values[0]
    PHMB_01_128_mean
    PHMB_01_128_sem = round(PHMB_01_128.sem().iloc[0], 5)
    PHMB_01_128_sem
    PHMB_01_128_row = ["1/128", PHMB_01_128_mean, PHMB_01_128_mean-sterility_control_mean, PHMB_01_128_sem]
    #
    PHMB_01_256 = dataset.iloc[1:3, 9:10]
    PHMB_01_256
    PHMB_01_256_mean = PHMB_01_256.mean().values[0]
    PHMB_01_256_mean
    PHMB_01_256_sem = round(PHMB_01_256.sem().iloc[0], 5)
    PHMB_01_256_sem
    PHMB_01_256_row = ["1/256", PHMB_01_256_mean, PHMB_01_256_mean-sterility_control_mean, PHMB_01_256_sem]
    #assemble rows into table & plot
    PHMB_01_row
    PHMB_01_2_row
    PHMB_01_4_row
    PHMB_01_8_row
    PHMB_01_16_row
    PHMB_01_32_row
    PHMB_01_64_row
    PHMB_01_128_row
    PHMB_01_256_row
    #
    dictionary = {
        PHMB_01_row[0]:PHMB_01_row[1:],
        PHMB_01_2_row[0]:PHMB_01_2_row[1:],
        PHMB_01_4_row[0]:PHMB_01_4_row[1:],
        PHMB_01_8_row[0]:PHMB_01_8_row[1:],
        PHMB_01_16_row[0]:PHMB_01_16_row[1:],
        PHMB_01_32_row[0]:PHMB_01_32_row[1:],
        PHMB_01_64_row[0]:PHMB_01_64_row[1:],
        PHMB_01_128_row[0]:PHMB_01_128_row[1:],
        PHMB_01_256_row[0]:PHMB_01_256_row[1:],
    }
    dictionary
    df = pd.DataFrame(dictionary)
    df.index =['mean', 'mean minus sterility control mean', 'standard error of mean']
    df
    df_output = df.transpose().iloc[::-1]
    #df_PHMB_01 is used for final assembled graph
    df_output['mean minus sterility control mean + sem']=df_output['mean minus sterility control mean']+df_output['standard error of mean']
    df_output['mean minus sterility control mean - sem']=df_output['mean minus sterility control mean']-df_output['standard error of mean']
    #title = file_list[0][:file_list[0].index(".")]+" PHMB 0.1%"
    title = filename_[:filename_.index(".xlsx")]+" PHMB 0.1%"
    print("title:", title)
    print("df_output\n", df_output)
    df_output.to_excel(output_path+"/"+title+'_output.xlsx')
    #df_output.drop(['standard error of mean'], axis = 1, inplace=True)
    #df_output.drop(['mean'], axis = 1, inplace=True)
    df_PHMB_01_ = df_output
    #-----
    labels = ['mean minus sterility control mean', 'error bars SEM']
    #labels = list(df_output.columns)
    #
    plt.close()
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.29, top=.91)
    ax.set_title(title)
    ax.set_ylabel("OD "+wavelength)
    ax.set_xlabel('Concentration (Dilutions)')
    ax.tick_params(axis='x', labelrotation = -80)
    l = ax.plot(df_output['mean minus sterility control mean'])
    y_error = df_output['standard error of mean']
    plt.errorbar(list(df_output.index), \
                 list(df_output['mean minus sterility control mean']),  \
                 yerr = y_error,fmt='o',ecolor = 'blue',color='blue')
    fig.legend(l, loc=8, labels=labels)
    #loc=2 = top left corner, loc=8 = 'lower center'
    #plt.show()
    plt.savefig(output_path+"/"+title+'_errorbars.png')
    #---------------------------
    PHMB_02 = dataset.iloc[3:5, 10:11]
    PHMB_02
    PHMB_02_mean = PHMB_02.mean().values[0]
    PHMB_02_mean
    PHMB_02_sem = round(PHMB_02.sem().iloc[0], 5)
    PHMB_02_sem
    PHMB_02_row = ["0", PHMB_02_mean, PHMB_02_mean-sterility_control_mean, PHMB_02_sem]
    #
    PHMB_02_2 = dataset.iloc[3:5, 2:3]
    PHMB_02_2
    PHMB_02_2_mean = PHMB_02_2.mean().values[0]
    PHMB_02_2_mean
    PHMB_02_2_sem = round(PHMB_02_2.sem().iloc[0], 5)
    PHMB_02_2_sem
    PHMB_02_2_row = ["1/2", PHMB_02_2_mean, PHMB_02_2_mean-sterility_control_mean, PHMB_02_2_sem]
    #
    PHMB_02_4 = dataset.iloc[3:5, 3:4]
    PHMB_02_4
    PHMB_02_4_mean = PHMB_02_4.mean().values[0]
    PHMB_02_4_mean
    PHMB_02_4_sem = round(PHMB_02_4.sem().iloc[0], 5)
    PHMB_02_4_sem
    PHMB_02_4_row = ["1/4", PHMB_02_4_mean, PHMB_02_4_mean-sterility_control_mean, PHMB_02_4_sem]
    #
    PHMB_02_8 = dataset.iloc[3:5, 4:5]
    PHMB_02_8
    PHMB_02_8_mean = PHMB_02_8.mean().values[0]
    PHMB_02_8_mean
    PHMB_02_8_sem = round(PHMB_02_8.sem().iloc[0], 5)
    PHMB_02_8_sem
    PHMB_02_8_row = ["1/8", PHMB_02_8_mean, PHMB_02_8_mean-sterility_control_mean, PHMB_02_8_sem]
    #
    PHMB_02_16 = dataset.iloc[3:5, 5:6]
    PHMB_02_16
    PHMB_02_16_mean = PHMB_02_16.mean().values[0]
    PHMB_02_16_mean
    PHMB_02_16_sem = round(PHMB_02_16.sem().iloc[0], 5)
    PHMB_02_16_sem
    PHMB_02_16_row = ["1/16", PHMB_02_16_mean, PHMB_02_16_mean-sterility_control_mean, PHMB_02_16_sem]
    #
    PHMB_02_32 = dataset.iloc[3:5, 6:7]
    PHMB_02_32
    PHMB_02_32_mean = PHMB_02_32.mean().values[0]
    PHMB_02_32_mean
    PHMB_02_32_sem = round(PHMB_02_32.sem().iloc[0], 5)
    PHMB_02_32_sem
    PHMB_02_32_row = ["1/32", PHMB_02_32_mean, PHMB_02_32_mean-sterility_control_mean, PHMB_02_32_sem]
    #
    PHMB_02_64 = dataset.iloc[3:5, 7:8]
    PHMB_02_64
    PHMB_02_64_mean = PHMB_02_64.mean().values[0]
    PHMB_02_64_mean
    PHMB_02_64_sem = round(PHMB_02_64.sem().iloc[0], 5)
    PHMB_02_64_sem
    PHMB_02_64_row = ["1/64", PHMB_02_64_mean, PHMB_02_64_mean-sterility_control_mean, PHMB_02_64_sem]
    #
    PHMB_02_128 = dataset.iloc[3:5, 8:9]
    PHMB_02_128
    PHMB_02_128_mean = PHMB_02_128.mean().values[0]
    PHMB_02_128_mean
    PHMB_02_128_sem = round(PHMB_02_128.sem().iloc[0], 5)
    PHMB_02_128_sem
    PHMB_02_128_row = ["1/128", PHMB_02_128_mean, PHMB_02_128_mean-sterility_control_mean, PHMB_02_128_sem]
    #
    PHMB_02_256 = dataset.iloc[3:5, 9:10]
    PHMB_02_256
    PHMB_02_256_mean = PHMB_02_256.mean().values[0]
    PHMB_02_256_mean
    PHMB_02_256_sem = round(PHMB_02_256.sem().iloc[0], 5)
    PHMB_02_256_sem
    PHMB_02_256_row = ["1/256", PHMB_02_256_mean, PHMB_02_256_mean-sterility_control_mean, PHMB_02_256_sem]
    #--------------
    #assemble rows into table & plot
    dictionary = {
        PHMB_02_row[0]:PHMB_02_row[1:],
        PHMB_02_2_row[0]:PHMB_02_2_row[1:],
        PHMB_02_4_row[0]:PHMB_02_4_row[1:],
        PHMB_02_8_row[0]:PHMB_02_8_row[1:],
        PHMB_02_16_row[0]:PHMB_02_16_row[1:],
        PHMB_02_32_row[0]:PHMB_02_32_row[1:],
        PHMB_02_64_row[0]:PHMB_02_64_row[1:],
        PHMB_02_128_row[0]:PHMB_02_128_row[1:],
        PHMB_02_256_row[0]:PHMB_02_256_row[1:],
    }
    dictionary
    df = pd.DataFrame(dictionary)
    df.index =['mean', 'mean minus sterility control mean', 'standard error of mean']
    df
    df_output = df.transpose().iloc[::-1]#reverses the order of columns
    #df_PHMB_02 is used for final assembled graph
    df_output['mean minus sterility control mean + sem']=df_output['mean minus sterility control mean']+df_output['standard error of mean']
    df_output['mean minus sterility control mean - sem']=df_output['mean minus sterility control mean']-df_output['standard error of mean']
    title = filename_[:filename_.index(".xlsx")]+" PHMB 0.2%"
    print("df_output\n", df_output)
    df_output.to_excel(output_path+"/"+title+'_output.xlsx')
    df_PHMB_02_ = df_output
    #-----
    plt.close()
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.29, top=.91)
    ax.set_title(title)
    ax.set_ylabel("OD "+wavelength)
    ax.set_xlabel('Concentration (Dilutions)')
    ax.tick_params(axis='x', labelrotation = -80)
    l = ax.plot(df_output['mean minus sterility control mean'])
    y_error = df_output['standard error of mean']
    plt.errorbar(list(df_output.index), \
                 list(df_output['mean minus sterility control mean']),  \
                 yerr = y_error,fmt='o',ecolor = 'blue',color='blue')
    fig.legend(l, loc=8, labels=labels)
    #loc=2 = top left corner, loc=8 = 'lower center'
    #plt.show()
    plt.savefig(output_path+"/"+title+'_errorbars.png')
    #---------------------------
    NAC = dataset.iloc[5:7, 10:11]
    NAC
    NAC_mean = NAC.mean().values[0]
    NAC_mean
    NAC_sem = round(NAC.sem().iloc[0], 5)
    NAC_sem
    NAC_row = ["0", NAC_mean, NAC_mean-sterility_control_mean, NAC_sem]
    #
    NAC_2 = dataset.iloc[5:7, 2:3]
    NAC_2
    NAC_2_mean = NAC_2.mean().values[0]
    NAC_2_mean
    NAC_2_sem = round(NAC_2.sem().iloc[0], 5)
    NAC_2_sem
    NAC_2_row = ["1/2", NAC_2_mean, NAC_2_mean-sterility_control_mean, NAC_2_sem]
    #
    NAC_4 = dataset.iloc[5:7, 3:4]
    NAC_4
    NAC_4_mean = NAC_4.mean().values[0]
    NAC_4_mean
    NAC_4_sem = round(NAC_4.sem().iloc[0], 5)
    NAC_4_sem
    NAC_4_row = ["1/4", NAC_4_mean, NAC_4_mean-sterility_control_mean, NAC_4_sem]
    #
    NAC_8 = dataset.iloc[5:7, 4:5]
    NAC_8
    NAC_8_mean = NAC_8.mean().values[0]
    NAC_8_mean
    NAC_8_sem = round(NAC_8.sem().iloc[0], 5)
    NAC_8_sem
    NAC_8_row = ["1/8", NAC_8_mean, NAC_8_mean-sterility_control_mean, NAC_8_sem]
    #
    NAC_16 = dataset.iloc[5:7, 5:6]
    NAC_16
    NAC_16_mean = NAC_16.mean().values[0]
    NAC_16_mean
    NAC_16_sem = round(NAC_16.sem().iloc[0], 5)
    NAC_16_sem
    NAC_16_row = ["1/16", NAC_16_mean, NAC_16_mean-sterility_control_mean, NAC_16_sem]
    #--------------
    #assemble rows into table & plot
    dictionary = {
        NAC_row[0]:NAC_row[1:],
        NAC_2_row[0]:NAC_2_row[1:],
        NAC_4_row[0]:NAC_4_row[1:],
        NAC_8_row[0]:NAC_8_row[1:],
        NAC_16_row[0]:NAC_16_row[1:],
    }
    dictionary
    df = pd.DataFrame(dictionary)
    df.index =['mean', 'mean minus sterility control mean', 'standard error of mean']
    df
    df_output = df.transpose().iloc[::-1]
    #df_NAC is used for final assembled graph
    df_output['mean minus sterility control mean + sem']=df_output['mean minus sterility control mean']+df_output['standard error of mean']
    df_output['mean minus sterility control mean - sem']=df_output['mean minus sterility control mean']-df_output['standard error of mean']
    title = filename_[:filename_.index(".xlsx")]+"_NAC"
    print("df_output\n", df_output)
    df_output.to_excel(output_path+"/"+title+'_output.xlsx')
    df_NAC_ = df_output
    #-----
    plt.close()
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.29, top=.91)
    ax.set_title(title)
    ax.set_ylabel("OD "+wavelength)
    ax.set_xlabel('Concentration (Dilutions)')
    ax.tick_params(axis='x', labelrotation = -80)
    l = ax.plot(df_output['mean minus sterility control mean'])
    y_error = df_output['standard error of mean']
    plt.errorbar(list(df_output.index), \
                 list(df_output['mean minus sterility control mean']),  \
                 yerr = y_error,fmt='o',ecolor = 'blue',color='blue')
    fig.legend(l, loc=8, labels=labels)
    #loc=2 = top left corner, loc=8 = 'lower center'
    #plt.show()
    plt.savefig(output_path+"/"+title+'_errorbars.png')
    #---------------------------
    TRIS = dataset.iloc[5:7, 11:12]
    TRIS
    TRIS_mean = TRIS.mean().values[0]
    TRIS_mean
    TRIS_sem = round(TRIS.sem().iloc[0], 5)
    TRIS_sem
    TRIS_row = ["0", TRIS_mean, TRIS_mean-sterility_control_mean, TRIS_sem]
    #
    TRIS_2 = dataset.iloc[5:7, 6:7]
    TRIS_2
    TRIS_2_mean = TRIS_2.mean().values[0]
    TRIS_2_mean
    TRIS_2_sem = round(TRIS_2.sem().iloc[0], 5)
    TRIS_2_sem
    TRIS_2_row = ["1/2", TRIS_2_mean, TRIS_2_mean-sterility_control_mean, TRIS_2_sem]
    #
    TRIS_4 = dataset.iloc[5:7, 7:8]
    TRIS_4
    TRIS_4_mean = TRIS_4.mean().values[0]
    TRIS_4_mean
    TRIS_4_sem = round(TRIS_4.sem().iloc[0], 5)
    TRIS_4_sem
    TRIS_4_row = ["1/4", TRIS_4_mean, TRIS_4_mean-sterility_control_mean, TRIS_4_sem]
    #
    TRIS_8 = dataset.iloc[5:7, 8:9]
    TRIS_8
    TRIS_8_mean = TRIS_8.mean().values[0]
    TRIS_8_mean
    TRIS_8_sem = round(TRIS_8.sem().iloc[0], 5)
    TRIS_8_sem
    TRIS_8_row = ["1/8", TRIS_8_mean, TRIS_8_mean-sterility_control_mean, TRIS_8_sem]
    #
    TRIS_16 = dataset.iloc[5:7, 9:10]
    TRIS_16
    TRIS_16_mean = TRIS_16.mean().values[0]
    TRIS_16_mean
    TRIS_16_sem = round(TRIS_16.sem().iloc[0], 5)
    TRIS_16_sem
    TRIS_16_row = ["1/16", TRIS_16_mean, TRIS_16_mean-sterility_control_mean, TRIS_16_sem]
    #
    #--------------
    #assemble rows into table & plot
    dictionary = {
        TRIS_row[0]:TRIS_row[1:],
        TRIS_2_row[0]:TRIS_2_row[1:],
        TRIS_4_row[0]:TRIS_4_row[1:],
        TRIS_8_row[0]:TRIS_8_row[1:],
        TRIS_16_row[0]:TRIS_16_row[1:],
    }
    dictionary
    df = pd.DataFrame(dictionary)
    df.index =['mean', 'mean minus sterility control mean', 'standard error of mean']
    df
    df_output = df.transpose().iloc[::-1]
    #df_TRIS is used for final assembled graph
    df_output['mean minus sterility control mean + sem']=df_output['mean minus sterility control mean']+df_output['standard error of mean']
    df_output['mean minus sterility control mean - sem']=df_output['mean minus sterility control mean']-df_output['standard error of mean']
    title = filename_[:filename_.index(".xlsx")]+"_TRIS"
    df_output.to_excel(output_path+"/"+title+'_output.xlsx')
    #df_output.drop(['standard error of mean'], axis = 1, inplace=True)
    #df_output.drop(['mean'], axis = 1, inplace=True)
    df_TRIS_ = df_output
    #-----
    plt.close()
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.29, top=.91)
    ax.set_title(title)
    ax.set_ylabel("OD "+wavelength)
    ax.set_xlabel('Concentration (Dilutions)')
    ax.tick_params(axis='x', labelrotation = -80)
    l = ax.plot(df_output['mean minus sterility control mean'])
    y_error = df_output['standard error of mean']
    plt.errorbar(list(df_output.index), \
                 list(df_output['mean minus sterility control mean']),  \
                 yerr = y_error,fmt='o',ecolor = 'blue',color='blue')
    fig.legend(l, loc=8, labels=labels)
    #loc=2 = top left corner, loc=8 = 'lower center'
    #plt.show()
    plt.savefig(output_path+"/"+title+'_errorbars.png')
    #-------------------------------------------------------------------------------
    #now plot combined graph of the different mediums on same plate.
    df_PHMB_01_.drop(['mean'], axis = 1, inplace=True)
    df_PHMB_01_.drop(['mean minus sterility control mean + sem'], axis = 1, inplace=True)
    df_PHMB_01_.drop(['mean minus sterility control mean - sem'], axis = 1, inplace=True)
    df_PHMB_01_.columns=['PHMB 01', 'PHMB 01 sem']
    df_PHMB_01_
    #
    df_PHMB_02_.drop(['mean'], axis = 1, inplace=True)
    df_PHMB_02_.drop(['mean minus sterility control mean + sem'], axis = 1, inplace=True)
    df_PHMB_02_.drop(['mean minus sterility control mean - sem'], axis = 1, inplace=True)
    df_PHMB_02_.columns=['PHMB 02', 'PHMB 02 sem']
    df_PHMB_02_
    #
    df_NAC_.drop(['mean'], axis = 1, inplace=True)
    df_NAC_.drop(['mean minus sterility control mean + sem'], axis = 1, inplace=True)
    df_NAC_.drop(['mean minus sterility control mean - sem'], axis = 1, inplace=True)
    df_NAC_.columns=['NAC', 'NAC sem']
    df_NAC_
    #
    df_TRIS_.drop(['mean'], axis = 1, inplace=True)
    df_TRIS_.drop(['mean minus sterility control mean + sem'], axis = 1, inplace=True)
    df_TRIS_.drop(['mean minus sterility control mean - sem'], axis = 1, inplace=True)
    df_TRIS_.columns=['TRIS', 'TRIS sem']
    df_TRIS_
    #combine columns together
    #df_combined = pd.DataFrame()
    df_combined = pd.concat([df_PHMB_01_, df_PHMB_02_], ignore_index=False, axis=1)
    df_combined = pd.concat([df_combined, df_NAC_, df_TRIS_], ignore_index=False, axis=1)
    df_combined
    df_combined.columns
    #'PHMB 01', 'PHMB 01 sem', 'PHMB 02', 'PHMB 02 sem', 'NAC', 'NAC sem','TRIS', 'TRIS sem'
    #-------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------
    plt.close()
    title = filename_[:filename_.index(".xlsx")]
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.17, top=.91, right=0.71)
    ax.set_title(title)
    ax.set_ylabel("OD "+wavelength)
    ax.set_xlabel('Concentration (Dilutions)')
    ax.tick_params(axis='x', labelrotation = -80)
    plt.errorbar(list(df_combined.index),
                 list(df_combined['PHMB 01']),
                 yerr = list(df_combined['PHMB 01 sem']),
                 label ='Otoflush 0.1%')
    plt.errorbar(list(df_combined.index),
                 list(df_combined['PHMB 02']),
                 yerr = list(df_combined['PHMB 02 sem']),
                 label ='Otoflush 0.1%')
    plt.errorbar(list(df_combined.index)[4:],
                 list(df_combined['TRIS'][4:]),
                 yerr = list(df_combined['TRIS sem'])[4:],
                 label ='TRIS')
    plt.errorbar(list(df_combined.index)[4:],
                 list(df_combined['NAC'][4:]),
                 yerr = list(df_combined['NAC sem'])[4:],
                 label ='NAC')
    labels=['Otoflush 0.1%', 'Otoflush 0.2%', 'TRIS-EDTA', 'NAC 2%']
    fig.legend(l, loc=7, labels=labels)
    #https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
    #plt.show()
    plt.savefig(output_path+"/"+title+'_all_medium_w_errorbars.png')
    #df_combined.to_excel(output_path+title+'_all_medium_w_errorbars.xlsx')
    print("df_combined\n", df_combined)
    print("title:", title)
    print("writing df_combined to : ", output_path+"/"+title+'_all_medium_w_errorbars.xlsx')
    df_combined.to_excel(output_path+"/"+title+'_all_medium_w_errorbars.xlsx')


"""
#standard error of mean
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sem.html
notes on code.
- data reformatting method is crude, excessively verbose but readable.
- the rounding helps only with intermediate stages to truncate float values for readability.
    underlying issue of float storage remains.
- watch floats carefully during presentation of data.

https://www.statology.org/error-bars-python/
"""
