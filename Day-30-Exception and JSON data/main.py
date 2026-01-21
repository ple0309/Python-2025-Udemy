# with open("a_file.txt") as file:
#     file.read()

#------------------------- #KeyError ------------------------
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]

#------------------------- #IndexError ----------------------
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#------------------------- #TypeError -----------------------
# text = "abc"
# print(text + 5)

#-----------------try, except, else, finally-----------------
# #FileNotFound
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["sdfadf"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
#
# #else will work when try run successfully
# #Setting up print(a_dictionary["key"] in try block to see.
# else:
#     content = file.read()
#     print(content)
#
# #finally will run no matter what happen
# finally:
#     file.close()
#     print("File was closed.")

#--------------------- raise -------------------------------
height = float(input("Height: "))
weight = int(input("Weight: "))

#ValueError will run when input value is wrong
if height > 3:
    raise ValueError("Human Height should not be over 3 meter.")

bmi = weight / height ** 2
print(bmi)