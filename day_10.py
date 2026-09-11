def format_case(f_name,l_name):
    first_formated=f_name.title()
    last_formated=l_name.title()
    name=first_formated + " " + last_formated
    return name
f_name=input("Enter First name : ")
l_name=input("Enter Last name : ")
print(f" You Name in Formated Way is : {format_case(f_name=f_name,l_name=l_name)}")