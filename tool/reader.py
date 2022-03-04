
import pandas as pd
from .table import Table
from typing import List

class Reader:
  def __init__(self, csv_path: str) -> None:
    self.csv_path = csv_path
    # self.__read_file()
    self.tables: List[Table] = []

  def __read_file(self):
    pass