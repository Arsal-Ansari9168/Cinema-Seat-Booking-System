# 🎬 Cinema Seat Booking System

## 📌 Project Overview

The Cinema Seat Booking System is a simple Python-based console application for managing cinema seat bookings.

The cinema has **100 seats**, numbered from **1 to 100**. Users can book seats, cancel booked seats, and check the availability of seats.

## 🛠️ Technologies Used

* Python
* while loop
* for loop
* if-elif-else
* Lists
* Boolean values
* User Input

## 🎟️ Menu

```text
1. Book Seat
2. Cancel Seat
3. Show Available Seats
4. Show Booked Seats
5. Exit
```

## ⚙️ Features

* 100 cinema seats are available initially.
* Seats are numbered from 1 to 100.
* Users can book an available seat.
* Users cannot book an already booked seat.
* Users can cancel a booked seat.
* Users cannot cancel an available seat.
* Users can view all available seats.
* Users can view all booked seats.
* The menu continues until the user selects Exit.
* Invalid seat numbers are handled by the program.

## 🔄 How the System Works

Initially, all 100 seats are marked as available using:

```python
seats = [False] * 100
```

Here:

* `False` → Seat is available
* `True` → Seat is booked

When a user books a seat, its value changes from `False` to `True`.

When a user cancels a seat, its value changes from `True` to `False`.

## ▶️ How to Run

1. Install Python.
2. Open the project in VS Code or any Python IDE.
3. Open the Python file.
4. Run the program.
5. Select an option from the menu.
6. Enter the seat number when required.
7. Select **Exit** to close the program.

## 📚 Python Concepts Practiced

This project demonstrates:

* Variables
* Lists
* Boolean values
* `while` loop
* `for` loop
* `if-elif-else`
* `input()`
* Type conversion using `int()`
* List indexing
* `break` statement

## 💻 Example

```text
--- Cinema Seat Booking System ---

1. Book Seat
2. Cancel Seat
3. Show Available Seats
4. Show Booked Seats
5. Exit

Enter your choice: 1
Enter seat number (1-100): 25

Seat booked successfully
```

## 🎯 Project Objective

The main objective of this project is to understand how Python can be used to create a simple real-world **seat booking and management system** using basic programming concepts.

## 👨‍💻 Author

**Arsal Ansari**

Python Beginner Project – Cinema Seat Booking System
