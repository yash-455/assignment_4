try:
    file2 = open('output.txt','w')
    f_write = file2.write(input("Enter text to write in the file: "))
    print("data successfully written to output.txt")
except:
    print("output.txt file does not found.")


try:
    file2 = open('output.txt','a')
    f_append = file2.write("\n" + input("Enter the data to add in the file: "))
    print("data successfull appended to output.txt file.")
except:
    print("output.txt file does not found.")
    

try:
    file2 = open('output.txt','r')
    f_read = file2.read()
    print("Final content of the file is: 1")
    print(f_read)
except:
    print("output.txt file does not found.")