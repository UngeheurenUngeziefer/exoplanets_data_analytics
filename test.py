import numpy as np
import matplotlib.pyplot as plt
from Exoplanets_basic_info import list, columns, rus_columns

class Diagrams:
    def __init__(self, prmtr_name):
        self.name = prmtr_name
        self.column = list[self.name]
        index_of_prmtr_name = columns.index(prmtr_name)
        self.rus_name = rus_columns[index_of_prmtr_name]
        self.conf_table = list[list['planet_status'] == 'Confirmed'].copy()
        self.confirmed_planets_table_with_prmtr = self.conf_table.dropna(subset=[self.name])



