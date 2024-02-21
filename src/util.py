def read_write_file(file_name, mode, data=None):
    with open(file_name, mode) as file:
        if data:
            file.write(data)
            return
        data = file.readlines()
        return data
