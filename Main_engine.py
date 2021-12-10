from Data_parser import *
from Data_visualization import *
from Data_crawler import *

def main():
    crawler_main()
    got_data, number_of_users, name_col_title, column_names, UserName_to_index = parser_main()
    print(number_of_users, column_names, name_col_title, UserName_to_index)
    connection_matrix, ValueBucket = form_connection_matrix(got_data, number_of_users, name_col_title, column_names, UserName_to_index)
    generate_graph(connection_matrix, ValueBucket, UserName_to_index)

main()