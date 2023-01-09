print("WELCOME TO THE SHOPPING APP!")
admin_id="admin@1000"
admin_pass="100101"
user_id="user@2000"
user_pass="200202"
electronics=[["REFRIGERATORS",46],["MOBILES",30],["WATCHES",41],["WASHING MACHINES",35],["AIR CONDITIONERS",41]]
ref=[["LG",5,18000],["WHIRPOOL",11,12000],["SAMSUNG",15,16000],["LLOYD",5,15000],["MARQ",10,13000]]
mob=[["APPLE",5,80000],["OPPO",7,30000],["SAMSUNG",3,12000],["REALME",5,15000],["REDMI",10,10000]]
wat=[["TITAN",10,1500],["MAXIMA",5,1000],["SONATA",5,800],["BENSON",10,3000],["TUDOR",11,5000]]
wash=[["SAMSUNG",6,14000],["LG",6,16000],["GODREJ",5,12000],["ONIDA",10,13000],["SANSUI",8,9000]]
air=[["VOLTAS",11,34000],["BLUE STAR",6,27000],["PANASONIC",10,39000],["LLOYD",6,29000],["CARRIER",8,37000]]
fashion=[["JEANS",52],["TOPS",62],["FOOTWEAR",92],["DRESSES",96],["ACCESSORIES",188]]
jeans=[["KNEE LENGTH",10,550],["ANKLE LENGTH",15,690],["TROUSERS",15,550],["JUMPY STYLE",10,350],["TRACK PANTS",12,600]]
tops=[["CROP TOPS",20,500],["T-SHIRTS",15,399],["SHIRTS",12,599],["LONG TOPS",15,499]]
foot=[["SHOES",12,899],["SANDLES",20,699],["FLIP FLOPS",20,299],["BOOTS",15,599],["HEELS",25,750]]
dress=[["SHORT DRESS",20,850],["GOWNS",15,1500],["FLARED SKIRTS",21,850],["BODYCONE DRESSES",15,2000],["FLORALS",25,1500]]
access=[["HANDBAGS",50,5000],["SUNGLASSES",30,750],["BELTS",30,549],["CLUCHES",23,650],["JEWELLERS",55,350]]
groceries=[["DRY FRUITS",105],["OIL",11],["SNACKS",102],["SPICES",83,],["TOPPINGS",93]]
dry_fruits=[["CASHEW NUTS",20,"850 per kg"],["ALMONDS",24,"800 per kg"],["PISTA",18,"860 per kg"],["RAISIN",22,"500 per kg"],["WALNUT",21,"408 per kg"]]
oil=[["SAFFOLA OIL",10,"420 per 5L"],["MUSTARD OIL",15,"500 per 5L"],["FORTUNE",20,"399 per 5L"],["NATURE FRESH",15,"499 per 5L"],["EMAMI OIL",11,"550 per 5L"]]
snacks=[["LAYS",25,20],["BISCUIT",15,20],["UNCLE CHIPS",20,20],["BINGO",17,30],["KURKURE",25,20]]
spices=[["TERMERIC POWDER",15,221],["SALT",20,20],["RED CHILLI POWDER",18,200],["BLACK PEPPER",20,200],["BAY LEAVES",10,30]]
toppings=[["TOMATO SAUCE",20,149],["CHILLI SAUCE",15,150],["CHEESE",25,200],["PIZZA TOPPING",33,120]]
f=0
def login():
    a=int(input("If u want to LOGIN enter 1   "))
    if(a==1):
        id=input("enter id  ")
        pas=input("enter password  ")
        if(pas==admin_pass and id==admin_id): 
            print("You are logged in  ")
            f=1
            return f
        else:
            print("You have enterd wrong id and password    ")
def up_elec(lis):
    for i in lis:
            upp=int(input(f"TO UPDATE {i[0]} Press 1    TO EXIT PRESS 0         TO SKIP PRESS ANY OTHER NUMBER      "))
            if(upp==1):
                qty=int(input(f"ENTER NEW QUANTITY FOR {i[0]} "))
                price=int(input(f"ENTER NEW PRICE FOR {i[0]}  "))
                i[1]=qty
                i[2]=price
            elif(upp==0):
                break
            else:
                continue
    return lis
