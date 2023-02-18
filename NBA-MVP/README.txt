Simple command-line program for accessing data about the NBA's Most Valuable Player (MVP) award winners.
The program prompts the user to enter a valid year or player name and returns the name of the MVP winner for that year, or the years in which a given player has won the award.

The folder has 3 files: 

1.) nba_mvps.db: A SQLite database to store and access data
2.) db_config.py: Pyhton script used to configure the database
3.) main.py: The script with the main code of the program, with two functions; -
-
a.) get_mvp(): responsible for executing SQL queries to retrieve data from the database
b.) main(): serving as the entry point to the program, it handles user input and output.

Overall, the program is a simple and effective way to retrieve data about NBA MVP winners, and it provides a good starting point for more complex projects involving SQLite databases and command-line interfaces.
