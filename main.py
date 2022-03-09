from re import S
from tool.reader import Reader
from tool.table import Table

csv_path = "./data/Deans Commendation List.csv"
r = Reader(csv_path)

r.getData()