import sqlite3


# function takes user input to retrieve values from connection (SQLite database)
def get_mvp(user_input, connection):
    # create cursor to execute interact with database
    cursor = connection.cursor()
    # if user input is a digit
    if user_input.isdigit():
        # cast user input as integer
        year = int(user_input)
        # if user input (year) matches value under column named 'year' in db, select corresponding player
        cursor.execute("SELECT player FROM mvps WHERE year = ?", (year,))
        # retrieve next row from a query set and return as tuple,
        result = cursor.fetchone()
        if result:
            return result[0]  # return index 0 in tuple
        else:
            return f"No data found for year {year}."
    else:
        # if user input matches value under column named 'player' in db, select corresponding year/s
        cursor.execute("SELECT year FROM mvps WHERE lower(player) = ?", (user_input.lower(),))
        # retrieve all rows from a query set and return as tuple
        result = cursor.fetchall()
        if result:
            sorted_years = sorted([r[0] for r in result])  # sort every instance in result in ascending order
            return ", ".join(str(year) for year in sorted_years)  # return every instance in sorted years in one line
        else:
            return f"{user_input} has never won the MVP award."


def main():
    # connect to the nba_mvps database using 'with' to automatically close connection
    with sqlite3.connect("nba_mvps.db") as connection:
        # ask for user input
        user_input = input("Enter a year or player name: ")
        # call get_mvp function passing 'user_input' and 'connection' arguments and save output in result variable
        result = get_mvp(user_input, connection)
        print(result)


if __name__ == '__main__':
    main()
