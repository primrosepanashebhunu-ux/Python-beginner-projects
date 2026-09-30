shopping_list=[]
while True:
    print("----MY SHOPPING LIST----")
    print("1.ADD ITEM")
    print("2.SORT ITEMS IN ORDER")
    print("3.REMOVE ITEM")
    print("4.CHECK IF ITEM IS ON THE LIST")
    print("5.EXIT SHOPPING LIST")
    choice=input("Enteroption from 1-5 :")
    if choice=="1":
        item=input("What item do you want to add?  :")
        shopping_list.append(item)
        print("Item successfully added ")
    elif choice=="2":
     shopping_list.sort()
    elif choice=="3":
       item=input("What do you want to remove?   ")
       if item in shopping_list:
          shopping_list.remove(item)
          print(f"{item} removed")
       else:
          print("Theitem was not found")
    elif choice=="4":
       if len(shopping_list)==0:
          print("Your list is empty")
       
