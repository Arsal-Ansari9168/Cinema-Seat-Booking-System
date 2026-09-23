#simple Cinema Seat Booking System. Using a while loop and if-elif-else.

seats = [False] * 100

while True:
    print("\n--- Cinema Seat Booking System ---")
    print("1. Book Seat")
    print("2. Cancel Seat")
    print("3. Show Available Seats")
    print("4. Show Booked Seats")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        seat = int(input("Enter seat number (1-100): "))

        if seat < 1 or seat > 100:
            print("Invalid seat number")
        elif seats[seat - 1] == False:
            seats[seat - 1] = True
            print("Seat booked successfully")
        else:
            print("Seat already booked")

    elif choice == 2:
        seat = int(input("Enter seat number (1-100): "))

        if seat < 1 or seat > 100:
            print("Invalid seat number")
        elif seats[seat - 1] == True:
            seats[seat - 1] = False
            print("Seat cancelled successfully")
        else:
            print("Seat is not booked")

    elif choice == 3:
        print("Available Seats:")
        for i in range(100):
            if seats[i] == False:
                print(i + 1, end=" ")
        print()

    elif choice == 4:
        print("Booked Seats:")
        for i in range(100):
            if seats[i] == True:
                print(i + 1, end=" ")
        print()

    elif choice == 5:
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice")
        
        
# Value	Meaning
# False	Seat is available
# True	Seat is booked