def up_fashion(lis):
    for i in lis:
        upp=int(input(f"TO UPDATE {i[0]} Press 1 TO EXIT PRESS 0    "))
        if(upp==1):
            qty=int(input(f"ENTER NEW QUANTITY FOR {i[0]} "))
            price=int(input(f"ENTER NEW PRICE FOR {i[0]}  "))
            i[1]=qty
            i[2]=price
        elif(upp==0):
                break
        else:
            continue
    return lis
def up_groceries(lis):
    for i in lis:
        upp=int(input(f"TO UPDATE {i[0]} Press 1 TO EXIT PRESS 0    "))
        if(upp==1):
            qty=int(input(f"ENTER NEW QUANTITY FOR {i[0]} "))
            price=int(input(f"ENTER NEW PRICE FOR {i[0]}  "))
            i[1]=qty
            i[2]=price
        elif(upp==0):
                break
        else:
            continue
    return lis
def view1(lis):
    print("PRODUCT      QUANTITY        PRICE(per piece in Rs)")
    for i,j,k in lis:
        print(i,"       ",j,"       ",k) 
def view2(lis):
    print("PRODUCT        PRICE(per piece in Rs)")
    for i in lis:
        print(i[0],"       ",i[2]) 
ch=int(input("enter 1 if you are ADMIN Enter 2 if you are USER  "))
if(ch==1):
        f=login()
        if(f==1):
            while(1):
                sel=int(input("Enter 1 if you wish to manage stock  Enter 2 if you wish to view stock   "))
                if(sel==1):
                    up=int(input("TO UPDATE ELECTRONICS PRESS 1  TO UPDATE FASHION PRESS 2  TO UPDATE GROCERIES PRESS 3     "))
                    if(up==1):
                        while(1):
                            cat=int(input("TO UPDATE REFRIGERATORS PRESS 1 TO UPDATE MOBILES PRESS 2 TO UPDATE WATCHES PRESS 3 TO UPDATE WASHIG MACHINES PRESS 4 TO UPDATE AIR CONDITIONERS PRESS 5 TO EXIT PRESS 0    "))
                            if(cat==1):
                                ref=up_elec(ref)
                            elif(cat==2):
                                mob=up_elec(mob)
                            elif(cat==3):
                                wat=up_elec(wat)
                            elif(cat==4):
                                wash=up_elec(wash)
                            elif(cat==5):
                                air=up_elec(air)
                            else:
                                break
                    elif(up==2):
                        while(1):
                            cat=int(input("TO UPDATE JEANS PRESS 1 TO UPDATE TOPS PRESS 2 TO UPDATE FOOTWEAR PRESS 3 TO UPDATE DRESSES PRESS 4 TO UPDATE ACCESSORIES PRESS 5 TO EXIT PRESS 0    "))
                            if(cat==1):
                                jeans=up_fashion(jeans)
                            elif(cat==2):
                                tops=up_fashion(tops)
                            elif(cat==3):
                                foot=up_fashion(foot)          
                            elif(cat==4):
                                dress=up_fashion(dress)
                            elif(cat==5):
                                access=up_fashion(access)
                            else:
                                break               
                    else:
                        while(1):
                            cat=int(input("TO UPDATE DRY FRUITS PRESS 1 TO UPDATE OIL PRESS 2 TO UPDATE SNACKS PRESS 3 TO UPDATE SPICES PRESS 4 TO UPDATE TOPPINGS PRESS 5 TO EXIT PRESS 0    "))
                            if(cat==1):
                                dry_fruits=up_groceries(dry_fruits)
                            elif(cat==2):
                               oil=up_groceries(oil)
                            elif(cat==3):
                                 snacks=up_groceries(snacks)      
                            elif(cat==4):
                                 spices=up_groceries(spices)
                            elif(cat==5):
                                 toppings=up_groceries(toppings)
                            else:
                                break               
                else:
                    while(1):
                        b=int(input("Enter 1 to view electronics  Enter 2 to view fashion corner  Enter 3 to view groceries    "))
                        print("PRODUCT          QUANTITY   ")
                        if(b==1):
                            for i,j in electronics:
                                print(i,"       ",j)
                            while(1):
                                i=0
                                j=0
                                c=int(input("To view REFRIGERATORS PRESS 1 To view MOBILES PRESS 2 To view WATCHES Press 3 To view WASHNG MACHINES Press 4 To view AIR CONDITIONERS Press 5    "))
                                print("PRODUCT      QUANTITY        PRICE(per piece in Rs)")
                                if(c==1):
                                    view1(ref)
                                elif(c==2):
                                    view1(mob)
                                elif(c==3):
                                   view1(wat)
                                elif(c==4):
                                   view1(wash)
                                else:
                                   view1(air)
                                c=int(input("IF YOU WANT TO EXIT PRESS 0 otherwise PRESS any number "))
                                if(c==0):
                                        break
                        elif(b==2):
                            for i,j in fashion:
                                print(i,"       ",j)
                            while(1):
                                c=int(input("To view JEANS PRESS 1 To view TOPS PRESS 2 To view FOOTWEAR Press 3 To view DRESSES Press 4 To view ACCESSORIES Press 5      "))
                                print("PRODUCT      QUANTITY        PRICE(per piece in Rs)")
                                if(c==1):
                                    view1(jeans)
                                elif(c==2):
                                    view1(tops)
                                elif(c==3):
                                    view1(foot)
                                elif(c==4):
                                    view1(dress)
                                else:
                                    view1(access)
                                c=int(input("IF YOU WANT TO EXIT PRESS 0 otherwise PRESS any number     "))
                                if(c==0):
                                        break
                        elif(b==3):
                            for i,j in groceries:
                                print(i,"       ",j)
                            while(1):
                                c=int(input("To view DRY FRUITS PRESS 1 To view OIL PRESS 2 To view SNACKS Press 3 To view SPICES Press 4 To view TOPPINGS Press 5      "))
                                print("PRODUCT      QUANTITY        PRICE(per packing in Rs)")
                                if(c==1):
                                    view1(dry_fruits)
                                elif(c==2):
                                    view1(oil)
                                elif(c==3):
                                    view1(snacks)
                                elif(c==4):
                                    view1(spices)
                                else:
                                    view1(toppings)
                                c=int(input("IF YOU WANT TO EXIT PRESS 0 OTHERWISE PRESS ANY NUMBER     "))
                                if(c==0):
                                        break
                        else:
                            print("YOU HAVE ENTERED A WRONG CHOICE  ")
                        c=int(input("IF YOU WANT TO EXIT VIEWING STOCK PRESS 0 OTHERWISE PRESS ANY NUMBER   "))
                        if(c==0):
                            break 
                a=int(input("TO LOGOUT ENTRE 0     ELSE PRESS ANY NUMBER     "))
                if(a==0):
                    f=0
                    break    
        else:
            print("YOU ARE NOT LOGGED IN PLEASE TRY AGAIN   ")  
            login()             
