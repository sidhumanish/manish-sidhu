import mysql.connector as sql
conn = sql.connect(host="localhost", user="root", password="your_mysql_password", database="moviebooking")

def add_movie():
    movie_name = input("Enter movie name: ")
    genre = input("Enter genre: ")
    duration = int(input("Enter movie duration (in minutes): "))
    language = input("Enter movie language: ")
    rating = float(input("Enter movie rating: "))
    showtime=input("Enter Showtime(HH:MM:SS):")
    showdate=input("Enter Showdate(YYYY-MM-DD):")
    available_seats=int(input("Enter number of seats available:"))
    price=float(input("Enter the price of each seat:"))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Movies (movie_name, genre, duration, language, rating)\
                   VALUES ('{}','{}','{}','{}','{}')".format(movie_name, genre, duration, language, rating))
    cursor.execute("INSERT INTO Showtimes(movie_name,show_date,show_time,available_seats,price) VALUES ('{}','{}','{}','{}','{}')"\
                   .format(movie_name,showdate,showtime,available_seats,price))
    conn.commit()
    print("Movie ", movie_name, " added successfully!")

def view_movies():
    cursor = conn.cursor()
    cursor.execute("SELECT movie_name, genre, duration, language, rating FROM Movies")
    movies = cursor.fetchall()
    if movies:
        print("\nAvailable Movies:")
        for movie in movies:
            moviename = movie[0]
            cursor.execute("SELECT movie_name, show_time, show_date, available_seats, price FROM Showtimes WHERE movie_name = %s", (moviename,))
            showtime = cursor.fetchone()
            if showtime:
                print("MOVIE NAME:", movie[0], "\tGENRE:", movie[1], "\tDURATION:", movie[2], "\tLANGUAGE:", movie[3], "\tRATING:", movie[4], 
                      "\nSHOW TIME:", showtime[1], "\tSHOW DATE:", showtime[2], "\tAVAILABLE SEATS:", showtime[3], "\tPRICE:", showtime[4])
    else:
        print("No movies available.")


def book_ticket():
    user_id = int(input("Enter your user ID: "))
    username=input("Enter your Username:")
    password=input("Enter your Password:")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users")
    user= cursor.fetchall()
    for j in range (len(user)):
        flag=0
        for i in user:
            if username==i[1] and user_id==i[0] and password==i[2]:
                flag=1
                break
        if flag==1:
            print("User confirmed!")
            print("All available movies are:")
            view_movies()
            moviename=input("Enter Movie Name you are wishing to watch:")
            cursor.execute("SELECT movie_name,show_date,show_time,\
                           available_seats,price FROM Showtimes WHERE movie_name=%s",(moviename,))
            showtimes = cursor.fetchall()
            if not showtimes:
                print("No Showtimes available for the movie you requested!")
            else:
                print("Available showtimes for the movie is:")
                for showtime in showtimes:
                    print("\tDate:{",showtime[1],"},\tTime:{",showtime[2],"},\tAvailable seats: {",showtime[3],"},\n Price per Ticket: {",showtime[4],"}")
                    cursor.execute("SELECT available_seats,price FROM Showtimes WHERE movie_name=%s",(moviename,))
                    showtime=cursor.fetchone()
                    while showtime:
                        seats = int(input("Enter number of seats to book: "))
                        if showtime[0] >= seats:
                            total_amount = showtime[1] * seats
                            print("Your booking has been successfully completed! TOTAL AMOUNT = {",total_amount,"}")
                        else:
                            print("Not enough seats available.")
                        break
        if flag==0:
             print("Invalid User!")
             break
        
def admin_login():
    name = input("Enter admin username: ")
    adminpassword = input("Enter admin password: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Admin")
    admin = cursor.fetchall()
    for j in range (len(admin)):
        flag=0
        for i in admin:
            if name==i[1] and adminpassword==i[2]:
                flag=1
                break
        if flag==1:
            print("Admin login successful!")
            admin_menu()
            break
        if flag==0:
             print("Invalid credentials!")
             break

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Movie")
        print("2. View Movies")
        print("3. Add User:")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_movie()
        elif choice == "2":
            view_movies()
        elif choice=="3":
            add_user()
        elif choice == "4":
            print("Exiting admin menu...")
            break
        else:
            print("Invalid choice!")

def add_user():
    user_id=int(input("Enter USER ID to be alloted to new user:"))
    username=input("Enter Username :")
    password=input("Enter new password:")
    Email=input("Enter user's email address:")
    phone=int(input("Enter user's phone number:"))
    while phone:
        if len(str(phone))==10:
            phone=phone
            break
        else:
            phone=int(input("Enter a valid phone number:"))
            break
    cursor=conn.cursor()
    cursor.execute( "INSERT INTO Users(user_id, username, password, email, phone)\
                    VALUES (%s, %s, %s, %s, %s)", (user_id, username, password, Email, phone) )
    conn.commit()
    print("New User is added!")
    
print("\nMovie Ticket Booking System")
print("1. Admin Login")
print("2. Book Ticket")
print("3. Exit")
choice = input("Choose an option: ")
if choice == "1":
    admin_login()
elif choice=='2':
    book_ticket()
elif choice == "3":
    print("Goodbye!")
else:
    print("Invalid choice!")
