import sqlite3

# dictionary with data of NBA MVP winners (key=year, value=player)
nba_mvps = {2022: 'Nikola Jokic', 2021: 'Nikola Jokic', 2020: 'Giannis Antetokounmpo', 2019: 'Giannis Antetokounmpo',
            2018: 'James Harden', 2017: 'Russell Westbrook', 2016: 'Stephen Curry', 2015: 'Stephen Curry',
            2014: 'Kevin Durant', 2013: 'LeBron James', 2012: 'LeBron James', 2011: 'Derrick Rose',
            2010: 'LeBron James', 2009: 'LeBron James', 2008: 'Kobe Bryant', 2007: 'Dirk Nowitzki', 2006: 'Steve Nash',
            2005: 'Steve Nash', 2004: 'Kevin Garnett', 2003: 'Tim Duncan', 2002: 'Tim Duncan', 2001: 'Allen Iverson',
            2000: "Shaquille O'Neal", 1999: 'Karl Malone', 1998: 'Michael Jordan', 1997: 'Karl Malone',
            1996: 'Michael Jordan', 1995: 'David Robinson', 1994: 'Hakeem Olajuwon', 1993: 'Charles Barkley',
            1992: 'Michael Jordan', 1991: 'Michael Jordan', 1990: 'Magic Johnson', 1989: 'Magic Johnson',
            1988: 'Michael Jordan', 1987: 'Magic Johnson', 1986: 'Larry Bird', 1985: 'Larry Bird',
            1984: 'Larry Bird', 1983: 'Moses Malone', 1982: 'Moses Malone', 1981: 'Julius Erving',
            1980: 'Kareem Abdul-Jabbar', 1979: 'Moses Malone', 1978: 'Bill Walton', 1977: 'Kareem Abdul-Jabbar',
            1976: 'Kareem Abdul-Jabbar', 1975: 'Bob McAdoo', 1974: "Kareem Abdul-Jabbar", 1973: 'David Cowens',
            1972: 'Kareem Abdul-Jabbar', 1971: 'Kareem Abdul-Jabbar', 1970: 'Willis Reed', 1969: 'Wes Unseld',
            1968: 'Wilt Chamberlain', 1967: 'Wilt Chamberlain', 1966: 'Wilt Chamberlain', 1965: 'Bill Russell',
            1964: 'Oscar Robertson', 1963: 'Bill Russell', 1962: 'Bill Russell', 1961: 'Bill Russell',
            1960: 'Wilt Chamberlain', 1959: 'Bob Pettit', 1958: 'Bill Russell', 1957: 'Bob Cousy', 1956: 'Bob Pettit'}

# connect to database (database name in string), if none create one with same name
connection = sqlite3.connect('nba_mvps.db')
# create connection cursor in order to execute commands on the database
cursor = connection.cursor()

# execute SQLite query -> create table named 'mvps' in database
cursor.execute('''CREATE TABLE IF NOT EXISTS mvps
                (year integer, player text)''')  # generate cloumns in table by defining their header & data type

# execute SQLite query -> insert dictionary data/values into table named 'mvps'
for year, player in nba_mvps.items():
    cursor.execute('INSERT INTO mvps VALUES (?, ?)', (year, player))

# commit changes to database
connection.commit()
# close database
connection.close()
