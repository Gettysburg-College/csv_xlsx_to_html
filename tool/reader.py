# %%
import pandas as pd
import numpy as np
from .table import Table
from typing import List, Dict

class Reader:
  DICT_KEYS = ('First-Name', 'Last-Name', 'Middle-Name', 'Exp-Grad')

  def __init__(self, csv_path: str) -> None:
    self.csv_path = csv_path
    # self.__read_file()
    self.list_tables: List[Table] = []

    table_name_list = set()
    curr_rows: List[Dict[str, str]]
    curr_table: Table = Table()

    df = self.__read_file()
    for id, row in df.iterrows():
      # rows like Seniors, Juniors, etc.
      if row[Reader.DICT_KEYS[0]] is str and pd.isnull(Reader.DICT_KEYS[1])\
       and pd.isnull(Reader.DICT_KEYS[2]):

        # if that year does not in list
        if row[0] not in table_name_list:
          table_name_list.add(row[0])

          # create new Table obj
          name = str(row[0])
          id = str(row[0]).lower()
          rows = []
          curr_table = Table(table_id=id, table_name=name, rows=rows)

          # add new Table into list_tables
          self.list_tables.append(curr_table)

          # update curr_rows
          curr_rows = curr_table.rows

      # rows contain student information
      else:
        # add student's info into Dictionary
        my_dict = dict()
        my_dict[Reader.DICT_KEYS[0]] = row[0]
        my_dict[Reader.DICT_KEYS[1]] = row[1]
        my_dict[Reader.DICT_KEYS[2]] = row[2]
        my_dict[Reader.DICT_KEYS[3]] = row[3]

        # add St
        curr_rows.append(my_dict)

  def __read_file(self):
    data = pd.read_csv(self.csv_path, encoding='latin1')
    data = data.dropna(axis=0, how='all')
    return data

  def getData(self):
    table_list = self.list_tables
    for table in table_list:
      pass