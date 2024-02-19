def write_to_template(code, line, data):
    for i in range(1, len(data) + 1):
        if i == line:
            data.insert(line, f"{code}\n")
            data.insert(line + 1, " \n")

    with open("template.c", "w") as template:
        template.write("".join(data))
