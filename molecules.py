from Exoplanets_basic_info import list
import pandas as pd
import collections
import itertools
import sys

empty_fields = list['molecules'].isna().sum()
filled_fields = 7013 - empty_fields
list['filled_fields'] = list['molecules'].count()
print('\nПустых полей в столбце molecules: {}, заполненных: {}'.format(empty_fields, filled_fields))
list = list.dropna(how='any', subset=['molecules'])

lines = 0
words = 0
letters = 0

for line in list['molecules']:
    lines += 1
    letters += len(line)

    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'


molecules_dict = collections.Counter(itertools.chain.from_iterable(v.split(',') for v in list.molecules))
molecules_table = pd.DataFrame.from_dict(molecules_dict, orient='index')
molecules_table.reset_index(level=0, inplace=True)
data = {'planets_have': molecules_table[0], 'molecule': molecules_table['index']}
molecules_df = pd.DataFrame(data=data)
molecules_df = molecules_df.sort_values(by='planets_have', ascending=False)
