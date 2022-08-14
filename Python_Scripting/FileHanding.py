path = "/Users/apple/Documents/Python/PyCharm_Project/Python_Scripting/Resources/Text/simple.txt"

'''  # Reading file im sample way

my_file = open(path)
print("Reading the text...")
# print(my_file.readline())
# my_file.close()
print(my_file.read())
'''
# Here no need to close file function
try:
    with open(path, mode="w+") as my_file:
        my_file.write("In the Settings/Preferences dialog ( Ctrl+Alt+S ) \n,"
                      " go to Editor | General (Mouse Control section). \n"
                      " Select the Change font size with Ctrl+Mouse Wheel in option."
                      " Return to the editor, press and hold Ctrl ,"
                      " and using the mouse wheel, adjust the font size")
        print(my_file.readline())
except FileNotFoundError as error:
    print(error)
