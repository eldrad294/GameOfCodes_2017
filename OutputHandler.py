import Constants as const
#
def clear_data_in_file():
    "Write over file / Create new file"
    f = open(const.ROUTE_FILE_PATH, "w+")
    f.close()
#
def write_data(output):
    "Append to file"
    with open(const.ROUTE_FILE_PATH, "a") as my_file:
        my_file.write(output+"\n")

