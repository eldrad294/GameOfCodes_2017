import src.Constants as const
#
def clear_data_in_file(ROUTE_FILE_PATH):
    "Write over file / Create new file"
    f = open(ROUTE_FILE_PATH, "w+")
    f.close()
#
def write_data(ROUTE_FILE_PATH, output):
    "Append to file"
    with open(ROUTE_FILE_PATH, "a") as my_file:
        my_file.write(output+"\n")

