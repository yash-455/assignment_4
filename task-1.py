try:
    file1 = open('sample.txt','r')
    read_file = file1.read()
    print("Reading file content:")
    print(read_file)
except:
    print("Error: the file sample.txt was not found")