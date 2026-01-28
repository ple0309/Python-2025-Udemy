#------- Data Type -----------

# age: int
# name: str
# height: float
# is_human: bool

#It will give hint when age is string from user input.
#Arrow -> for the type of return
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

