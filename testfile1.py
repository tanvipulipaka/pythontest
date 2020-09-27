def count():
    filename=input("Enter the file name:")
    numberofwords=0
    fileopen= open("/Users/Tanvi/Desktop/Pythontest/testfile1.py")
    for line in fileopen:
        words=line.split()
        numberofwords=numberofwords+ len(words)
    print("Number of Words:")
    print(numberofwords)    
count()
