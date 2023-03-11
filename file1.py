with open("poems.txt","r") as f:
    if("twinkle" in f.read()):
        print("true")
    else:
        print("false")
    f.close()        
