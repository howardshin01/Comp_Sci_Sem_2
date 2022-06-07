x = 0 
y = 1 
name = input("Enter first and last name:")
for i in range(0,len(name)): 
    if(name[x:y] == " "): 
        print(name[x:len(name)]) 
        print(name[0:x]) 
        break
    x = x + 1 
    y = y + 1 
