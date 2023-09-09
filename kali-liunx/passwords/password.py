def kaga():
    user = input("new-user-name : ")
    print("save-new-user-name")
    password = input("new-password : ")
    print("save-new-password")
    print("================================================")
    fill = open('kaga.txt',"w")
    fill.write(user)
    fill.write(" : ")
    fill.write(password)
    
name = input