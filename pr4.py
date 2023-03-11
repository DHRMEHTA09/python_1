with open("pr4.txt","r") as f:
    text=f.read()
    
text=text.replace("donkey","#####")
with open("pr4.txt","w") as f:
    f.write(text)
   

