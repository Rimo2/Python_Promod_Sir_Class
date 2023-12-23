# File handling
# file_object = open("filename.text",mode)

with open ("TestData.txt", 'r') as file:
    content = file.read()
    print(content)

