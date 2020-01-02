import filecmp
import pathlib
from typing import Union
from os import listdir
from os.path import isfile, join
import pandas as pd
from pandas import DataFrame
import pandas as pd

API_URL = 'https://www.metaweather.com/api/'


def concat_data(
        path: Union[str, pathlib.Path],
):
    data = []
    # 'created','min_temp','temp','max_temp','air_pressure','humidity','visibility','wind_direction','compass,wind_direction','wind_speed'
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for file in files:
        data_temp = pd.read_csv(path +"/"+ file)
        created_temp = data_temp['created']
        created_temp = list(map(lambda x: x[0:10],created_temp))
        data_temp['created'] = created_temp
        
        
        data_temp = data_temp[data_temp.created  == data_temp.applicable_date]
        data_temp = data_temp[['created', 'min_temp', 'the_temp', 'max_temp', 'air_pressure', 'humidity', 'visibility', 'wind_direction_compass', 'wind_direction', 'wind_speed']]
        data.append(data_temp)
    
    data = pd.concat(data)
    data.sort_values(by=['created'])
    
    with open(str(path) + '.csv', 'w+') as f:
        f.write(data.to_csv(index=False))
        

if __name__ == '__main__':
    concat_data('weather_data/523920_2017_03')
    assert filecmp.cmp(
        'lab_10/tasks/expected_523920_2017_03.csv',
        'weather_data/523920_2017_03/'
    )
