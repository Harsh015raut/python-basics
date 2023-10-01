letter = '''Dear <|Name|>,
You are selected!
Date:<|Date|>
 '''
name = input("Enter Your Name:")
date = input("Enter Date:")
letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)
print(letter)
