
text = "Yooooo\nThis is some text\nHave a good one\n"
text2 = "Have a nice day! See ya"

with open('Jest.txt','w') as file:
    file.write(text)
with open('Jest.txt','a') as file:
    file.write(text2)
