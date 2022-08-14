from translate import Translator

path = "/Users/apple/Documents/Python/PyCharm_Project/Python_Scripting/Resources/Text/"
language =  "ja"
tranlator = Translator(to_lang=language)
try:
    with open(path+"simple.txt",mode="r") as my_file:
        text = my_file.read()

        trans = tranlator.translate(text)

        print(trans)
        with open((path+f"{language}_simple.txt"), mode="w") as my_file2:
            my_file2.write(trans)


except:
    print("error")
