from pyvis.network import Network

def initialize_connection_matrix(number_of_users):
    connection_matrix = [[0 for j in range(number_of_users)]for i in range(number_of_users)]
    print(connection_matrix)
    return connection_matrix

def sort_users_by_their_responses(got_data, column_names, name_col_title):
    ValueBucket = dict()
    for index, row in got_data.iterrows():
        for columnname1 in column_names:
            if columnname1 == name_col_title:
                continue
            candidates_in_this_column_value = set()
            if row[columnname1] in ValueBucket:
                candidates_in_this_column_value = ValueBucket[row[columnname1]]
            candidates_in_this_column_value.add(row[name_col_title])
            ValueBucket[row[columnname1]] = candidates_in_this_column_value
    print(ValueBucket)
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
    #got_net.force_atlas_2based()
    got_net.barnes_hut(gravity=-80000, central_gravity=0.3, spring_length=250, spring_strength=0.001, damping=0.09, overlap=0)

    for k,v in UserName_to_index.items():
        got_net.add_node(v, label=k, title=k)

    for k,v in ValueBucket.items():
        for i in v:
            for j in v:
                if i != j:
                    got_net.add_edge(UserName_to_index[i], UserName_to_index[j], value=connection_matrix[UserName_to_index[i]][UserName_to_index[j]]/2)
                    got_net.add_edge(UserName_to_index[j], UserName_to_index[i], value=connection_matrix[UserName_to_index[j]][UserName_to_index[i]]/2)
    got_net.show('nx.html')