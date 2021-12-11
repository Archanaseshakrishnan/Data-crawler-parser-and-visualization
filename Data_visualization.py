from os import listdir
import re
import numpy as np
from pyvis.network import Network

def initialize_connection_matrix(number_of_users):
    connection_matrix = [[0 for j in range(number_of_users)]for i in range(number_of_users)]
    #print(connection_matrix)
    return connection_matrix

def sort_users_by_their_responses(got_data, column_names, name_col_title):
    ValueBucket = dict()
    for index, row in got_data.iterrows():
        for columnname1 in column_names:
            if columnname1 == name_col_title:
                continue
            elif row[columnname1] is np.nan:
                continue
            else:
                candidates_in_this_column_value = set()
                if row[columnname1] in ValueBucket:
                    candidates_in_this_column_value = ValueBucket[row[columnname1]]
                candidates_in_this_column_value.add(row[name_col_title])
                ValueBucket[row[columnname1]] = candidates_in_this_column_value
    #print(ValueBucket)
    total_entrees = 0
    for k,v in ValueBucket.items():
        for j in v:
            total_entrees += 1
    print(total_entrees)
    return ValueBucket

def form_connection_matrix(got_data, number_of_users, name_col_title, column_names, UserName_to_index):
    connection_matrix = initialize_connection_matrix(number_of_users)
    ValueBucket = sort_users_by_their_responses(got_data, column_names, name_col_title)
    for k,v in ValueBucket.items():
        for i in v:
            for j in v:
                if i != j:
                    connection_matrix[UserName_to_index[i]][UserName_to_index[j]] += 1
                    connection_matrix[UserName_to_index[j]][UserName_to_index[i]] += 1
    return connection_matrix, ValueBucket

def generate_graph(connection_matrix, ValueBucket, UserName_to_index):
    got_net = Network(height='100%', width='100%', bgcolor='#222222', font_color='white')
    #got_net.force_atlas_2based(spring_length=1000, spring_strength=0.001, gravity=-80000, central_gravity=0.3, damping=0.09, overlap=0)
    got_net.barnes_hut(gravity=-80000, central_gravity=0.3, spring_length=300, spring_strength=0.001, damping=0.09, overlap=0)
    base_path = r"C:\Users\archanr\OneDrive - Synopsys, Inc\Desktop\I&D Taskforce members\\"
    image_list = listdir(base_path)
    #print(image_list)
    for k,v in UserName_to_index.items():
        pattern = r"\w*"+k+"\w*"
        #print(pattern)
        file_re = re.compile(pattern)
        filtered_files = [x for x in image_list if file_re.match(x)]
        if len(filtered_files) == 0:
            got_net.add_node(v, label=k, value=50)
        else:
            got_net.add_node(v, label=k, title=k, shape='image', image=base_path+filtered_files[0], size=30)
    #title=k,
    for k,v in ValueBucket.items():
        for i in v:
            for j in v:
                if i != j:
                    got_net.add_edge(UserName_to_index[i], UserName_to_index[j], value=connection_matrix[UserName_to_index[i]][UserName_to_index[j]]/2)
                    got_net.add_edge(UserName_to_index[j], UserName_to_index[i], value=connection_matrix[UserName_to_index[j]][UserName_to_index[i]]/2)
    got_net.show('nx.html')