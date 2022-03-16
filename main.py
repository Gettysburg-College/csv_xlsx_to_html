import sys

from tool.page import Page
from tool.reader import Reader
from tool.table import Table

if __name__ == "__main__":

  # csv_path = "./data/Deans Commendation List.csv"
  # output_path = "./output/test.html"

  csv_path = sys.argv[1]
  output_path = sys.argv[2]

  r = Reader(csv_path, verbose=True)

  p = Page(r)
  with open(output_path, "w") as f:
    f.write(p.generate())