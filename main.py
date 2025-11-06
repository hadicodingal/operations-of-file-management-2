with open("data.txt","w") as f:
    f.write("I am Hadi\n")
    f.write("i am 10\n")
with open("data.txt","r") as f:
    data=f.readlines()
    print (data)
    for i in data:
        word=i.split()
        print (word)
