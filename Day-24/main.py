## READING FILES
# #####First way to open file and including file.close()
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
#
# #Free resource
# file.close()

##READING FILES
# ####Second way we don't need to remember file.close()
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)



##WRITING FILES
#Note open("my_file.txt") read only mode, so I need to setting up its mode.
# 'w' for writing, 'a' for append
with open("my_file.txt", mode="a") as file:
    file.write("\nNew Text.")
