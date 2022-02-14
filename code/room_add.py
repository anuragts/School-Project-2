from basic import mycursor,mydb

def add_room():
    room_number = int(input("Enter room number: "))
    condition = True
    while condition == True:
        print("""
        Enter room type:
        1. VIP
        2. Deluxe
        3. Normal
        """)
        response = input("Enter your choice: ")
        if response == "1":
            room_type = "VIP"
            condition = False
        elif response == "2":
            room_type = "Deluxe"
            condition = False
        elif response == "3":
            room_type = "Normal"
            condition = False
        else:
            print("Invalid room type")
        
    price = float(input("Enter room price: ₹"))
    # rm = mycursor.execute(f"SELECT * FROM rooms WHERE room_number LIKE {room_number}")
    # print (rm)
    sql = "INSERT INTO rooms (room_number,room_type,price) VALUES(%s,%s,%s)"
    val = (room_number,room_type,price)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"record inserted.")