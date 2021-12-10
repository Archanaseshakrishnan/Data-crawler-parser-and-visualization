import pandas as pd
import re
from os import listdir
from os.path import isfile, join

#https://form.jotform.com/archanr/get_to_know_us_form

def read_crawled_data():
    abs_path = r"<your file path>"
    onlyfiles = [f for f in listdir(abs_path) if isfile(join(abs_path, f))]
    file_re = re.compile(r'^Get_to_know_us_form\d{4}-\d{2}-\d{2}_\d{2}_\d{2}_\d{2}.csv$')
    filtered_files = [ x for x in onlyfiles if file_re.match(x)]
    sorted_files = sorted(filtered_files,reverse=True)
    got_data = pd.read_csv(abs_path+"\\"+sorted_files[0])
    return got_data

def preprocess_crawled_data(got_data):
    got_data.columns = got_data.columns.str.replace(' ','_')
    got_data.columns = got_data.columns.str.replace(':','')
    got_data.columns= got_data.columns.str.lower()
    got_data = got_data.dropna(thresh=len(got_data.columns)-2)
    return got_data

def generate_column_names_and_users_list(got_data):
    column_names = []
    UserName_to_index = {}
    name_col_title = ""
    for (columnName, columnData) in got_data.iteritems():
        if columnName == 'Date':
            continue
        column_names.append(columnName)
        if columnName.find('name') != -1:
            name_col_title = columnName
            Users = list(set(columnData))
            Users.sort()
            uindex = 0
            for user in Users:
                if user == None or user == " " or user == '':
                    continue
                UserName_to_index[user] = uindex
                uindex += 1
    print(column_names)
    print(UserName_to_index)
    return name_col_title, column_names, UserName_to_index

def postprocess_crawled_data(got_data, name_col_title):
    got_data = got_data.dropna(subset=[name_col_title])
    return got_data

def parser_main():
    got_data = read_crawled_data()
    got_data = preprocess_crawled_data(got_data)
    name_col_title, column_names, UserName_to_index = generate_column_names_and_users_list(got_data)
    number_of_users = len(UserName_to_index)
    got_data = postprocess_crawled_data(got_data, name_col_title)
    return got_data, number_of_users, name_col_title, column_names, UserName_to_index

#parser_main()
