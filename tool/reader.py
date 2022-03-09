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
    curr_rows: List[Dict[str, str]] = []
    curr_table: Table = Table()

    df = self.__read_file()
    for id, row in df.iterrows():
      # new table for Seniors, Juniors, etc.
      # print(pd.isna(Reader.DICT_KEYS[1]))
      if row[Reader.DICT_KEYS[0]] is not None and pd.isna(row[Reader.DICT_KEYS[0]]) and pd.isna(row[Reader.DICT_KEYS[2]]):
      # and pd.isnull(Reader.DICT_KEYS[1]) and pd.isnull(Reader.DICT_KEYS[2]):

        # if that year does not in list
        if row[0] not in table_name_list:
          table_name_list.add(row[0])

          # create new Table obj
          name = str(row[0])
          id = str(row[0]).lower()
          rows = []
          curr_table = Table(table_id=id, table_name=name, rows=rows)

          print(f'{name} : {id}')

          # add new Table into list_tables
          self.list_tables.append(curr_table)

          # update curr_rows
          curr_rows = curr_table.rows

      # rows contain student information
      else:
        # print('new student')

        # add student's info into Dictionary
        my_dict = dict()
        my_dict[Reader.DICT_KEYS[0]] = row[0]
        my_dict[Reader.DICT_KEYS[1]] = row[1]
        my_dict[Reader.DICT_KEYS[2]] = row[2]
        my_dict[Reader.DICT_KEYS[3]] = row[3]

        # add St
        curr_rows.append(my_dict)
        print(f'{id}:\t{my_dict}')

  def __read_file(self):
    data = pd.read_csv(self.csv_path, encoding='latin1')
    data = data.dropna(axis=0, how='all')
    print('finish read data')
    return data

  def getData(self):
    for table in self.list_tables:
      print(f'{table.table_name} - id= {table.table_name}')
      for student in table.rows:
        print(f'last: {student[Reader.DICT_KEYS[1]]} \t fist: {student[Reader.DICT_KEYS[0]]}\
         \t mid: {student[Reader.DICT_KEYS[2]]} \t grad_year {student[Reader.DICT_KEYS[3]]}')
      print()
  
    return self.list_tables.copy()