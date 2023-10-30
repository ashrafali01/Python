#2) create dictionary to store player name and runs scored of at least 5 players. Display it. Now convert this dictionary ‌into Series object and print it.

import pandas as nd
dict ={}

for x in range(5):
    name=input(" Name of Batsmen - ")
    runs=int(input("Runs scored - "))

    dict[name]=runs

ScoreCard=nd.Series(dict)

print(ScoreCard)