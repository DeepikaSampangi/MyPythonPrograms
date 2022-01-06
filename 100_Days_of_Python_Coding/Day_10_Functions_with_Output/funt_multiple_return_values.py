def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return
    formated_fname = f_name.title()
    formated_lname = l_name.title()
    return formated_fname, formated_lname


print(format_name("deepika", "deepIkA"))
