def formated_name(f_name, l_name):
    """formating the name into title"""
    if f_name == "" or l_name == "":
        return
    return f"{f_name.title()} {l_name.title()}"
print(formated_name(input("what is your first name?"), input("What is your last name?")))