elif(ch==2):
    while(1):
        b=int(input("Enter 1 to view electronics  Enter 2 to view fashion corner  Enter 3 to view groceries    "))
        if(b==1):
            while(1):
                c=int(input("To view REFRIGERATORS PRESS 1 To view MOBILES PRESS 2 To view WATCHES Press 3 To view WASHNG MACHINES Press 4 To view AIR CONDITIONERS Press 5    "))
                if(c==1):
                    view2(ref)
                elif(c==2):
                    view2(mob)
                elif(c==3):
                    view2(wat)
                elif(c==4):
                    view2(wash)
                else:
                    view2(air)
                c=int(input("IF YOU WANT TO EXIT PRESS 0 otherwise PRESS any number "))
                if(c==0):
                    break
        elif(b==2):
            while(1):
                c=int(input("To view JEANS PRESS 1 To view TOPS PRESS 2 To view FOOTWEAR Press 3 To view DRESSES Press 4 To view ACCESSORIES Press 5    "))
                if(c==1):
                    view2(jeans)
                elif(c==2):
                    view2(tops)
                elif(c==3):
                    view2(foot)
                elif(c==4):
                    view2(dress)
                else:
                    view2(access)
                c=int(input("IF YOU WANT TO EXIT PRESS 0 otherwise PRESS any number "))
                if(c==0):
                    break
        elif(b==3):
            while(1):
                c=int(input("To view DRY FRUITS PRESS 1 To view OILS PRESS 2 To view SNACKS Press 3 To view SPICES Press 4 To view TOPPINGS Press 5    "))
                if(c==1):
                    view2(dry_fruits)
                elif(c==2):
                    view2(oil)
                elif(c==3):
                    view2(snacks)
                elif(c==4):
                    view2(spices)
                else:
                    view2(toppings)
                c=int(input("IF YOU WANT TO EXIT PRESS 0 otherwise PRESS any number "))
                if(c==0):
                    break
        else:
            print("YOU HAVE ENTERED A WRONG CHOICE  ")
        c=int(input("IF YOU WANT TO EXIT BROWSING ITEMS PRESS 0 OTHERWISE PRESS ANY NUMBER   "))
        if(c==0):
            break 
    print("START ADDING ITEMS TO YOUR CART  ")
    amt=0
    order=[]
    def billing(lis):
        amt=0
        print("ITEM  PRICE")
        for i in lis:
            print(i[0], i[2])
        while(1):
            item=input("enter the item      ")
            qty=int(input("ENTER THE QUANTITY       "))
            for i in lis:
                if(item==i[0]):
                    amt=amt+qty*i[2]
                    order.append([item,qty,amt])
                    break
            exit=int(input("TO EXIT PLACING ORDER PRESS 0    OTHERWISE PRESS ANY NUMBER   "))
            if(exit==0):
                break
            amt=0
    while(1):
        inp=int(input("FOR ORDERING ELECTRONICS PRESS 1  FOR ORDERING FASHION PRESS 2  FOR ORDERING GROCERIES PRESS 3      TO EXIT PRESS 4     "))
        if(inp==1):
            chh=int(input("FOR REFRIGERATORS ENTER 1  FOR MOBILES ENTRE 2  FOR WATCHES ENTER 3  FOR WASHING MACHINES ENTER 4  FOR AIR CONDITIONERS ENTER 5      "))
            if(chh==1):
                billing(ref)
            elif(chh==2):
                billing(mob)
            elif(chh==3):
                billing(wat)
            elif(chh==4):
                billing(wash)
            else:
                billing(air)
        elif(inp==2):
            chh=int(input("FOR JEANS ENTER 1  FOR TOPS ENTRE 2  FOR FOOTWEAR ENTER 3  FOR DRESSES ENTER 4  FOR ACCESSORIES ENTER 5      "))
            if(chh==1):
                billing(jeans)
            elif(chh==2):
                billing(tops)
            elif(chh==3):
                billing(foot)
            elif(chh==4):
                billing(dress)
            else:
                billing(access)
        elif(inp==3):
            chh=int(input("FOR DRY FRUITS ENTER 1  FOR OIL ENTRE 2  FOR SNACKS ENTER 3  FOR SPICES ENTER 4  FOR TOPPINGS ENTER 5      "))
            if(chh==1):
                billing(dry_fruits)
            elif(chh==2):
                billing(oil)
            elif(chh==3):
                billing(snacks)
            elif(chh==4):
                billing(spices)
            else:
                billing(toppings)
        else:
            break
    for i in order:
        amt=amt+i[2]
    print("IF U WISH TO PROCEED WITH YOUR ORDER THEN LOGIN IF YOU ARE NOT LOGGED IN     ")
    if(f==0):
        print("YOU ARE NOT LOGED IN ")
        login()
        print("ENTER YOUR NAME ADDRESS PINCODE     ")
        name=input()
        add=input()
        pin=int(input())
        while(1):
            pre=int(input("TO PREVIEW YOUR ORDER PRESS 1       "))
            if(pre==1):
                print("PRODUCT     QUANTITY      PRICE")
                for i,j,k in order:
                    print(i,"   ",j,"   ",k)
            modify=int(input("IF YOU WISH TO MODIFY ANY PRODUCTS PRESS 1    ELSE PRESS ANY NUMBER       "))
            if(modify==1):
                item=input("ENTER THE PRODUCT NAME YOU WANT TO MODIFY       ")
                new_qty=int(input("ENTER THE NEW QUANTITY       "))
                if(new_qty>0):
                    for i in order:
                        if(i[0]==item):
                            if(new_qty>i[1]):
                                i[2]=i[2]+(new_qty-i[1])*(i[2]//i[1])
                                i[1]=new_qty
                                break
                            else:
                                i[2]=i[2]-(i[1]-new_qty)*(i[2]//i[1])
                                i[1]=new_qty
                                break
                else:
                    for i in order:
                        if(i[0]==item):
                            order.remove(i)
                            break
                for i in order:
                    amt=0
                    amt=amt+i[2]
                print(f"YOUR ORDER AMOUNTING {amt} IS PLACED SUCCESSFULLY   ")
            else:
                print(f"YOUR ORDER AMOUNTING {amt} IS PLACED SUCCESSFULLY   ")
                break





    


    
