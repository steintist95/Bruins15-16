# from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector
# import BruinsSchedule
# import bruinsCalendar
import csv



#Main file
#Reads data from Bruins Full Schedule (CSV file) and imports data into Bruins2015 Database
#After importing into database, the score is added to my calendar

bruinsCSV = open('full.csv', 'rb')

cnx = mysql.connector.connect(user='jstein', password='deffhalen123', database='Bruins2015', host='127.0.0.1')
cursor = cnx.cursor()

tomorrow = datetime.now().date() + timedelta(days=1)
print tomorrow

addGame = ("INSERT INTO record "
           "(Day, opponent, homeAway, winLose, score) "
           "VALUES (%(Day)s, %(opponent)s, %(homeAway)s, %(winLose)s, %(score)s);")


data_game = {
    'Day': str(raw_input('Enter Date: ')),
    'opponent': str(raw_input('Enter Opponent: ')),
    'homeAway': str(raw_input('Enter Home or Away: ')),
    'winLose': str(raw_input('Enter Win or Lose: ')),
    'score': str(raw_input('Enter Score: ')),
}

cursor.execute(addGame, data_game)

cnx.commit()
cursor.close()
cnx.close()