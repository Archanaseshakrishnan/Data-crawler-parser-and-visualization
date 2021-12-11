from Data_parser import *
from Data_visualization import *
from Data_crawler import *

def print_stats(number_of_users, name_col_title, column_names, UserName_to_index, connection_matrix, ValueBucket):
    print("Stats: ")
    print("Number_of_users: "+str(number_of_users))
    print("Column titles: "+str(column_names))
    print("Usernames column name: "+name_col_title)
    print("Username -> index: ")
    print(UserName_to_index)
    Users = []
    for k,v in UserName_to_index.items():
        Users.append(k)
    Users.sort()
    print(Users)
    print("--------------------------------------------------------------------------")
    print("Value Bucket: ")
    for k,v in ValueBucket.items():
        print(k+" : "+str(v))
    print("--------------------------------------------------------------------------")
    print("Connected neighbors: ")
    for i in range(0,len(connection_matrix)):
        StringBuilder = "{" + Users[i] + " -> "
        for j in range(0,len(connection_matrix[0])):
            if connection_matrix[i][j] != 0:
                StringBuilder += Users[j] + ":" + str(connection_matrix[i][j]) + ", "
        print(StringBuilder+"}")
    print("--------------------------------------------------------------------------")
    print("Unconnected neighbors: ")
    for i in range(0,len(connection_matrix)):
        StringBuilder = "{" + Users[i] + "-> "
        for j in range(0,len(connection_matrix[0])):
            if connection_matrix[i][j] == 0 and i != j:
                StringBuilder += Users[j] + ":" + str(connection_matrix[i][j]) + ", "
        print(StringBuilder+"}")

def main():
    #crawler_main()
    got_data, number_of_users, name_col_title, column_names, UserName_to_index = parser_main()
    connection_matrix, ValueBucket = form_connection_matrix(got_data, number_of_users, name_col_title, column_names, UserName_to_index)
    print_stats(number_of_users, name_col_title, column_names, UserName_to_index, connection_matrix, ValueBucket)
    generate_graph(connection_matrix, ValueBucket, UserName_to_index)

main()