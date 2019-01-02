# Assignment calls for me to write a program that uses a dictionary that has existing entries, and
# updates the entries by giving values for any existing keys, as well as allowing the user to add new
# entries for the dictionary

studentDic = {'first name': input('Enter first name:'), 'last name': input('Enter last name:'), 'student_id': input('Enter\
 student_id')}

print("first name:", studentDic['first name'])
print("last name:", studentDic['last name'])
print("student_id:", studentDic['student_id'])

add_more = input("add more to the dictionary? (Y for yes)")
if add_more == "Y" or "y":
    key_to_add = input("Enter a kind of information to add:")
    value_to_add = input("Enter the value for the information to add:")
    studentDic.update({key_to_add: value_to_add})
    print(studentDic)
    add_more = input("Do you have more info to add?").lower()
elif add_more != "Y" or "y":
    print(studentDic)
    print("See you later")

